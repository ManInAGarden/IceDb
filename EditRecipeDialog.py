import tempfile as tmpf
import copy

import GeneratedGUI as gg
from PersistClasses import Recipe, UnitCat, RecipeIngredientInter
from GuiHelper import *
from IngREecditDialog import *
import sqlitepersist as sqp

class EditRecipeDialog(gg.gEditRecipeDialog):
    INGRED_DEFINS = [
            {"propname":"amount", "title":"Menge"},
            {"propname":"ingredient.unit.value", "title":"Einheit"},
            {"propname":"ingredient.name", "title":"Name"}

        ]
    @property 
    def configuration(self):
        return self._configuration

    
    def __init__(self, parent, fact : sqp.SQFactory, dta : Recipe):
            super().__init__(parent)
    
            GuiHelper.set_icon(self)
            self._fact = fact
            self._docarchive = parent.docarchive
            self._configuration = parent._configuration
            tdir = tmpf.gettempdir()
            self.extdir = tdir + os.path.sep + self._configuration.get_value("archivestore", "localtemp")
            self._recipe = copy.copy(dta)
            self._configuration = parent.configuration
            self._init_gui()

    
    def _init_gui(self):
        self._fact.fill_joins(self._recipe, Recipe.Ingredients)
        self._init_cats()
        GuiHelper.set_columns_forlstctrl(self.m_ingredientsLBCTRL, self.INGRED_DEFINS)

    def _init_cats(self):
        """Initialze catalogs to be used in this dialog"""
        
        #units
        q = sqp.SQQuery(self._fact, UnitCat).where(UnitCat.LangCode=="DEU").order_by(UnitCat.Value)
        self._units = list(q)
    
    def showmodal(self):
        if self._recipe != None:
            self._filldialog()

        return self.ShowModal()

    def _filldialog(self):
        rec = self._recipe
        GuiHelper.set_val(self.m_titleTB, rec.title)
        GuiHelper.set_val(self.m_descriptionTB, rec.description)
        GuiHelper.set_val(self.m_cookingDescriptionTB, rec.cookingdescription)
        GuiHelper.set_data_for_lstctrl(self.m_ingredientsLBCTRL, self.INGRED_DEFINS, rec.ingredients)

    def flushnget(self):
        r = self._recipe
        r.title = GuiHelper.get_val(self.m_titleTB)
        r.description = GuiHelper.get_val(self.m_descriptionTB)
        r.cookingdescription = GuiHelper.get_val(self.m_cookingDescriptionTB)

        self._fact.flush(self._recipe) #parent flush
        self._recipe.ingredients = None
        

        return self._recipe
        
    def addIngreditientLink(self, event):
        """connect a new ingredient to a recipe"""
        igl = RecipeIngredientInter()
        igl.recipeid = self._recipe._id
        dial = IngREecEditDialog(self, self._fact, igl)
        res = dial.showmodal()
        if res != wx.ID_OK:
             return
        recinginter = dial.flushnget()
        
        self.m_ingredientsLBCTRL.DeleteAllItems()
        self._recipe.ingredients = None
        self._fact.fill_joins(self._recipe, Recipe.Ingredients)
        GuiHelper.set_data_for_lstctrl(self.m_ingredientsLBCTRL, self.INGRED_DEFINS, self._recipe.ingredients)

    
    def removeIngreditientLink(self, event):
        seing = GuiHelper.get_selected_fromlctrl(self.m_ingredientsLBCTRL, self._recipe.ingredients)
        if seing is None:
            return
        self._fact.delete(seing)
        reci = sqp.SQQuery(self._fact, Recipe).where(Recipe.Id==self._recipe._id).first()
        self._fact.fill_joins(reci, Recipe.Ingredients)
        self._recipe = reci
        self._filldialog()


    def editIngredientDetails(self, event):
        seing = GuiHelper.get_selected_fromlctrl(self.m_ingredientsLBCTRL, self._recipe.ingredients)
        if seing is None:
            return
        dial = IngREecEditDialog(self, self._fact, seing)
        res = dial.showmodal()
        if res != wx.ID_OK:
                return
        recinginter = dial.flushnget()

        self.m_ingredientsLBCTRL.DeleteAllItems()
        self._recipe.ingredients = None
        self._fact.fill_joins(self._recipe, Recipe.Ingredients)
        GuiHelper.set_data_for_lstctrl(self.m_ingredientsLBCTRL, self.INGRED_DEFINS, self._recipe.ingredients)