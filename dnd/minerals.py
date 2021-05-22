import random
import rangen
import numpy as np
from Ingredientable import Ingredientable




class Mineral(Ingredientable):
    
    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        fractures = ['conchoidal','earthy','hackly','splintery','uneven']

        streak=''   #colour
        lattices = ['cubic','tetragonal','orthorhombic','hexagonal','trigonal','triclinic','monoclinic']
        names = Ingredientable.load_names('minerals')
        
        self.type = 'Mineral'       #This is for the jpg saved
        super().__init__(shapes, textures,p_distr)

        
        self.name = rangen.newWord(names,6)+"ite"
        self.fracture = random.choice(fractures)
        self.lattice = random.choice(lattices)


x = Mineral()

