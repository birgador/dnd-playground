import random
import numpy as np
import plant_classes
import minerals
from PIL import Image



class Recipe:
    verbs = ['freeze','smash','heat','refrigerate','boil','fry','slice','regurgitate','chew and spit the juice']
    adjs = ['a paste forms','bubbles start to appear','soft','crunchy','hard','dry']
    recipients = ['bowl','glass {from material}','grid']
    place_adjs = ['wet','dry','moist','rough','hot','cool','empty']
    # ingredients_list = [plant_classes.Fruit(),'{ingredient from} creature',minerals.Mineral(),'{ingredient from} plant']
    ingredients_list = [plant_classes.Fruit,minerals.Mineral]

    def __init__(self) -> None:
        
        self.ingredients = []
        toxic = random.choice([1,-1])
        for i in range(3):
            
            ingredient = random.choice(self.ingredients_list)()
            if isinstance(ingredient, plant_classes.Fruit):
                ingredient = random.choice([ingredient.core,ingredient.skin,ingredient.seed])
            while ingredient.toxicity/toxic < 0:
                ingredient = random.choice(self.ingredients_list)()
                if isinstance(ingredient, plant_classes.Fruit):
                    ingredient = random.choice([ingredient.core,ingredient.skin,ingredient.seed])

                # print(ingredient.toxicity/toxic)
            self.ingredients.append(ingredient) 
            

        v = [random.choice(self.verbs) for x in range(10)]
        self.desc ="{verb1} the {ingredient1} until {adj1}. Then add {ingredient2} and {verb2}. {verb3} for {timeNum} {timeUnit} and combine with {ingredient3}. Boil with {liq} and let rest.".format(verb1 = random.choice(self.verbs), ingredient1 = self.ingredients[0].name, adj1 = random.choice(self.adjs), ingredient2 = self.ingredients[1].name,verb2 = random.choice(self.verbs),verb3 = random.choice(self.verbs),timeNum=random.randint(1,100),timeUnit = random.choice(["seconds","minutes","hours"]),ingredient3 = self.ingredients[2].name, liq = "water")

        ''' {verb1} the {ingredient1} until {adj1}. Then add {ingredient2} and {verb2}. {verb3} for {timeNum} {timeUnit} and combine with {ingredientz3}. Boil with {liq} and let rest. '''
        pass


    def getIngredients(self):
        
        return self.ingredients

class Potion:

    def __init__(self) -> None:
        
        self.recipe = Recipe()
        self.ingredients = self.recipe.getIngredients()

        # for ingredient in self.ingredients:
        #     if isinstance(ingredient, plant_classes.Fruit):

        self.properties = [(ingredient.props,ingredient.name) for ingredient in self.ingredients]
        

    def describe(self):
        print(self.recipe.desc)
        print(self.properties)

    def describe_ingredients(self):
        for ingredient in self.ingredients:
            ingredient.describe()




for i in range(10):
    potion  = Potion()

    potion.describe()
    # print("describing ingredients")
    # potion.describe_ingredients()
    print("\n")

# ingredients = ['water',plant_classes.Fruit(),'{ingredient from} creature','salt {from a mineral}','{ingredient from} plant']


# liquid_type = ['potion','poison']



# def random_colour():
#     random_number = random.randint(0,16777215)
#     hex_number = str(hex(random_number))
#     hex_number ='#'+ hex_number[2:]
#     if len(hex_number)!=7:
#         hex_number+='0'
#     # print('A  Random Hex Color Code is :',hex_number)
#     im = Image.new('RGB',(1080,1440),hex_number)
#     im.save('test.jpg','JPEG')
#     return hex_number

# def plant_name():
#     pass

# def potion():
#     v = [random.choice(verbs) for x in range(10)]
#     ings = [random.choice(ingredients) for x in range(10)]
    
#     recipient1 = random.choice(recipients)
#     adj1 = random.choice(adjs)
#     place_adj1 = random.choice(place_adjs)
#     time = 'some time'
#     liquid = random.choice(liquid_type)
#     recipes = ['First {} the {} until {}. Then {} and {}.'.format(v[0],ings[0],adj1,v[1],v[2]),'{} the {} with {}. Wait for {} and then proceed to {} and {}. Place on a {} {}.'.format(v[0],ings[0],ings[1],time,v[1],v[2],place_adj1,recipient1),'In a {} place the {} and {} and {}. Quickly mix with {}.'.format(recipient1,ings[0],ings[1],v[0],ings[2])]

#     recipe = random.choice(recipes)
#     colour = random_colour()
#     print(recipe)
#     print('The {} is of colour {}\n'.format(liquid,colour))

#     return recipe

'''I could try and import a list of monsters by CR'''

# for i in range(100):
#     potion = potion()

# recipe1 = 'First {} the {ingredient} until {adj}. Then {} and {}'.format()

# recipe2 = '{} the {ing} with {ing2}. Wait for {time} and then proceed to {} and {}. Place on a {place_adj} {recipìent}'.format()

# recipe3 = 'In a {recipient} place the {ing1} and {ing2} and {}. Quickly mix with {ing3}'

