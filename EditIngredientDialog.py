import GeneratedGUI as gg
import sqlitepersist as sqp
from GuiHelper import *
from PersistClasses import UnitCat, Ingredient

class EditIngredientDialog(gg.gEditIngredientDialog):

    @property 
    def configuration(self):
        return self._configuration
    
    def __init__(self, parent, fact : sqp.SQFactory, ing : Ingredient):
        super().__init__(parent)

        GuiHelper.set_icon(self)
        self._fact = fact
        self._configuration = parent.configuration
        self._ingredient = ing

        self._init_gui()

    def _init_cats(self):
        """Initialze catalogs to be used in this dialog"""
        
        #units
        q = sqp.SQQuery(self._fact, UnitCat).where(UnitCat.LangCode=="DEU").order_by(UnitCat.Value)
        self._units = list(q)

    def _init_gui(self):
        self._init_cats()

    def _filldialog(self):
        ing = self._ingredient
        GuiHelper.set_val(self.m_nameTBC, ing.name)
        GuiHelper.set_val(self.m_unitCB, ing.unit, self._units)
        GuiHelper.set_val(self.m_fatSCD, ing.fat)
        GuiHelper.set_val(self.m_sugarSCD, ing.sugar)
        GuiHelper.set_val(self.m_waterSCD, ing.water)
        GuiHelper.set_val(self.m_caloriesSCD, ing.calories)

    def flushnget(self):
        ing = self._ingredient
        ing.name = GuiHelper.get_val(self.m_nameTBC)
        ing.unit = GuiHelper.get_val(self.m_unitCB, self._units)
        ing.fat = GuiHelper.get_val(self.m_fatSCD)
        ing.sugar = GuiHelper.get_val(self.m_sugarSCD)
        ing.water = GuiHelper.get_val(self.m_waterSCD)
        ing.calories = GuiHelper.get_val(self.m_caloriesSCD)
        
        self._fact.flush(ing)

        return ing

    def showmodal(self):
        self._filldialog()

        return self.ShowModal()
