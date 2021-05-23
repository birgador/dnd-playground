import random
import rangen
import numpy as np
import plant_classes
from Ingredients import Ingredient
from Entities import Entity



class Flower(Ingredient):

    def __init__(self,shapes=Ingredient.shapes, textures = Ingredient.textures,p_distr=Ingredient.p_distr):
        flower_types = ['sympetalous','polypetalous','actinomorphic','zygomorphic']
        
        self.attributes['type'] = 'Flower'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)
        self.attributes['flower_type'] = random.choice(flower_types).title()

class Leaf(Ingredient):

    def __init__(self,shapes=Ingredient.shapes, textures = Ingredient.textures,p_distr=Ingredient.p_distr):
        leaf_types = ['needle','frond','undulate','sinuate','serrate','dentale','lobate','scalloped','palmate','digitate','bipinnatisect','tripinnatisect','pinnatisect','palmatisect','pedate','palmatilobate','bipartite','tripartite','palmatipartite','pinnatipartite','pinnatifid']
        self.attributes['type'] =  'Leaf'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)
        
        self.attributes['leaf_type'] = random.choice(leaf_types).title()

class Root(Ingredient):

    def __init__(self, shapes, textures, p_distr):
        root_types = ['fibrous','taproot','adventitious','creeping','tuberous','water','parasite']  #https://www.botanical-online.com/en/botany/roots-types
        self.attributes['type'] = 'Root'
        
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.attributes['root_type'] = random.choice(root_types)

class Sap(Ingredient):

    def __init__(self, shapes, textures, p_distr):
        sap_adjs = ['placeholder']
        self.type = 'Sap'
        
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.sap = random.choice(sap_adjs)

class Plant(Ingredient):

    def __init__(self,shapes=Ingredient.shapes, textures = Ingredient.textures,p_distr=Ingredient.p_distr):
        
        names = Ingredient.load_names('minerals')
        self.type = 'Plant'
        super().__init__(shapes, textures,p_distr)
        
        
        self.flower = Flower()
        self.leaf = Leaf()
        self.name = rangen.newWord(names,6)+"cea"



class Bark(Ingredient):

    def __init__(self, shapes, textures, p_distr):
        bark_types = ['placeholder']
        self.type = 'Bark'
        super().__init__(shapes=shapes, textures=textures, p_distr=p_distr)

        self.bark = random.choice(bark_types)





        


''' 
- Idea. Crear nova classe que no heredi d'Ingredientable i sigui rollo ingredients_bucket. Tree i fruita en serien, per exemple. Si no, mirar de modificar el cosntructor de les classes per no dependre tant d'Ingredientable i que tingui rollo Tree(root = None, etc)
- Quan es crei una poti, s'escull un tipus d'ingredient. Després és crear l'ingredient i es puja en el construction tree. Els següents components del bucket que s'hagin de crear tindran una chance cumulativa de ser efectius o no. Així s'intentarà tirar per un bucket més o menys equilibrat
- Mirar d'estandaritzar el describe method per a totes les classes, una del bucket i una del ingredientable.
- Potser mirar de crear child class "herb" per parent class "plant". Potser mirar de afegir una propietat rollo, most_common_form_as_ingredient = ['dried','powder', etc]
- Posar classificacions i diversitat per les child classes. 
'''