from pylab import *
import random

def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

def union(lst1, lst2): 
    final_list = lst1 + lst2 
    return final_list

def ointersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value not in lst2] 
    return lst3

    
def assignProb(lst):
    probs=[]
    weights=[]
    cum=0
    for element in lst:
        prob=random.randint(1,100)/1.0
        probs.append(prob)
        cum+=prob
    for p in probs:
        w=round(p/cum,2)
        weights.append(w)
    return weights

def economy():
    generic_res_list=["Metal","Animals","Agriculture","Spices","Woods",\
                  "Minerals"]
    metals=["Gold","Silver","Platinum","Iron","Tin","Copper","Mercury","Zinc","Niquel",\
            "Mithryl","Adamantite","Kurdurite","Titanite"] #Inventar
    
    animals=["Furs","Cattle","Transport","Other"]
    furs=["Furs","Exotic Furs and meat","wool"]
    trans=["Horses","Fantasy land transport","Fantasy air transport"]
    
    gen_res=random.choices(generic_res_list,k=random.randint(1,len(generic_res_list)))
    nat_res=[]
    
    for res in gen_res:
    
        if(res=="Metal"):
            choices=random.choices(metals,k=random.randint(1,3))
            for choice in choices:
                nat_res.append(choice)
        elif(res=="Animals"):
            choices=random.choices(animals,k=random.randint(1,3))
            
                
            for choice in choices:
                if(choice=="Furs"):
                    nat_res.append(random.choices(furs,weights=[0.45,0.1,0.45],k=1))
                elif(choice=="Transport"):
                    nat_res.append(random.choices(trans,weights=[0.45,0.45,0.1],k=random.randint(1,2)))
                elif
        elif(res=="Agriculture"):
            choices=random.choices(metals,k=random.randint(1,3))
            for choice in choices:
                nat_res.append(choice)
        elif(res=="Spices"):
            choices=random.choices(metals,k=random.randint(1,3))
            for choice in choices:
                nat_res.append(choice)
        elif(res=="Woods"):
            choices=random.choices(metals,k=random.randint(1,3))
            for choice in choices:
                nat_res.append(choice)
        elif(res=="Minerals"):
            choices=random.choices(metals,k=random.randint(1,3))
            for choice in choices:
                nat_res.append(choice)
                
                
def genFamily():
    


        
races=["Dwarves","Humans","Elves"]

    
resourcelist=["gold","silver","iron","cattle","crops","wood","stone","fabrics","gems",\
              "horses","Animals"]
product=["jewels","weapons","armor","leather","luxury","ships","tools","spices",\
         "exotic","potions"]

area=int(input("Type the area of the country: "))
tier=input("Type the tier of population density of the country. 1=very low, 2=low, 3=medium, 4=high, 5=very high,0=random ")
tiertrade=input("Type the tier of economic wealth. 1=very poor, 2=poor,3=medium, 4=wealthy, 5=very wealthy,0=random ")
tierlaw=int(input("Type the tier of randomized laws. 1=randomised tier 1 outlawed laws, higher"+\
              "tiers outlawed. 0 for complete randomisation (yields crazy results),-1 "+\
              "for default."+\
              "Default is: murder, slavery, child labor,drug use, drug production, "+\
              "Heavy Weapon ownership, prostitution, fraud, eye for an eye"+\
              "and money laudering are outlawed: "))
tiermagic=int(input("Do you want to randomise taboo schools of magic? Default is Necromancy.\
         Type 0 for fully random, 1 to randomise allowed schools and 2 for default: "))
tierrace=int(input("Choose main race. 1: Humans, 2: Elves, 3: Dwarves, 0: Random"))

#area=50000
#tier=0
#tiertrade=0
#tierlaw=0
#tiermagic=0

print("")
if(int(tier)==0):
    tier=random.randint(1,5)

if int(tier)==1:    
    density=random.randint(30,39) #30-39
elif int(tier)==2:
    density=random.randint(40,59) #40-59
    
elif int(tier)==3:
    density=random.randint(60,79) #60-79
    
elif int(tier)==4:
    density=random.randint(80,99) #80-99

elif int(tier)==5:
    density=random.randint(100,120) #100-120

if(int(tiertrade)==0):
    tiertrade=random.randint(1,5)

if int(tiertrade)==1:    
    wealth=random.randint(1,15) #30-39
elif int(tiertrade)==2:
    wealth=random.randint(16,30) #40-59
    
elif int(tiertrade)==3:
    wealth=random.randint(31,50) #60-79
    
elif int(tiertrade)==4:
    wealth=random.randint(51,79) #80-99

elif int(tiertrade)==5:
    wealth=random.randint(80,130) #100-120     


print("__Economy__")
print("The GDP is: ",int(wealth*1000*2/1.6),"gp and it's a tier: "+str(tiertrade)+" country")


resources=random.sample(resourcelist,k=random.randint(1,5))
production=[]
#resource=resources[0]
for resource in resources:
    
    if(resource=="gold" or resource=="silver" or resource=="gems"):
        products=["jewels("+str(resource)+")","exotic("+str(resource)+")","luxury("+str(resource)+")"]
        production.extend(products)
    elif(resource=="iron" or resource=="cattle"):
        products=["weapons("+str(resource)+")","armor("+str(resource)+")","leather("+str(resource)+")","tools("+str(resource)+")","luxury("+str(resource)+")","exotic("+str(resource)+")"]
        production.extend(products)
    elif(resource=="wood" or resource=="cattle"):
        products=["ships("+str(resource)+")","tools("+str(resource)+")","luxury("+str(resource)+")","exotic("+str(resource)+")"]
        production.extend(products)
    elif(resource=="stone"):
        products=["tools("+str(resource)+")","luxury("+str(resource)+")","exotic("+str(resource)+")"]
        production.extend(products)
    elif(resource=="fabrics"):
        products=["luxury("+str(resource)+")","exotic("+str(resource)+")"]
        production.extend(products)


print("It has: ",", ".join(resources)) 

print("Produces: ",", ".join(production) )
coin=random.randint(1,35)/10.0
print("1 gp is worth "+str(coin)+" times the local currency")
print("Base cost of resources, relate gdp to that and add reasons,Black Market, presence, goods")
print("")
print("__Demographics__")
if(tierrace==0):
    race=random.choice(races)
elif(tierrace==1):
    race="Humans"
elif(tierrace==2):
    race="Elves"
elif(tierrace==3):
    race="Dwarves"
raind=races.index(race)
races.pop(raind)
minorities=races
print("Main race: "+race)
diversity=random.randint(1,3)
if(diversity==3):
    nationals=random.randint(33,50)
    offset=nationals
    min1=random.randint(1,offset)
    offset+=min1
    if(100-offset>0):
        min2=random.randint(1,100-nationals-min1)
    else:
        min2=0
        other=0
    offset+=min2
    other=100-offset
elif(diversity==2):
    nationals=random.randint(51,95)
    offset=nationals
    min1=random.randint(1,100-offset)
    offset+=min1
    if(100-offset>0):
        min2=random.randint(1,100-offset)
    else:
        min2=0
        other=0
    offset+=min2
    other=100-offset
elif(diversity==1):
    nationals=random.randint(96,99)
    offset=nationals
    min1=random.randint(1,100-offset)
    offset+=min1
    if(100-offset>0):
        min2=random.randint(1,100-offset)
    else:
        min2=0
        other=0
    offset+=min2
    other=100-offset

print("Diversity is: ",race+":"+str(nationals)+"%",minorities[0]+": "+str(min1)+"%",minorities[1]+": "+str(min2)+"% Other: "+str(other)+"%")
print("The density is: ", density)
print("Area is: ",area," km2")
pop=float(density*area)
a=random.randint(1,4)
b=random.randint(1,4)
m=a+b+10
cappop=sqrt(pop)*m
a=random.randint(1,4)
b=random.randint(1,4)
citypop=(a+b)*0.1*cappop

print("country: ",int(pop))
print("capital: ",int(cappop))
print("city #2: ",int(citypop))
i=2
while citypop >=8000:
    i=i+1
    a=random.randint(1,4)
    b=random.randint(1,4)
    citypop=(a+b)*0.05*citypop
    if citypop<8000:
        print("city #"+str(i)+" :", 8000+random.randint(1000,2000))

a=random.randint(1,8)
b=random.randint(1,8)
numtowns=(a+b)*i

for j in range(numtowns):
    townpop=random.randint(1000,7999)
    print("town #"+str(j+1)+" :",int(townpop))

print("")
print("__Politics__")
power_structure=["unitary estate","federation","confederation"]
power_source=["autocratic","democratic","oligarchic"]
power_duration=["death","end of term"]
power_transfer=["hereditary","elective","agreement"]
power_holders=["ecclesiastic elite","elite of mages","aristocrats","intellectuals","merchants"]
power_economy=["capitalist","feudalist","totalitarian","tribalism"]
pol_agendas=["National development","Build trade agreements","Reform military",\
             "Secure resource by conquest","Racial cleansing","Reform economy",\
             "Focus on Magical development","Expand borders","Conquer known world",
             "Unify race under single banner","Eliminate rebels","Isolationism",\
             "Secure and build new trade routes"]

gov=random.choice(power_source)+" "+random.choice(power_structure)
transfer=random.choice(power_transfer)

duration=random.choice(power_duration)
holder=random.choice(power_holders)
economy=random.choice(power_economy)
inv=["very low","low","medium","high","very high"]
gov_inv=random.choice(inv)
    

gov_support=random.randint(25,99)

print("The form of government is: "+gov)
#print("Power held by: "+holder+" until: "+duration+" and power transfer is: "+transfer)
print("Power held by: ",holder)
print("Economic system is: "+economy)
print("government involvement in lives, number of factions")
print("governmetn support is: "+str(gov_support)+"%")
print("government control is: "+gov_inv)
print("Agenda: "+", ".join(random.sample(pol_agendas,2)))
print("")
print("__Laws__")
laws=["murder without proven justification","mining without permit","poaching",\
      "gambling","drug possession",\
      "child labor", "slavery", "drug production", \
              "Heavy Weapon ownership", "prostitution","fraud",\
              "money laundering","eye for an eye","conspiracy"]

lawtier1=["poaching","gambling","fraud","drug possession","mining without permit"]
lawtier2=["drug production","Heavy Weapon ownership","prostitution",\
          "money laundering","child labor"]
lawtier3=["murder without proven justification","conspiracy","slavery","eye for an eye" ]

default=["murder without proven justification", "slavery", "child labor", "drug possession", "drug production",\
              "Heavy Weapon ownership", "prostitution", "fraud", "eye for an eye", \
              "money laundering"]
              
            
if(tierlaw==1):
    ranlaws=random.sample(lawtier1,k=random.randint(1,len(lawtier1)))
    #outlawed=union(default,ranlaws)
    ranlaws.extend(lawtier2)
    ranlaws.extend(lawtier3)
    outlawed=ranlaws
    
elif(tierlaw==2):
    ranlaws=random.sample(lawtier2,k=random.randint(1,len(lawtier2)))
    ranlaws.extend(random.sample(lawtier1,k=random.randint(1,len(lawtier1))))
    #outlawed=union(default,ranlaws)
    ranlaws.extend(lawtier3)
    outlawed=ranlaws
    
elif(tierlaw==3):
    ranlaws=random.sample(lawtier1,k=random.randint(1,len(lawtier1)))
    ranlaws.extend(random.sample(lawtier2,k=random.randint(1,len(lawtier2))))
    ranlaws.extend(random.sample(lawtier3,k=random.randint(1,len(lawtier3))))
    #outlawed=union(default,ranlaws)
    outlawed=ranlaws
    
elif(tierlaw==0):
    outlawed=random.sample(laws,k=random.randint(1,len(laws)))
elif(tierlaw==-1):
    outlawed=default

allowed=ointersection(laws,outlawed)

print("Allowed: ",", ".join(allowed))  
print("")  
print("Outlawed: ",", ".join(outlawed),len(outlawed))
print("")
print("__Magic and Religion__")
all_schools=["Abjuration","Conjuration","Divination","Enchantment","Evocation","Illusion",\
               "Necromancy","Transmutation"]
allowed_schools=["Abjuration","Conjuration","Divination","Enchantment","Evocation","Illusion",\
               "Transmutation"]
ban=["Necromancy"]
regulations=["Unregulated","Usable with a license","Forbidden"]
regulated_types=["Full use of magic.",\
                 "All Damaging cantrips and spells are forbidden. Spells over lvl 5 forbidden",\
                 "All Damaging cantrips and spells are forbidden",\
                 "Only non-damaging cantrips allowed"
                 ]
regulation=random.choice(regulations)
#extra_ban=random.randint(0,1)
if(tiermagic==1):
    ban.extend(random.sample(allowed_schools,random.randint(1,len(allowed_schools)-1)))
elif(tiermagic==0):
    ban=random.sample(all_schools,random.randint(1,len(all_schools)))
    
print("Magic usage is: "+regulation)

if(regulation=="Usable with a license"):
    type_of_reg=random.choice(regulated_types)
       
else:
    type_of_reg="None required"
print("License: "+type_of_reg)
    

#if(regulation=="Banned shcools" or regulation=="Usable with a license"):
#    ban.extend(random.sample(all_schools,random.randint(1,len(allowed_schools)-1)))
if(regulation=="Forbidden"):
    print("Banned schools of Magic: All")
else:
    print("Banned schools of Magic: "+", ".join(ban))
gods=["Alasia","Bestus","Hetesis","Tudros","Viesis"]
god=random.choice(gods)
print("Main god is: "+god)
zealous=random.randint(0,1)
razel=gods.index(god)
gods.pop(razel)
ban_gods=["Daasis","Sinmos"]
if(zealous==1):
    ban_gods.extend(random.sample(gods,k=random.randint(1,len(gods))))
print("Sacrilegous gods: "+", ".join(ban_gods))
#print("")
#print(len(allowed)+len(outlawed),len(laws))
#print("")
#print("laws: ",", ".join(laws),len(laws))

print("__Culture__")
print("")
print("__History__")
events=["won war","lost war","Famine","plague","economic crisis","dynasty change",\
        "assassination","change of government","economic boom","civil war","rebellion"]
major_events=["foundation"]
major_events.extend(random.choices(events,k=random.randint(1,len(events))))
war_num=major_events.count("won war")+major_events.count("lost war")
casus_bellis=["border dispute","Discovered Spy","Diplomatic Insult","Religious","Trade conflict",\
              "Conquest","Independence","Racial war","Liberation","Claim on other Throne",\
              "Spread of ideology","Change of government type","Intervention"]

if(war_num>0):
    casus_belli=random.sample(casus_bellis,k=war_num)

cb=0    
print("Major events: ")
for event in major_events:
    if(event=="won war" or event=="lost war"):
        print(event,"Casus belli:"+casus_belli[cb])
        cb+=1
    else:
        print(event)
    

#War generator

print("Fa 818 anys pre-forgetting")