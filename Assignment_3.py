#ASSIGNMENT #3

import random

#input hero's name
print("You want to be a hero, huh? Well, hero, who are you?")
name = input( "Enter your name: ")
print(f'nice to meet you {name}!')
home = input("and dear hero, where do you call home: ?")
answer = input("Are you ready: ")
print(f'You’re not a hero yet {name}. You will need some gear.')


print("There should be some weapons in the chest over there. Go take a look.")

wpons = {'dagger': [2, 1, 1],'stick': [2, -2, 3], "wand":[2,2,2], 'sword':[-2,3,-1], 'pebble':[1,-2,3]}

#INPUT FOR WEAPON
chest = input("Type open to open the chest: ")
if chest == "open":
    # Randomly choose a weapon (property) from the dictionary 
    weapon = random.choice(list(wpons))
    print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
    # Get the values of the chosen weapon
    sk1 = wpons[weapon][0]
    ft1 = wpons[weapon][1]
    rn1 = wpons[weapon][2]
else:
    print("If this is your first time opening a chest try starting with the word open.")
    chest = input("Type open to open the chest: ")
    if chest == "open":
        weapon = random.choice(list(wpons))
        print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
        sk1 = wpons[weapon][0]
        ft1 = wpons[weapon][1]
        rn1 = wpons[weapon][2]
    else:
        print("Open the chest.")
        chest = input("Type open to open the chest: ")
        if chest == "open":
            weapon = random.choice(list(wpons))
            print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
            sk1 = wpons[weapon][0]
            ft1 = wpons[weapon][1]
            rn1 = wpons[weapon][2]
        else: 
            print("*You open the chest*")
            weapon = random.choice(list(wpons))
            print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
            sk1 = wpons[weapon][0]
            ft1 = wpons[weapon][1]
            rn1 = wpons[weapon][2]
            
############################################################################################################################################  

#INPUT TO ROLL FOR armor
print(f'With your {weapon} in hand you should check out the armory and pick somthing out.')
#Create armor dictionary 
#Format → ‘armor’: [S,F,R]
#S = sneak, F = fight, R = run

arm = {'casual clothes': [1, -4, 1],'light armor': [2,2,2], 'medium armor':[1,3,-1], 'heavy armor':[-6,4,-4], 'magical robes':[2,5,2],
'bubblewrap':[-11,-4,-3], '...birthday suit?':[1,-4,11]}

armory = input("Type armory to pick out armor: ")
if armory =="armory":
    armor = random.choice(list(arm))
    print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
    sk2  = arm[armor][0]
    ft2 = arm[armor][1]
    rn2 = arm[armor][2]
else:
    print("My appologizes the armory is on my right not yours. Follow the sign that says armory")
    armory = input("Type armory to pick out armor: ")
    if armory == "armory":
        armor = random.choice(list(arm))
        print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
        sk2  = arm[armor][0]
        ft2 = arm[armor][1]
        rn2 = arm[armor][2]
    else:
        print("I see you need a map. Here: a-r-m-o-r-y")
        armory = input("Type armory to pick out armor: ")
        if armory=="armory":
            armor = random.choice(list(arm))
            print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
            sk2  = arm[armor][0]
            ft2 = arm[armor][1]
            rn2 = arm[armor][2]
        else:
            print("*you go to the armory*")
            armor = random.choice(list(arm))
            print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
            sk2  = arm[armor][0]
            ft2 = arm[armor][1]
            rn2 = arm[armor][2]
            
############################################################################################################################################

import matplotlib.pyplot as plt

stats = input("Before you go lets take a quick look at your hero stats. type stats to open hero stats: ")
if stats=="stats":
    skt = sk1 +sk2
    ftt = ft1 +ft2
    rnt = rn1 +rn2
    categories = ["Sneak", "Fight", "Run"]
    values =  [skt, ftt, rnt]
    color=["darkslateblue", "firebrick", "limegreen"]
    plt.bar(categories, values, color=color)
    plt.xlabel("Stats")
    plt.ylabel("Modifier")
    plt.title("Hero Stats")
    plt.axhline(y=10, color="black", linestyle="--", label="Success")
    plt.axhline(y=0, color="black")
    plt.legend()
    plt.show()
    print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')
else:
    print("are you sure? It could save your life. *hint hint wink wink*")
    stats = input("Before you go lets take a quick look at your hero stats. type stats to open hero stats: ")
    if stats == "stats":
        skt = sk1 +sk2
        ftt = ft1 +ft2
        rnt = rn1 +rn2
        categories = ["Sneak", "Fight", "Run"]
        values =  [skt, ftt, rnt]
        color=["darkslateblue", "firebrick", "limegreen"]
        plt.bar(categories, values, color=color)
        plt.xlabel("Stats")
        plt.ylabel("Modifier")
        plt.title("Hero Stats")
        plt.axhline(y=10, color="black", linestyle="--", label="Success")
        plt.axhline(y=0, color="black")
        plt.legend()
        plt.show()
        print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')
    else:
        print("Wow look at those stats!")
        skt = sk1 +sk2
        ftt = ft1 +ft2
        rnt = rn1 +rn2
        categories = ["Sneak", "Fight", "Run"]
        values =  [skt, ftt, rnt]
        color=["darkslateblue", "firebrick", "limegreen"]
        plt.bar(categories, values, color=color)
        plt.xlabel("Stats")
        plt.ylabel("Modifier")
        plt.title("Hero Stats")
        plt.axhline(y=10, color="black", linestyle="--", label="Success")
        plt.axhline(y=0, color="black")
        plt.legend()
        plt.show()
        print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')

############################################################################################################################################
mon = ["Skeleton", "Giant Spider", "Vampire", "Dragon", "Bandit", "Troll", "Rodents Of Unusual Size"]
monster = random.choice(mon)
print("*you recieve a letter while on your travels*")
print("I hope you are doing well on your quest dear adventure. My old mind is getting the best of me, how long has it been old friend?")
time = input("How long has it been: ")
print("*you send your letter and return to the path of glory*")
print(f' After {time} of treacherous travel you finally get to the treasure cave. As you enter, you spot a monster! Oh no, you spotted a {monster}!')

############################################################################################################################################

import numpy as np

#################################################################

#Titles as lists to randomize from
# t = title
# w = win
tsw = ["the nonchalant", "the Unseen", "the nimble"]
tfw = ["the Brave", "the Mighty", "the Slayer"]
trw = ["the living another day", "the retired", "the cautious"]
# t = title
# f = fail
tsf = ["the not so subtle", "the lead foot", "the loud pop"]
tff = ["the super dead", "the knife at a gunfight", "the food"]
trf = ["the Coward", "the Slow", "the Oops Too Late"]

############################################################################
class dice:
    #initilizes: runs when new dice object is created
    def __init__(self):
        #outcome variables store results of each roll
        self.outcome=0
    #method for fair die roll
    def roll(self):
        #gen random int1-21
        self.outcome=np.random.randint(1,21)
        return self.outcome
        
result = 0
value = 0 

print(f'QUICK! THE {monster} AND ONLY THING THAT STANDS BETWEEN YOU AND THE TREASURE HAS NOTICED YOU!')
print("What will you do, Hero?! SNEAK around the monster by nightfall? FIGHT the monster with your weapon? or RUN away to safety")
act = input("type SNEAK, FIGHT, or RUN: ")

#############################################################
if act == "SNEAK" :
    print(f'You wait for the {monster} to fall asleep before sneaking against the cave walls as you make your way towards the treasure.')
    roll = input('roll for sneak: ')
    sk_die = dice()	
    result += sk_die.roll() 
    value += (result + skt)
    if value >= 10:
        title = random.choice(list(tsw)) 
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} did sneak, as the {monster} did sleep. And {name} {title} left with the treasure without a peep!')
    else: 
        title = random.choice(list(tsf))
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} did sneak, as the {monster} caught on. And {name} {title} is long gone!')
elif act == "FIGHT":
    print(f'You charge into action with you {weapon} drawn and {armor} secured.')
    roll = input("roll for fight: ")
    ft_die = dice()	
    result += ft_die.roll() 
    value += (result + ftt)
    if result >= 10 : 
        title = random.choice(list(tfw)) 
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} lunged and fought! As the {monster} head is servered on a tray, we all cheer and say. Oh {name} {title} was there to slay!')
    else: 
        title = random.choice(list(tff))
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} lunged and fought! As the {monster} attacked, the hero did say! Oh no, {name} {title} should have covered their back!')
elif act == "RUN":
    print(f'You turn on you heals, seath your {weapon} and run as fast as you can away from the {monster}.')
    roll = input("roll for run: ")
    rn_die = dice()	
    result += rn_die.roll() 
    value += (result + rnt)
    if result >= 10:
        title = random.choice(list(trw))
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} turned around and ran! As the {monster} gave up, the Hero did say! Oh my {name} {title} is so lucky to have run away!') 
    else: 
        title = random.choice(list(trf)) 
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} turned around and ran! As the {monster} caught up the hero did say! Oh my {name} {title} will seen!') 
else:
    print(f'You freeze in fear as the {monster} eyes you down hungery for wimpy hero.') 
#########################################################################
print("THE END") 
############################################################################
