import random
import rangen
import numpy as np

class Ingredientable:
    shapes = ['spherical','elliptical','prism','conic','star-shaped','heart-shaped']
    textures = ['abrasive','coarse','dry','flaky','gelatinous','hatched','shiny','tessellated','flat']
    p_distr = rangen.normal_doubled(np.arange(-100,100),20,20,-50,50)
    

    drunk_ranking = []
    time_ranking = [" no time"," 1 round"," 5 rounds"," 1 minute"," 10 minutes"," 1 hour"," 1 day"," 1 week"," 1 month"," 1 year","ever"]
    def __init__(self):
        # self.name = 
        self.colour = rangen.random_colour()
        # self.flavour = None

    def set_name(self,name):
        self.name = name
        

class Fruit_seed(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        
        self.colour = rangen.random_colour('seed')
        self.dimensions = abs(np.int_(np.random.poisson(5,3))) #mm
        self.shape = random.choice(shapes)
        self.texture = random.choice(textures)
        
        self.toxicity = random.choices(np.arange(-100,100),p_distr)[0]
        self.props = rangen.gen_props(self.toxicity)
        if self.toxicity <20:
            self.edible = ""
        else:
            self.edible = "not "


    def describe(self,time_ranking=Ingredientable.time_ranking,effects = []):
        print('Seed is {shape} with dimensions {x}, {y}, {z} mm and is of colour {colour}. Its texture is {texture}'.format(shape = self.shape, x = self.dimensions[0],y = self.dimensions[1],z = self.dimensions[2], colour = self.colour, texture = self.texture))

        print("It has the following properties:",self.props)
        #print(effects)
        

class Fruit_skin(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        
        self.colour = rangen.random_colour('fruit_skin')
        # self.dimensions = abs(np.int_(np.random.poisson(5,3))) #mm
        self.shape = random.choice(shapes)
        self.texture = random.choice(textures)
        
        self.toxicity = random.choices(np.arange(-100,100),p_distr)[0]
        self.props = rangen.gen_props(self.toxicity)
        if self.toxicity <20:
            self.edible = ""
        else:
            self.edible = "not "

    def set_name(self,name):
        self.name = name


    def describe(self,time_ranking=Ingredientable.time_ranking,effects = []):
        print('Skin is of colour {colour}. Its texture is {texture}'.format(colour = self.colour, texture = self.texture))

        print("It has the following properties:",self.props)
        #print(effects)

class Fruit_core(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        
        self.colour = rangen.random_colour('fruit_core')
        self.dimensions = abs(np.int_(np.random.poisson(15,3))) #mm
        self.shape = random.choice(shapes)
        self.texture = random.choice(textures)
        
        self.toxicity = random.choices(np.arange(-100,100),p_distr)[0]
        self.props = rangen.gen_props(self.toxicity)
        if self.toxicity <20:
            self.edible = ""
        else:
            self.edible = "not "


    def describe(self,time_ranking=Ingredientable.time_ranking,effects = []):
        print('Core is {shape} with dimensions {x}, {y}, {z} mm and is of colour {colour}. Its texture is {texture}'.format(shape = self.shape, x = self.dimensions[0],y = self.dimensions[1],z = self.dimensions[2], colour = self.colour, texture = self.texture))

        print("It has the following properties:",self.props)
        #print(effects)



class Fruit(Ingredientable):
    
    with open('files/fr.txt','r') as f:
        read_data = f.readlines()[0]
        data = set(read_data.split(','))

    def __init__(self,data=data):
        self.core = Fruit_core()
        self.skin = Fruit_skin()
        self.seed = Fruit_seed()
        self.name = rangen.newWord(data)
        self.environment = rangen.choose_environment()

    def describe(self):

        print("The fruit is named {} and can usually be found in {}".format(self.name,self.environment))
        self.skin.describe()
        self.core.describe()
        self.seed.describe()

# for i in range(10):
#     x = Fruit()
#     x.describe()
#     print("\n")
#     del x



'''
La idea es tenir una dsitribució en forma de pits amb "zeros" al -101,0 i 101 repreentant la toxicitat dels ingredients. Els ingredients de 0 a -101 seran beneficiosos. Hi haurà una sèrie de rangs que representaran el base-die de l'ingredient. Propers al zero seran d4 i propers a +-100 seran d12 (potser plantejar d20 o d100)

'''

x = Fruit()
print(x.name)