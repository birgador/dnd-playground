import random
import rangen
import numpy as np
from Ingredients import Ingredient




class Mineral(Ingredient):
    
    def __init__(self):
        fractures = ['conchoidal','earthy','hackly','splintery','uneven']

        streak=''   #colour
        lattices = ['cubic','tetragonal','orthorhombic','hexagonal','trigonal','triclinic','monoclinic']
        # names = Ingredientable.load_names('minerals')
        super().__init__()
        self.attributes['type'] = 'Mineral'       #This is for the jpg saved
        

        
        self.attributes['name'] = rangen.newWord('minerals',6)+"ite"
        self.attributes['fracture'] = random.choice(fractures)
        self.attributes['lattice'] = random.choice(lattices)

