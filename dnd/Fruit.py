import random
import rangen
import Seed
from PIL import Image

class Fruit():
    core = ''
    skin = ''
    seed = ''
    with open('files/fr.txt','r') as f:
        read_data = f.readlines()[0]
        data = set(read_data.split(','))

    def __init__(self,data=data):
        self.seed = Seed()
        self.name = rangen.newWord(data)
        self.environment = rangen.choose_environment()


x = Fruit()
print(x.name.title())
    
    
    
    
'''
Has core, 
peel,
seeds
shape

Animal has
blood, 
skin, 
cover
    fur, scales
eyes
saliva
bone
    choose bone?
    marrow
    no_marrow
gland
    gland_name
urine
venom
fangs/teeth
tongue
organs
    organname

plant has
roots
savia
leaves
bark
log

    '''
    