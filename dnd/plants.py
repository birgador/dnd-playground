import random
import rangen
import numpy as np
import plant_classes
from Ingredientable import Ingredientable



class Flower(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        flower_types = ['sympetalous','polypetalous','actinomorphic','zygomorphic']
        
        self.type = 'Flower'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)
        self.flower = random.choice(flower_types)

class Leaf(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        leaf_types = ['needle','frond','undulate','sinuate','serrate','dentale','lobate','scalloped','palmate','digitate','bipinnatisect','tripinnatisect','pinnatisect','palmatisect','pedate','palmatilobate','bipartite','tripartite','palmatipartite','pinnatipartite','pinnatifid']
        self.type =  'Leaf'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)
        
        self.leaves = random.choice(leaf_types)

class Root(Ingredientable):

    def __init__(self, shapes, textures, p_distr):
        root_types = ['placeholder']
        self.type = 'Root'
        
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.root = random.choice(root_types)

class Sap(Ingredientable):

    def __init__(self, shapes, textures, p_distr):
        sap_adjs = ['placeholder']
        self.type = 'Sap'
        
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.sap = random.choice(root_types)

class Plant(Ingredientable):

    def __init__(self,shapes=Ingredientable.shapes, textures = Ingredientable.textures,p_distr=Ingredientable.p_distr):
        
        names = Ingredientable.load_names('minerals')
        self.type = 'Plant'
        super().__init__(shapes, textures,p_distr)
        
        
        self.flower = Flower()
        self.leaf = Leaf()
        self.name = rangen.newWord(names,6)+"cea"



class Bark(Ingredientable):

    def __init__(self, shapes, textures, p_distr):
        bark_types = ['placeholder']
        self.type = 'Bark'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.bark = random.choice(bark_types)


class Tree(Plant):

    def __init__(self, shapes=Plant.shapes, textures=Plant.textures, p_distr=Plant.p_distr):
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.bark = Bark()
        self.leaf = Leaf()
        self.root = Root()
        self.sap_phloem = Sap()     #From leaves/oplace where food created to downwards. Usually sugary
        self.sap_xylem = Sap()      #From roots to rest of tree. Transport water and thingies from oil


        ''' Em falta self.cup_shape = , no em mola idea que tree neixi d'ingredientable a través de plant. No pots fer servir abedul com a ingredient, però sí madera... '''

        fruit = random.choice([True,False])
        if fruit:
            self.fruit = plant_classes.Fruit()
        else:
            self.fruit = None
        


''' 
- Idea. Crear nova classe que no heredi d'Ingredientable i sigui rollo ingredients_bucket. Tree i fruita en serien, per exemple. Si no, mirar de modificar el cosntructor de les classes per no dependre tant d'Ingredientable i que tingui rollo Tree(root = None, etc)
- Quan es crei una poti, s'escull un tipus d'ingredient. Després és crear l'ingredient i es puja en el construction tree. Els següents components del bucket que s'hagin de crear tindran una chance cumulativa de ser efectius o no. Així s'intentarà tirar per un bucket més o menys equilibrat
- Mirar d'estandaritzar el describe method per a totes les classes, una del bucket i una del ingredientable.
- Potser mirar de crear child class "herb" per parent class "plant". Potser mirar de afegir una propietat rollo, most_common_form_as_ingredient = ['dried','powder', etc]
- Posar classificacions i diversitat per les child classes. 
'''