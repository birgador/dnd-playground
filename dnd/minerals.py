from Ingredientable import Ingredientable
import random
import rangen
import numpy as np
from Ingredientable import Ingredientable

class Mineral(Ingredientable):
    fractures = ['conchoidal','earthy','hackly','splintery','uneven']

    streak=''   #colour
    lattice = ['cubic','tetragonal','orthorhombic','hexagonal','trigonal','triclinic','monoclinic']
    names = Ingredientable.load_names('minerals')

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
       self.type = 'Mineral'
       self.name = rangen.newWord(self.names,6)+"ite"
       super().__init__(shapes, textures,p_distr)




x = Mineral()

x.describe()