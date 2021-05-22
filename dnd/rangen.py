import random
import numpy as np
from PIL import Image

def random_colour(name='test'):
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    if len(hex_number)!=7:
        for i in range(7-len(hex_number)):
            hex_number+='0'
    # print('A  Random Hex Color Code is :',hex_number)
    im = Image.new('RGB',(1080,1440),hex_number)
    im.save(name+'.jpg','JPEG')
    return hex_number



def random_name_fruit():
    pass

def choose_environment():
    environments = ['Arctic','Badlands','Coastal','Desert','Forest','Grassland','Hill','Mountain','Swamp','Underdark','Underwater','Urban']

    return random.choice(environments)

# Generates new words based on input using markov chains
def newWord(words,lim=7):
    states = {}
    initial_states = {}
    for word in words:
        chunks, chunk_size = len(word),3
        prev_state = ''
        for i in range(chunks-chunk_size+1):
            state = word[i:i+chunk_size].lower()
            if i == 0:
                if state in initial_states:
                    initial_states[state] += 1
                else:
                    initial_states[state] = 1
            else:
                if prev_state not in states:
                    states[prev_state] = {state:1}
                else:
                    if state in states[prev_state]:
                        states[prev_state][state] += 1
                    else:
                        states[prev_state][state] = 1
            prev_state = state

    # Step 1: Start with some initial random state
    
    new_word =''
    while '.' not in new_word and len(new_word)<lim+random.randint(-3,5):
        initial_state = random.choices(list(initial_states.keys()),list(initial_states.values()))[0]
        new_word += initial_state
    # # Step 2: Select randomly one of its transition states, considering its weights
        next_state = random.choices(list(states[initial_state].keys()),list(states[initial_state].values()))[0]
        new_word += next_state[-1]
    # # Step 3: Append the new state to your generated text

    # # Step 4: Repeat step one using the new state, until a stop character is found, or until you are happy with your result
        # time.sleep(2.0)
    return new_word



def normal_doubled(x,sigma1=1,sigma2=1,mu1=0,mu2=0):

    def normal(x,sigma=1,mu=0):
        p = np.exp(-0.5*((x-mu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))

    
        return p
    
    p1 = normal(x,sigma=sigma1,mu=mu1)
    
    p2 = normal(x,sigma=sigma2,mu=mu2)
    c = 1/np.sum(p1+p2)
    p = (p1+p2)*c
    return p

def normal(x,sigma=1,mu=0):
    p = np.exp(-0.5*((x-mu)/sigma)**2)/(sigma*np.sqrt(2*np.pi))


    return p

def gen_props(toxicity):
    effects = {
        "muscle soarness":{
            "effects":{
                "STR":0,
                "athletics":0,
                "strFlavour":0
            },
            "weights":[],
            "links":["muscle soarness","slow reflexes","fragility"]
        },
        "slow reflexes":{
            "effects":{
                "DEX":0,
                "Acrobatics":0,
                "Sleight of Hand":0,
                "Stealth":0,
                "dexFlavour":0
            },
            "weights":[],
            "links":["slow reflexes","muscle soarness","aempathy"]  
        },
        "fragility":{
            "effects":{
                "CON":0,
                "Concentration":0,
                "conFlavour":0
            },
            "weights":[],
            "links":["fragility","muscle soarness","slow reflexes"]    
        },
        "dizziness":{
            "effects":{
                "INT":0,
                "Arcana, History, Nature and Religion":0,
                "Investigation":0,
                "intFlavour":0
            },
            "weights":[],
            "links":["dizziness","aempathy","obliviousness"]    
        },
        "obliviousness":{   #Despiste
            "effects":{
                "WIS":0,
                "Animal Handling":0,    #Potser et tornes més torpe, o el teu cos fa més sorolls/olors que not cool x animals
                "Insight":0,            # Et tornes més robòtic?
                "Medicine":0,           # Et tremola tot + idem que a INT?
                "Perception":0,         # Més despistat/ ho veus tot més borròs
                "Survival":0,           # Ídem above
                "wisFlavour":0
            },
            "weights":[],
            "links":["obliviousness","dizziness","fragility"]
            
        },
        "aempathy":{                #Think of rabbies? Et tornes més borde. Fàcilment enfadable
            "effects":{
                "CHA":0,
            "Deception":0,
            "Deception":0,
            "Performance":0,
            "Persuasion":0,
            "chaFlavour":0,
            
            },
            "weights":[],
            "links":["aempathy","slow reflexes","dizziness"] 
        }
    }
    time_ranking = [" no time"," 1 round"," 5 rounds"," 1 minute"," 10 minutes"," 1 hour"," 1 day"," 1 week"," 1 month"," 1 year","ever"]
    pass_distr = np.array([19,22,16,11,9,7,6,4,3,2,1])
    num_of_passes = random.choices(np.arange(0,11),pass_distr,k=1)[0]
    
    properties = []

    sign = np.sign(toxicity)
    toxicity = abs(toxicity)
    new_effect = toxicity
    # print(toxicity)
    if num_of_passes != 0:
        x = np.arange(0,100)
        

        #Calculate base die
        die = "no_damage"
        if 50<=toxicity and toxicity<75:
            die = "d4"
        elif 75<=toxicity and toxicity<90:
            die = "d6"
        elif 90<=toxicity and toxicity<96:
            die = "d8"
        elif 96<=toxicity and toxicity<100:
            die = "d10"
        elif toxicity==100:
            die = "d12"

        props = {
            "die":[die,0],
            "drug":0,
            "drunk":0
        }
        for i in range(num_of_passes):           
            if new_effect <20:
                props["drunk"]+=1*sign
            elif 20 <=new_effect and new_effect<50:
                props["drug"]+=1*sign
            elif 50<=new_effect:
                if props["die"][1]==0:

                    if 50<=new_effect and new_effect<75:
                        die = "d4"
                    elif 75<=new_effect and new_effect<90:
                        die = "d6"
                    elif 90<=new_effect and new_effect<96:
                        die = "d8"
                    elif 96<=new_effect and new_effect<100:
                        die = "d10"
                    elif new_effect==100:
                        die = "d12"
                    props["die"][0] = die

                props["die"][1]+=1*sign
            new_effect*=-1    
            while new_effect < 0:
                new_effect = random.choices(x,normal(x,10,abs(toxicity)),k=1)[0]
            # print(toxicity,new_effect)
    else:
        # print("EMPTYYYYYYYYYYYYY")
        props = {
            "die":["no_damage",0],
            "drug":0,
            "drunk":0
        }
    if props["die"][0] != "no_damage":
        if props["die"][1]<0:
            damage = "Heals "+str((-1)*props["die"][1])+str(props["die"][0])
        else:
            damage = "Deals "+str(props["die"][1])+str(props["die"][0])
        properties.append(damage)
    # else:
    #     damage = "Deals no poison damage"
    
    
    poisoned = time_ranking[abs(props["drug"])]
    if props["drug"]>0:
        properties.append("Gives condition poisoned for"+poisoned)
    elif props["drug"]<0:
        properties.append("Gives condition boosted for"+poisoned)
    for i in range(abs(props['drunk'])):
        if i ==0:
            initial_category = random.choice(list(effects))
            links = effects[initial_category]["links"]
            target = random.choice(list(effects[initial_category]["effects"]))
            effects[initial_category]["effects"][target] += 1*(-sign)
        else:
            next_category = random.choices(links,[80,10,10],k=1)[0] #Choose attribute
            target = random.choice(list(effects[next_category]['effects']))   #Choose effect
            links = effects[next_category]["links"]
            effects[next_category]["effects"][target] += 1*(-sign)
        
    for cat in effects:
        for effect in effects[cat]["effects"]:
            property = effects[cat]["effects"][effect]
            if property != 0:
                properties.append([effect,property])

    # print("debug info:",props)
    # print("------------------")
    return properties
        # print("debug info:",props,"sign:",sign)

    
    # prop_num = random.choices(np.arange(0,10),weights,k=1)

    # for i in range(prop_num):
    #     if i ==0:
    #        p = normal_doubled(x,sigma1=1,sigma2=1,mu1=0,mu2=0) 
