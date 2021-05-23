import random
import rangen
import numpy as np
from Ingredients import *



# An entity is an object composed of other objects but has no intrinsic toxicity
class Entity():

    def __init__(self) -> None:
        self.components = {}


    def debug_describe(self):
        for ingredient in self.components:
            print(ingredient,self.components[ingredient])

    def getAllComponents(self):

        def iterate_dict(object):
            return_vals = []

            for key in object:
                if hasattr(object[key],'components'):
                    # return_vals += iterate_dict(object[key].components)
                    pass
                elif isinstance(object[key],dict):
                    return_vals += iterate_dict(object[key])
                else:
                    return_vals.append(object[key])

            return return_vals


        all_comps = iterate_dict(self.components)
        global_props = [comp.attributes for comp in all_comps if comp!=None]
        # for comp in all_comps:
        #     if comp!=None:
        #         print(type(comp))
        
        return global_props
    
    def getAllEffects(self):
        components = self.getAllComponents()
        # effects = {}
        for component in components:
            print(component['type'],component['props'])
            # effects.append({component['type'],component['props']})

    def getEntityIngredients(self):
        ingredients = {}
        for component in self.components:
            if issubclass(type(self.components[component]),Ingredient):
                ingredients[component] = self.components[component]
            elif component == 'Sap':
                ingredients['Phloem'] = self.components[component]['Phloem']
                ingredients['Xylem'] = self.components[component]['Xylem']
                
        return ingredients

    def regurgitate(self):
        
        ingredients = self.getEntityIngredients()
        
        initial_ingredient = random.choice(list(ingredients))   #This selects a random ingredient which will be the initial toxic ingredient. From now on, each new ingredient will have a smaller 
        while ingredients[initial_ingredient].attributes['props'] == []:
            initial_ingredient = random.choice(list(ingredients))
        print('Initial ingredient is '+initial_ingredient)
        del ingredients[initial_ingredient]
        for ingredient in ingredients:
            luck = random.randint(1,6)
            if luck !=6:
                print('Changing '+ingredient+':')
                print('from',ingredients[ingredient].attributes['props'])
                # self.components[ingredient].attributes['props'] = []
                ingredients[ingredient].attributes['props'] = []
                print('to',ingredients[ingredient].attributes['props'])
            else:
                print('Not changing '+ingredient)


    def describe(self):
        # print('{name} can typically be found in {environment}'.format(self.a))
        pass

class Fruit(Entity):
    
    # with open('files/fr.txt','r') as f:
    #     read_data = f.readlines()[0]
    #     data = set(read_data.split(','))

    def __init__(self):
        super().__init__()
        self.components['core'] = Fruit_core()
        self.components['seed'] = Fruit_seed()
        self.components['skin'] = Fruit_skin()
        self.name = rangen.newWord('fr')

class Plant(Entity):
    def __init__(self):
        super().__init__()
        self.components['Leaf'] = Leaf()
        self.components['Root'] = Root()
        self.components['Sap'] = {
            'Phloem':Sap(),     #From leaves/or place where food created to downwards. Usually sugary
            'Xylem':Sap()       #From roots to rest of tree. Transport water and thingies from soil
            }
        self.name = rangen.newWord('fr')+'ea'
        self.environment = rangen.choose_environment()

    def describe(self):
        super().describe()
        print('{name} can typically be found in {environment}'.format(name = self.name,environment = self.environment))
        pprint('It has the following properties {props}'.format(props = self.getAllComponents()))
        return 

class Tree(Plant):

    def __init__(self):
        super().__init__()


        self.components['bark'] = Bark()
        # self.components['Leaf'] = Leaf()
        # self.components['Root'] = Root()
        # self.components['Sap'] = {
        #     'Phloem':Sap(),     #From leaves/or place where food created to downwards. Usually sugary
        #     'Xylem':Sap()       #From roots to rest of tree. Transport water and thingies from soil
        #     }
   
        ''' Em falta self.cup_shape = , no em mola idea que tree neixi d'ingredientable a través de plant. No pots fer servir abedul com a ingredient, però sí madera... '''
        if random.choice([True,False]) == True:
            self.components['Fruit'] = Fruit()
        else:
            self.components['Fruit'] = None


# x = Tree()
# x.describe()
# pprint(x.getEntityIngredients())
# pprint(x.components)

# pprint(x.getAllComponents())