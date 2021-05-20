import random
import rangen
import numpy as np

class Ingredientable:
    shapes = ['spherical','elliptical','prism','conic','star-shaped','heart-shaped']
    textures = ['abrasive','coarse','dry','flaky','gelatinous','hatched','shiny','tessellated','flat']
    p_distr = rangen.normal_doubled(np.arange(-100,100),20,20,-50,50)
    
    

    drunk_ranking = []
    time_ranking = [" no time"," 1 round"," 5 rounds"," 1 minute"," 10 minutes"," 1 hour"," 1 day"," 1 week"," 1 month"," 1 year","ever"]
    type = ''
    def __init__(self,shapes=shapes, textures = textures,p_distr=p_distr):
        
        self.colour = rangen.random_colour(self.type)
        self.dimensions = abs(np.int_(np.random.poisson(5,3))) #mm
        self.shape = random.choice(shapes)
        self.texture = random.choice(textures)
        
        self.toxicity = random.choices(np.arange(-100,100),p_distr)[0]
        self.props = rangen.gen_props(self.toxicity)
        if self.toxicity <20:
            self.edible = ""
        else:
            self.edible = "not "


    def describe(self,time_ranking=time_ranking,effects = []):
        print('{type} is {shape} with dimensions {x}, {y}, {z} mm and is of colour {colour}. Its texture is {texture}'.format(type = self.type,shape = self.shape, x = self.dimensions[0],y = self.dimensions[1],z = self.dimensions[2], colour = self.colour, texture = self.texture))

        print("It has the following properties:",self.props)

    def set_name(self,name):
        self.name = name


    def load_names(file_name):
        with open('files/'+file_name+'.txt','r') as f:
            read_data = f.readlines()[0]
            data = set(read_data.split(','))
        return data


