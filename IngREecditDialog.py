import copy
import sqlitepersist as sqp
import GeneratedGUI as gg
from PersistClasses import RecipeIngredientInter, Ingredient, UnitCat
from GuiHelper import *

class IngREecEditDialog(gg.gIngREecEditDialog):
    """class for editing an intersection bewteen recipes and ingredients"""

    def __init__(self, parent, fact : sqp.SQFactory, dta : RecipeIngredientInter):
        super().__init__(parent)

        GuiHelper.set_icon(self)
        self._fact = fact
        self._configuration = parent._configuration
        self._recinginter = copy.copy(dta)
        self._configuration = parent.configuration
        self._init_gui()

    def _init_gui(self):
        self._init_cats()
        self._init_avail_ingreds()

    def _filldialog(self):
        GuiHelper.set_val(self.m_ammountSCD, self._recinginter.amount)
        GuiHelper.set_val(self.m_ingredCBC, self._recinginter.ingredient, self._ingredients)
        if (self._recinginter.ingredient is None):
            GuiHelper.set_val(self.m_unitTC, None)
        else:
            GuiHelper.set_val(self.m_unitTC, self._recinginter.ingredient.unit.value)

    def showmodal(self):
        self._filldialog()

        return self.ShowModal()

    def _init_cats(self):
        """Initialze catalogs to be used in this dialog"""
        
        #units
        q = sqp.SQQuery(self._fact, UnitCat).where(UnitCat.LangCode=="DEU").order_by(UnitCat.Value)
        self._units = list(q)

    def _init_avail_ingreds(self):
        """Initialize a list of currently available ingredients to be used in the ingredients list for a recipe"""

        q = sqp.SQQuery(self._fact, Ingredient).where(Ingredient.Active==True).order_by(Ingredient.Name)
        self._ingredients = list(q)

    def flushnget(self):
        #get edits
        seling = GuiHelper.get_sqp_objval(self.m_ingredCBC, self._ingredients)
        self._recinginter.ingredientid = seling._id
        self._recinginter.amount = GuiHelper.get_val(self.m_ammountSCD)

        self._fact.flush(self._recinginter)
        return self._recinginter

    def onIngredientSelected(self, event):
        """The user selected a new ingredient"""

        ingred = GuiHelper.get_val(self.m_ingredCBC, self._ingredients)
        GuiHelper.set_val(self.m_unitTC, ingred.unit.value)
