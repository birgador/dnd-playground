import random
from PIL import Image


verbs = ['let rest','smash','heat','refrigerate','boil','fry','slice','regurgitate','chew and spit the juice']
adjs = ['a paste forms','bubbles start to appear','soft','crunchy','hard','dry']
ingredients = ['water','ingredient from fruit','ingredient from creature','salt from a mineral','ingredient from plant']
recipients = ['bowl','glass from material','grid']
place_adjs = ['wet','dry','moist','rough','hot','cool','empty']
liquid_type = ['potion','poison']



def random_colour():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    if len(hex_number)!=7:
        hex_number+='0'
    # print('A  Random Hex Color Code is :',hex_number)
    im = Image.new('RGB',(1080,1440),hex_number)
    im.save('test.jpg','JPEG')
    return hex_number

def plant_name():
    pass

def potion():
    v = [random.choice(verbs) for x in range(10)]
    ings = [random.choice(ingredients) for x in range(10)]
    
    recipient1 = random.choice(recipients)
    adj1 = random.choice(adjs)
    place_adj1 = random.choice(place_adjs)
    time = 'some time'
    liquid = random.choice(liquid_type)
    recipes = ['First {} the {} until {}. Then {} and {}.'.format(v[0],ings[0],adj1,v[1],v[2]),'{} the {} with {}. Wait for {} and then proceed to {} and {}. Place on a {} {}.'.format(v[0],ings[0],ings[1],time,v[1],v[2],place_adj1,recipient1),'In a {} place the {} and {} and {}. Quickly mix with {}.'.format(recipient1,ings[0],ings[1],v[0],ings[2])]

    recipe = random.choice(recipes)
    colour = random_colour()
    print(recipe)
    print('The {} is of colour {}\n'.format(liquid,colour))

    return recipe

'''I could try and import a list of monsters by CR'''

for i in range(100):
    potion = potion()


# recipe1 = 'First {} the {ingredient} until {adj}. Then {} and {}'.format()

# recipe2 = '{} the {ing} with {ing2}. Wait for {time} and then proceed to {} and {}. Place on a {place_adj} {recipìent}'.format()

# recipe3 = 'In a {recipient} place the {ing1} and {ing2} and {}. Quickly mix with {ing3}'

