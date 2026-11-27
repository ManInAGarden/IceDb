import os
import sys
import shutil
import tempfile as tmpf
import platform

import wx
import wx.adv

from ConfigReader import *

import GeneratedGUI as gg
from GuiHelper import GuiHelper
from ABDBTools import APDBTools
import mylogger as mylo

from PersistClasses import Recipe, Ingredient, BasicRecipeIngredientInter, RecipeIngredientInter
from EditRecipeDialog import *
from EditIngredientsDialog import *

class IceDbMain(gg.IceDBMain):
    RECIPE_DEFINS = [
        {"propname":"title", "title":"Rezepttitel", "width":300},
        {"propname":"created", "title":"Angelegt am", "format":"{:%d.%m.%Y %H:%M}"}
    ]

    def __init__(self, parent ):
        super().__init__(parent)
        self._version = "1.0.0"
        GuiHelper.set_icon(self)
        self.init_environ()
        self.init_prog()
        self.init_logging()
        self._dbt = APDBTools(self._configuration, self.logger)
        self.init_archive()
        self.init_db()
        self.init_gui()

    @property
    def configuration(self):
        return self._configuration

    def makesuredirexists(self, filename):
        APDBTools.makesuredirexists(filename)

    def expand_dvalue(self, d : dict, name : str) -> dict:
        """expand any value in the dict with the given key recursively
        and return a coopy of the dict"""
        answ = {}
        for key, val in d.items():
            valt = type(val)
            if valt is str:
                if type(key) is str and key==name:
                    newval = os.path.expandvars(val)
                    answ[key] = newval
                else:
                    answ[key] = val
            elif valt is dict:
                answ[key] = self.expand_dvalue(val, name)
            else:
                answ[key] = val

        return answ

    def expand_dvalueO(self, d : dict, name : str):
        """expand any value in the dict with the given key recursively"""
        for key, val in d.items():
            valt = type(val)
            if valt is str:
                if type(key) is str and key==name:
                    newval = os.path.expandvars(val)
                    d[key] = newval #oh oh does this work?!?
            elif valt is dict:
                self.expand_dvalue(val, name)

    def init_environ(self):
            appdtap = os.environ["AppData"]
            self._appdatapath = os.path.join(appdtap, "IceDb")
            self.makesuredirexists(os.path.join(self._appdatapath, "dummifile"))
    
        
    def init_logging(self):
        cdict = self._configuration.get_section("logging")
        confdict = self.expand_dvalue(cdict, "filename")
        
        lvl = confdict.get("level")
        fname = confdict.get("filename")
        rotsize = confdict.get("maxbytes")

        self.logger = mylo.Logger(lvl)
        self.logger.add_handler(mylo.RotatingFileHandler(fname, rotsize))
        self.logger.info("INF Started IceDB V{} log level is {}", self._version, lvl)

    @property
    def applicationpath(self):
        """return the path wehere the appplication is located
        these files may only be modified by an admin"""
        return self._apppath
    
    @property
    def appdatapath(self):
        """property to get the path where all user modifiable data are located"""
        return self._appdatapath

    @property
    def docarchive(self):
        return self._docarchive


    def _get_app_path(self):
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        elif __file__:
            return os.path.dirname(__file__)
        else:
            raise Exception("Unsupported constellation when trying to get application path")


    def _get_last_dir(self, p : str):
        """getting the last dir element of a path"""
        parts = os.path.split(p)
        l = len(parts)
        return parts[l-1]
    
    def _get_all_but_last_dir(self, p : str):
        """getting all but the last dir"""
        parts = os.path.split(p)
        return parts[0]


    def _get_storagebasics(self):
        dbfilename = self._configuration.get_value_interp("database", "filename")
        currdbdir = os.path.dirname(dbfilename)
        storagepath = self._get_all_but_last_dir(currdbdir)
        dbname = self._get_last_dir(currdbdir)
        return storagepath, dbname

    def _ensure_config(self, cnfname):
        """make sure the config exists. if not try to create it from a distributed version
		"""
        tgtcnfpath = os.path.join(self.appdatapath, cnfname)
        if os.path.exists(tgtcnfpath) and os.path.isfile(tgtcnfpath):
            return

        done = False
        #try an already existing conf file in the application path and copy it to the appdata path
        distcnfpath = os.path.join(self.applicationpath, cnfname)
        done = self.trycopycnf(distcnfpath, tgtcnfpath)

        if done:
            return
        
		#try windows default from the application path
        distcnfpath = os.path.join(self._apppath, "AncPicDb######.conf")
        osname = platform.system()
        done = self.trycopycnf(distcnfpath.replace("######", osname), tgtcnfpath)

        if not done:
            raise Exception("No configuration was found and also could not be created from the os-specific configs")

        return    
    
    def trycopycnf(self, src, tgt):
        if os.path.exists(src) and os.path.isfile(src):
            shutil.copy(src, tgt)
            return True
        else:
            return False


    def init_prog(self):
            self._apppath = self._get_app_path()
            cnfname = "IceDb.conf"
    
            self._ensure_config(cnfname)
            self._configuration = ConfigReader(os.path.join(self.appdatapath, cnfname))
    
            self.storagepath, self.dbname = self._get_storagebasics()

    def init_archive(self):
        """Initialise the archive at the configured path"""
        apath = self._configuration.get_value_interp("archivestore","path")
        self._docarchive = self._dbt.init_archive(apath)
        self.logger.info("Initialised archive at {}", apath)

    def init_db(self):
            dbfilename = self._configuration.get_value_interp("database", "filename")
            self._fact = self._dbt.init_db("IceDb", dbfilename)
            self.logger.info("Initialised DB with database file {}", dbfilename)

    def init_gui(self):
            """fill the gui for the first time. This includes to fetch all initially needed data from the DB"""
            
            #heavily used data with only a small number of records
            self.logger.debug("Initialising the GUI starting")
            
            self.m_mainWindowSB.SetStatusText("DB: {0}".format(self.dbname), 0)
            
            self._csvexpsettings = None

            #creating columnns for recipe list control
            GuiHelper.set_columns_forlstctrl(self.m_recipesLC,
                                            self.RECIPE_DEFINS)
            self.refresh_dash()
            self.logger.debug("Initialising the GUI done")

    def cleanup_temp(self):
        expa = self._dbt.extractionpath
        """delete any temporary files from the temp-dir"""
        if not os.path.exists(expa):
            return

        if not os.path.isdir(expa):
            return

        list_of_files = []
        for root, dirs, files in os.walk(expa):
            for filename in files:
                list_of_files.append(os.path.join(root,filename))
        fct = 0
        dct = 0
        for filename in list_of_files:
            if os.path.isfile(filename):
                os.remove(filename)
                fct += 1
            elif os.path.isdir(filename):
                os.rmdir(filename)
                dct += 1
				
        #lastly remove the temp-dir used for temporary extraction
        os.rmdir(expa)
        self.logger.debug("Cleaned temporary {} files in {} directories", fct, dct+1)


    def refresh_dash(self, prevsel : Recipe = None):
        """do a complete refresh of the main GUI with the list of recipes"""
        
        self.logger.debug("Refreshing the dash")
        self._recipes = self.get_all_recipes()

        self.logger.debug("Found {:d} recipes to be displayed in the main list", len(self._recipes))
        self.m_recipesLC.DeleteAllItems()

        GuiHelper.set_data_for_lstctrl(self.m_recipesLC, self.RECIPE_DEFINS, self._recipes)
        if prevsel is not None:
            GuiHelper.select_item_in_lstctrl(self.m_recipesLC, self._recipes, prevsel)
            self._show_recipe(prevsel)
        else:
            self.m_recipeRT.Clear()

        self.m_mainWindowSB.SetStatusText("Rezepte: {0}".format(len(self._recipes)), 0)


    def get_all_recipes(self):
        q = sqp.SQQuery(self._fact, Recipe).order_by(Recipe.Title, Recipe.Created)
        answ = list(q)

        return answ

    def _show_recipe(self, rec : Recipe):
        self._fact.fill_joins(rec, Recipe.Ingredients)
        consfont = wx.Font(11, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        rt = self.m_recipeRT
        rt.Clear()

        rt.BeginFontSize(14)
        rt.BeginBold()
        rt.WriteText(rec.title)
        rt.EndBold()
        rt.EndFontSize()
        rt.Newline()

        if rec.description is not None:
            rt.BeginFontSize(11)
            rt.BeginItalic()
            rt.WriteText(rec.description)
            rt.EndItalic()
            rt.EndFontSize()
            rt.Newline()
        if rec.ingredients is not None and len(rec.ingredients)>0:
            rt.BeginFontSize(11)
            rt.BeginBold()
            rt.WriteText("Zutaten:")
            rt.EndBold()
            rt.Newline()
            rt.BeginFont(consfont)
            for inginter in rec.ingredients:
                if inginter.ingredient.unit.code=="NUMBER":
                    unival = ""
                else:
                    unival = inginter.ingredient.unit.value

                line = "{:>6n} {:4} {}".format(inginter.amount, unival, inginter.ingredient.name)
                rt.WriteText(line)
                rt.Newline()
            rt.EndFont()
        if rec.cookingdescription is not None:
            rt.BeginFontSize(11)
            rt.BeginBold()
            rt.WriteText("Zubereitung:")
            rt.EndBold()
            rt.Newline()
            rt.WriteText(rec.cookingdescription)
            rt.EndFontSize()
            rt.Newline()

    
    # Handlers for AncPicDBMainFrame events.

    def onRecipeSelected(self, event):
        currec = GuiHelper.get_selected_fromlctrl(self.m_recipesLC, self._recipes)
        if (currec is None):
            return

        self._show_recipe(currec)
    
    def quit( self, event ):
        """The user selected the menu item "close AncPicDb" """
        self.logger.info("Quitting IceDb")
        self.cleanup_temp()
        self.Close()

    def addRecipe(self, event):
        self.logger.info("adding recipe")
        newreci = Recipe()
        newreci.title = "<Neues Rezept>"
        self._fact.flush(newreci) #we need an id to enable connection of ingredients in intersection: recipe/ingredients
        recidial = EditRecipeDialog(self, self._fact, newreci)
        res = recidial.showmodal()
        newp = recidial.flushnget()

        if res != wx.ID_OK:
            self._fact.delete(newp) #eventually added intersection entries are also deleted here - cascading delete
            return
        
        self.refresh_dash()

    def editRecipeButPressed(self, event):
        sel = GuiHelper.get_selected_fromlctrl(self.m_recipesLC, self._recipes)
        if (sel is None):
            self.logger.info("no recipe selected - editing (not) done")
            return
        
        return self.edit_recipe(sel)

    def edit_recipe(self, sel):
        self.logger.info("editing a recipe")

        dial = EditRecipeDialog(self, self._fact, sel)
        res = dial.showmodal()
        if (res!=wx.ID_OK):
            return

        self.logger.info("edit of recipe {} done, saving to database now", sel._id)
        newreci = dial.flushnget()

        self.refresh_dash(newreci)
        self.logger.info("editing a recipe done")


    def deleteRecipe(self, event):
        rec = GuiHelper.get_selected_fromlctrl(self.m_recipesLC, self._recipes)
        if rec is None:
            return
        res = GuiHelper.ask_user(self, "Soll das Rezept '{}' wirklich gelöscht werden?".format(rec.title))
        if res==wx.ID_YES:
            self._fact.delete(rec)
            self.refresh_dash()

    def onListDblClick(self, event):
        selrec = GuiHelper.get_selected_fromlctrl(self.m_recipesLC, self._recipes)
        if selrec is None:
            return

        self.edit_recipe(selrec)

    def OnMenuIngredients(self, event):
        dial = EditIngredientsDialog(self, self._fact)
        res = dial.showmodal()

    def onRepairDB(self, event):
        """Try to repair the database
        """

        #open Recipe/Ingredient intersections
        inters = list(sqp.SQQuery(self._fact, BasicRecipeIngredientInter))
        delinters = []
        for inter in inters:
            if inter.recipeid is not None:
                recipe = sqp.SQQuery(self._fact, Recipe).where(Recipe.Id==inter.recipeid).first_or_default(None)
            else:
                recipe = None

            if recipe is None:
                delinters.append(inter)
                continue

            if inter.ingredientid is not None:
                ingred = sqp.SQQuery(self._fact, Ingredient).where(Ingredient.Id==inter.ingredientid).first_or_default(None)
            else:
                ingred = None

            if ingred is None:
                delinters.append(inter)

        if len(delinters) > 0:
            res = GuiHelper.ask_user(self, "Es werden {} Verknüpfungen von Rezept zur Zutat gelöscht. OK?".format(len(delinters)))
            if res == wx.ID_YES:
                for delinter in delinters:
                    self._fact.delete(delinter)





if __name__ == '__main__':
    app = wx.App()
    frm = IceDbMain(None)
    frm.Show()
    app.MainLoop()