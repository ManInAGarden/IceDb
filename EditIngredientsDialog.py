import GeneratedGUI as gg
from GuiHelper import *
from PersistClasses import Ingredient, UnitCat
from EditIngredientDialog import *

class EditIngredientsDialog(gg.gEditIngredientsDialog):
    INGRED_DEFINS = [
                {"propname":"name", "title":"Name", "width":300},
                {"propname":"unit.value", "title":"Einheit"},
                {"propname":"fat", "title":"Fettanteil"},
                {"propname":"sugar", "title":"Zuckeranteil"},
                {"propname":"water", "title":"Wasseranteil"},
                {"propname":"calories", "title":"Kalorien"},
                {"propname":"active", "title":"Aktiv"}
            ]
    @property 
    def configuration(self):
        return self._configuration

    """Dialog zum Bearbeiten der verfügbaren Zutaten"""
    def __init__(self, parent, fact : sqp.SQFactory):
               super().__init__(parent)
       
               GuiHelper.set_icon(self)
               self._fact = fact
               self._configuration = parent.configuration
               self._ingredients = []
               self._init_gui()
               self._get_ingredients()

    def _init_cats(self):
        """Initialze catalogs to be used in this dialog"""
        
        #units
        q = sqp.SQQuery(self._fact, UnitCat).where(UnitCat.LangCode=="DEU").order_by(UnitCat.Value)
        self._units = list(q)

    def _get_ingredients(self):
         q = sqp.SQQuery(self._fact, Ingredient).order_by(Ingredient.Name)
         self._ingredients = list(q)

    def _init_gui(self):
        self._init_cats()
        GuiHelper.set_columns_forlstctrl(self.m_ingredientsLCTRL, self.INGRED_DEFINS)

    def _filldialog(self):
        GuiHelper.set_data_for_lstctrl(self.m_ingredientsLCTRL, self.INGRED_DEFINS, self._ingredients)
    
    def showmodal(self):
        self._filldialog()

        return self.ShowModal()

    def editIngredient(self, event):
        seling = GuiHelper.get_selected_fromlctrl(self.m_ingredientsLCTRL, self._ingredients)
        if seling is None:
             return

        dial = EditIngredientDialog(self, self._fact, seling)

        res = dial.showmodal()

        if res != wx.ID_OK:
             return
        
        ing = dial.flushnget()