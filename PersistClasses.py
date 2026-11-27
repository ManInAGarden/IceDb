import sqlitepersist as sqp
import datetime


class UnitCat(sqp.PCatalog):
     _cattype = "UNITTYPE"
     _langsensitive = True

class Ingredient(sqp.PBase):
     Id = sqp.UUid()
     Name = sqp.String()
     Unit = sqp.Catalog(catalogtype=UnitCat)
     Fat = sqp.Float()
     Water = sqp.Float()
     Sugar = sqp.Float()
     Calories = sqp.Float()
     UnitWeight = sqp.Float()
     Active = sqp.Boolean(default=True)

     def __str__(self):
          return self.name


class BasicRecipeIngredientInter(sqp.PBase):
     _collectionname = "RecipeIngredientInter"
     RecipeId = sqp.UUid(uniquegrp="repipeingredunique")
     IngredientId = sqp.UUid(uniquegrp="repipeingredunique")
     Amount = sqp.Int()
class RecipeIngredientInter(BasicRecipeIngredientInter):
     Ingredient = sqp.JoinedEmbeddedObject(targettype=Ingredient, localid=BasicRecipeIngredientInter.IngredientId, autofill=True)


class Recipe(sqp.PBase):
     Id = sqp.UUid()
     Title = sqp.String()
     Description = sqp.String()
     CookingDescription = sqp.String()
     Ingredients = sqp.IntersectedList(targettype=RecipeIngredientInter, interupid="recipeid", interdownid="ingredientid", cascadedelete=True)

     def as_string(self):
          return "{}".format(self.title)


     
     


     
def ewn(val):
     if val is None:
          return ""
          
     if type(val) is str:
          return val
     elif type(val) is datetime.datetime:
          return "{:%d.%m.%Y}".format(val)
     elif type(val) is int:
          return "{}".format(val)
     elif issubclass(type(val), sqp.PCatalog):
          return "{}".format(val.value)
     elif issubclass(type(val), sqp.PBase):
          return val.__str__()
     else:
          raise Exception("Unbekannter Datentyp in PersistClasses.py ewn()")
         