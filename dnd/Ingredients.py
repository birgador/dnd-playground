import random
import rangen
import numpy as np
from pprint import pprint

class Ingredient:

    
    # shapes = ['spherical','elliptical','prism','conic','star-shaped','heart-shaped']
    # textures = ['abrasive','coarse','dry','flaky','gelatinous','hatched','shiny','tessellated','flat']
    # p_distr = rangen.normal_doubled(np.arange(-100,100),20,20,-50,50)
    

    drunk_ranking = []
    # time_ranking = [" no time"," 1 round"," 5 rounds"," 1 minute"," 10 minutes"," 1 hour"," 1 day"," 1 week"," 1 month"," 1 year","ever"]
    
    def __init__(self):
        # shapes = ['spherical','elliptical','prism','conic','star-shaped','heart-shaped']
        # print('Initializing '+str(type(self).__name__)+' (Class: Ingredient)')
        self.attributes = {

        }
        textures = ['abrasive','coarse','dry','flaky','gelatinous','hatched','shiny','tessellated','flat']
        p_distr = rangen.normal_doubled(np.arange(-100,100),20,20,-50,50)
        self.attributes['type'] = type(self).__name__
        self.attributes['colour'] = rangen.random_colour(self.attributes['type'])
        # self.dimensions = abs(np.int_(np.random.poisson(5,3))) #mm
        # self.shape = random.choice(shapes)
        self.attributes['texture'] = random.choice(textures)
        
        self.attributes['toxicity'] = random.choices(np.arange(-100,100),p_distr)[0]
        self.attributes['props'] = rangen.gen_props(self.attributes['toxicity'])
        # print("Ingredient:")
        # pprint(self.attributes)
        # if self.toxicity <20:
        #     self.edible = ""
        # else:
        #     self.edible = "not "


    def describe(self,effects = []):
        print('{type} is {shape} with dimensions {x}, {y}, {z} mm and is of colour {colour}. Its texture is {texture}'.format(type = self.type,shape = self.shape, x = self.dimensions[0],y = self.dimensions[1],z = self.dimensions[2], colour = self.colour, texture = self.texture))

        print("It has the following properties:",self.props)

    def set_name(self,name):
        self.attributes['name'] = self.attributes['type']+' of '+name


    def load_names(file_name):
        with open('files/'+file_name+'.txt','r') as f:
            read_data = f.readlines()[0]
            data = set(read_data.split(','))
        return data


class Flower(Ingredient):

    def __init__(self):
        flower_types = ['sympetalous','polypetalous','actinomorphic','zygomorphic']
        super().__init__()
        self.attributes['type'] = 'Flower'
        self.attributes['flower_type'] = random.choice(flower_types).title()

class Leaf(Ingredient):

    def __init__(self):
        super().__init__()
        leaf_types = ['needle','frond','undulate','sinuate','serrate','dentale','lobate','scalloped','palmate','digitate','bipinnatisect','tripinnatisect','pinnatisect','palmatisect','pedate','palmatilobate','bipartite','tripartite','palmatipartite','pinnatipartite','pinnatifid']
        self.attributes['type'] =  'Leaf'
        self.attributes['leaf_type'] = random.choice(leaf_types)

class Root(Ingredient):

    def __init__(self):
        super().__init__()
        root_types = ['taproot','fibrous root','tuberous root','creeping root','water root','adventitious root','parasite root']        #https://www.botanical-online.com/en/botany/roots-types
        self.attributes['type'] = 'Root'  
        self.attributes['root_type'] = random.choice(root_types)

class Sap(Ingredient):

    def __init__(self):
        super().__init__()
        sap_adjs = ['placeholder']
        self.attributes['type'] = 'Sap'
        self.attributes['adjective'] = random.choice(sap_adjs)

# class Plant(Ingredient):

#     def __init__(self):
        
#         names = Ingredient.load_names('minerals')
#         self.type = 'Plant'
#         super().__init__(shapes, textures,p_distr)
        
        
#         self.flower = Flower()
#         self.leaf = Leaf()
#         self.name = rangen.newWord(names,6)+"cea"


class Bark(Ingredient):

    def __init__(self):
        super().__init__()
        bark_types = ['placeholder']
        self.attributes['type'] = 'Bark'
        self.attributes['bark']= random.choice(bark_types)

    # def set_name(self, name):
    #     return super().set_name(self.attributes['type']+' of '+name)

class Ingredient_with_shape(Ingredient):
    def __init__(self):
        # print('Initializing '+str(type(self).__name__)+' (Class: Ingredient_with_shape)')
        super().__init__()
        shapes = ['spherical','elliptical','prism','conic','star-shaped','heart-shaped']
        self.attributes['shape'] = random.choice(shapes)
        # print("Ingredient with shape")
        # pprint(self.attributes)

class Fruit_core(Ingredient_with_shape):

    def __init__(self):
        # print('Initializing '+str(type(self).__name__)+' Fruit_core')
        super().__init__()
        self.attributes['type'] = 'Fruit core'
        # print('Creating new '+type(self).__name__)
        
        # self.colour = rangen.random_colour('fruit_core')
        self.attributes['dimensions (mm)'] = abs(np.int_(np.random.poisson(15,3))) #mm
        # print('Fruit_core')
        # pprint(self.attributes)
        # pprint(self.attributes)

class Fruit_seed(Ingredient_with_shape):

    def __init__(self):
        # print('Initializing'+type(self).__name__+' Fruit_seed')
        super().__init__()
        self.attributes['type'] = 'Fruit seed'
        # print('Creating new '+type(self).__name__)
        
        self.attributes['dimensions (mm)'] = abs(np.int_(np.random.poisson(15,3))) #mm
        

        # print('Fruit_seed')
        # pprint(self.attributes)


class Fruit_skin(Ingredient):
    def __init__(self):
        super().__init__()
        # print('Initializing'+type(self).__name__+' Fruit_skin')
        self.attributes['type'] = 'Fruit skin'
        # print('Creating new '+type(self).__name__)
        # print('Fruit_skin')
        # pprint(self.attributes)
        
# x = Bark()
# x.set_name('uff')
# x.nae