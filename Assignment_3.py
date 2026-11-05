#ASSIGNMENT #3

#Import the random module to allow random selections from lists and dictionaries.
import random
#Imports argparse to handle command-line arguments (like --debug)
import argparse 

#Sets up command-line arguments so the script can accept extra flags when run.
parser = argparse.ArgumentParser()
parser.add_argument(
    "--debug",
    action="store_true",
    help="display the values of the game's variables",
)
#Checks if the user ran the script with the --debug flag enabled.
DEBUG = parser.parse_args().debug
#Creates an empty dictionary to store variable states for debugging.
DEBUG_STATE = {}

#Initializes placeholder variables for dice rolls, totals, and earned titles.
roll = None
total = None
title = None

#Defines a helper function to print and track variable values when debug mode is on.
def debug_print_state(**variables):
    if DEBUG:
        DEBUG_STATE.update(variables)
        print("--- Debug variable values ---")
        for variable, value in DEBUG_STATE.items():
            print(f"{variable} = {value!r}")

#Prints an introductory narrative prompt to the console.
print("You want to be a hero, huh? Well, hero, who are you?")
#Prompts the user to type their name and store it in the 'name' variable. 
name = input( "Enter your name: ")
#Record the name variable into the debug tracking state
debug_print_state(name=name)
#Prints a greeting using an f-string to insert the user's name.
print(f'nice to meet you {name}!')
#Asks the user for their hometown and stores it in 'home'.
home = input("and dear hero, where do you call home?:")
#Record name and home into the debug state
debug_print_state(name=name, home=home)
#Asks the user if they're ready and stores the response in 'answer'.
answer = input("Are you ready: ").strip().lower()
#Record user readiness response into the debug state
debug_print_state(name=name, home=home, answer=answer)
#Prints a story message addressing the hero by name. 
print(f'You’re not a hero yet {name}. You will need some gear.')
#Informs the user about a weapons chest.
print("There should be some weapons in the chest over there. Go take a look.")
#Define a dictionary of weapons where each key maps to a list of stats [sneak, fight, run].
wpons = {'dagger': [2, 1, 1],'stick': [2, -2, 3], "wand":[2,2,2], 'sword':[-2,3,-1], 'pebble':[1,-2,3]}

#INPUT FOR WEAPON
#Asks the user to type 'open' to interact with the chest.
chest = input("Type open to open the chest: ").strip().lower()
#Record the chest input in the debug state
debug_print_state(chest=chest)
#Checks if the user typed 'open' correctly on the first try. 
if chest == "open":
    # Randomly choose a weapon (property) from the dictionary 
    weapon = random.choice(list(wpons))
    #Prints a reaction to the chosen weapon.
    print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
    # Get the values of the chosen weapon
    #Extracts the sneak, fight, and run stat modifier (index 0, 1, and 2, respectively) for the weapon.
    sk1 = wpons[weapon][0]
    ft1 = wpons[weapon][1]
    rn1 = wpons[weapon][2]
    #Update debug state with the chosen weapon and its stats
    debug_print_state(weapon=weapon, sk1=sk1, ft1=ft1, rn1=rn1)
#Executes if the user failed to type 'open'
else:
    #Gives the user a hint and a second chance to type 'open'.
    print("If this is your first time opening a chest try starting with the word open.")
    chest = input("Type open to open the chest: ").strip().lower()
    debug_print_state(chest=chest)
    #Check if the second attempt was correct.
    if chest == "open":
        #Randomly choose a weapon.
        weapon = random.choice(list(wpons))
        #Prints a weapon reaction to show which weapon was found.
        print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
        #Assigns a fight, sneak, or run stat.
        sk1 = wpons[weapon][0]
        ft1 = wpons[weapon][1]
        rn1 = wpons[weapon][2]
        debug_print_state(weapon=weapon, sk1=sk1, ft1=ft1, rn1=rn1)
    #Executes if all previous attempts failed (fallback).
    else:
        #Prints a direct instruction.
        print("Open the chest.")
        #Gives the user a third chance to type 'open'.
        chest = input("Type open to open the chest: ").strip().lower()
        debug_print_state(chest=chest)
        #Check if the third attempt was correct.
        if chest == "open":
            #Randomly choose a weapon.
            weapon = random.choice(list(wpons))
            #Prints a weapon reaction to show which weapon was found.
            print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
            #Assigns a fight, sneak, or run stat.
            sk1 = wpons[weapon][0]
            ft1 = wpons[weapon][1]
            rn1 = wpons[weapon][2]
            debug_print_state(weapon=weapon, sk1=sk1, ft1=ft1, rn1=rn1)
        #Execute if all previous attempts failed (fallback).
        else: 
            #Force open narrative action.
            print("*You open the chest*")
            #Randomly choose a weapon anyway.
            weapon = random.choice(list(wpons))
            #Prints a weapon reaction to show which weapon was found.
            print(f'a {weapon} person ay. I am bow man myself. Many a man have caught an arrow in the knee by my hands.')
            #Assigns a fight, sneak, or run stat.
            sk1 = wpons[weapon][0]
            ft1 = wpons[weapon][1]
            rn1 = wpons[weapon][2]
            debug_print_state(weapon=weapon, sk1=sk1, ft1=ft1, rn1=rn1)
            
############################################################################################################################################  

#INPUT TO ROLL FOR armor
#Prompts user to visit armory.
print(f'With your {weapon} in hand you should check out the armory and pick somthing out.')
#Create armor dictionary 
#Format → ‘armor’: [S,F,R]
#S = sneak, F = fight, R = run

#Defines a dictionary containing different armor types and their corresponding [sneak, fight, run] stat modifiers.
arm = {'casual clothes': [1, -4, 1],'light armor': [2,2,2], 'medium armor':[1,3,-1], 'heavy armor':[-6,4,-4], 'magical robes':[2,5,2],
'bubblewrap':[-11,-4,-3], '...birthday suit?':[1,-4,11]}

#Asks the user to type 'armory'.
armory = input("Type armory to pick out armor: ").strip().lower()
debug_print_state(armory=armory)
#Check if the user typed 'armory' correctly on the first try.
if armory =="armory":
    #Randomly select an armor piece from the dictionary keys.
    armor = random.choice(list(arm))
    #Prints compliment message using the selected armor.
    print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
    #Extracts the armor fight, sneak, or run modifier. 
    sk2  = arm[armor][0]
    ft2 = arm[armor][1]
    rn2 = arm[armor][2]
    debug_print_state(armor=armor, sk2=sk2, ft2=ft2, rn2=rn2)
#Executed if the user failed to type 'armory' on the first try.
else:
    #Prints helpful error message.
    print("My appologizes the armory is on my right not yours. Follow the sign that says armory")
    #Gives a second chance to input 'armory'.
    armory = input("Type armory to pick out armor: ").strip().lower()
    debug_print_state(armory=armory)
    #Checks second attempt.
    if armory == "armory":
        #Randomly selects armor.
        armor = random.choice(list(arm))
        #Prints compliment message using the selected armor.
        print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
        #Extracts the armor fight, sneak, or run modifier.
        sk2  = arm[armor][0]
        ft2 = arm[armor][1]
        rn2 = arm[armor][2]
        debug_print_state(armor=armor, sk2=sk2, ft2=ft2, rn2=rn2)
    #Gives third chance.
    else:
        #Prints map hint.
        print("I see you need a map. Here: a-r-m-o-r-y")
        #Gives a third chance to input 'armory'.
        armory = input("Type armory to pick out armor: ").strip().lower()
        debug_print_state(armory=armory)
        #Checks third attempt.
        if armory=="armory":
            #Randomly select armor.
            armor = random.choice(list(arm))
            #Prints compliment message using the selected armor.
            print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
            #Extracts the armor fight, sneak, or run modifier.
            sk2  = arm[armor][0]
            ft2 = arm[armor][1]
            rn2 = arm[armor][2]
            debug_print_state(armor=armor, sk2=sk2, ft2=ft2, rn2=rn2)
        #Fallback if all input attempts fail.
        else:
            #Forces player to progress. 
            print("*you go to the armory*")
            #Randomly select armor.
            armor = random.choice(list(arm))
            #Prints compliment message using the selected armor.
            print(f"Absolutly dashing! Almost like a knight in shining {armor}.")
            #Extracts the armor fight, sneak, or run modifier.
            sk2  = arm[armor][0]
            ft2 = arm[armor][1]
            rn2 = arm[armor][2]
            debug_print_state(armor=armor, sk2=sk2, ft2=ft2, rn2=rn2)
            
############################################################################################################################################

# Imports matplotlib module for plotting graphs.
import matplotlib.pyplot as plt

#Define a dictionary mapping monsters to their respective difficulty class (DC) target numbers.
mon = {
    "Skeleton": 7,
    "Giant Spider": 14,
    "Vampire": 12,
    "Dragon": 18,
    "Bandit": 4,
    "Troll": 10,
    "Rodents Of Unusual Size": 8,
    "Rodents of Usual Size": 2,
}
#Randomly select a monster from the dictionary.
monster = random.choice(list(mon))
#Look up the difficulty class value for the chosen monster.
difficulty_class = mon[monster]
#Record the chosen monster and its difficulty class in the debug state.
debug_print_state(monster=monster, difficulty_class=difficulty_class)
#Asks user to view stats
stats = input("Before you go lets take a quick look at your hero stats. type stats to open hero stats: ").strip().lower()
debug_print_state(stats=stats)
#Checks if user typed 'stats' correctly on the first try.
if stats=="stats":
    #Calculate total sneak stat (weapon sneak + armor sneak).
    skt = sk1 +sk2
    #Calculate total fight stat (weapon fight + armor fight).
    ftt = ft1 +ft2
    #Calculate total run stat (weapon run + armor run).
    rnt = rn1 +rn2
    debug_print_state(skt=skt, ftt=ftt, rnt=rnt)
    #Define X-axis category labels for the chart.
    categories = ["Sneak", "Fight", "Run"]
    #Define Y-axis values corresponding to the categories.
    values =  [skt, ftt, rnt]
    #Define custom bar colors for each stat.
    color=["darkslateblue", "firebrick", "limegreen"]
    #Create a bar chart with the categories, values, and colors.
    plt.bar(categories, values, color=color)
    #Label the X-axis as "Stats".
    plt.xlabel("Stats")
    #Label the Y-axis as "Modifier".
    plt.ylabel("Modifier")
    #Set the title of the chart to "Hero Stats"
    plt.title("Hero Stats")
    #Draw a dashed horizontal reference line at y=10.
    plt.axhline(y=difficulty_class, color="black", linestyle="--", label="Monster difficulty")
    #Draw a solid horizontal line at y=0 for the baseline.
    plt.axhline(y=0, color="black")
    #Display the chart legend.
    plt.legend()
    #Render and display the plot window.
    plt.show()
    #Print adventure start message.
    print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')
#Executes if user failed to type 'stats' on first try.
else:
    #Give a hint to view stats.
    print("are you sure? It could save your life. *hint hint wink wink*")
    #Second chance input.
    stats = input("Before you go lets take a quick look at your hero stats. type stats to open hero stats: ").strip().lower()
    debug_print_state(stats=stats)
    #Check second attempt.
    if stats == "stats":
        #Calculate total fight, sneak, run.
        skt = sk1 +sk2
        ftt = ft1 +ft2
        rnt = rn1 +rn2
        debug_print_state(skt=skt, ftt=ftt, rnt=rnt)
        #Define X-axis category labels for the chart.
        categories = ["Sneak", "Fight", "Run"]
        #Define Y-axis values corresponding to the categories.
        values =  [skt, ftt, rnt]
        #Define custom bar colors for each stat.
        color=["darkslateblue", "firebrick", "limegreen"]
        #Create a bar chart with the categories, values, and colors.
        plt.bar(categories, values, color=color)
        #Label the X-axis as "Stats".
        plt.xlabel("Stats")
        #Label the Y-axis as "Modifier".
        plt.ylabel("Modifier")
        #Set the title of the chart to "Hero Stats"
        plt.title("Hero Stats")
        #Draw a dashed horizontal reference line at y=10.
        plt.axhline(y=difficulty_class, color="black", linestyle="--", label="Monster difficulty")
        #Draw a solid horizontal line at y=0 for the baseline.
        plt.axhline(y=0, color="black")
        #Display the chart legend.
        plt.legend()
        #Render and display the plot window.
        plt.show()
        #Print adventure start message.
        print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')
    #Fall back if all attempts fail.
    else:
        #Prints a sarcastic remark.
        print("Wow look at those stats!")
        #Calculate total sneak, fight, run.
        skt = sk1 +sk2
        ftt = ft1 +ft2
        rnt = rn1 +rn2
        debug_print_state(skt=skt, ftt=ftt, rnt=rnt)
        #Define X-axis category labels for the chart.
        categories = ["Sneak", "Fight", "Run"]
        #Define Y-axis values corresponding to the categories.
        values =  [skt, ftt, rnt]
        #Define custom bar colors for each stat.
        color=["darkslateblue", "firebrick", "limegreen"]
        #Create a bar chart with the categories, values, and colors.
        plt.bar(categories, values, color=color)
        #Label the X-axis as "Stats".
        plt.xlabel("Stats")
        #Label the Y-axis as "Modifier".
        plt.ylabel("Modifier")
        #Set the title of the chart to "Hero Stats"
        plt.title("Hero Stats")
        #Draw a dashed horizontal reference line at y=10.
        plt.axhline(y=difficulty_class, color="black", linestyle="--", label="Monster difficulty")
        #Draw a solid horizontal line at y=0 for the baseline.
        plt.axhline(y=0, color="black")
        #Display the chart legend.
        plt.legend()
        #Render and display the plot window.
        plt.show()
        #Print adventure start message.
        print(f'With you {weapon} and {armor} It’s time to set forth on an adventure; kill the monster and take the treaasure. Soon they will tell stories about {name} the... Soon to be titled!')

############################################################################################################################################
#Print narrative text.
print("*you recieve a letter while on your travels*")
#Prints the letter you receive.
print("I hope you are doing well on your quest dear adventure. My old mind is getting the best of me, how long has it been old friend?")
#Asks user for travel duration.
time = input("How long has it been: ")
debug_print_state(time=time)
#Prints narrative text.
print("*you send your letter and return to the path of glory*")
#Prints arrival and monster encounter message.
print(f' After {time} of treacherous travel you finally get to the treasure cave. As you enter, you spot a monster! Oh no, you spotted a {monster}!')

############################################################################################################################################

#Imports the numpy library for numerical operations and random number generation. 
import numpy as np

#################################################################

#Titles as lists to randomize from
# t = title
# w = win
#Sneak win titles.
tsw = ["the nonchalant", "the Unseen", "the nimble"]
#Fight win titles.
tfw = ["the Brave", "the Mighty", "the Slayer"]
#Run win titles.
trw = ["the living another day", "the retired", "the cautious"]

# t = title
# f = fail
#Sneak fail titles.
tsf = ["the not so subtle", "the lead foot", "the loud pop"]
#Fight fail titles.
tff = ["the super dead", "the knife at a gunfight", "the food"]
#Run fail titles.
trf = ["the Coward", "the Slow", "the Oops Too Late"]

############################################################################
#Define a custom dice class for rolling numbers in the encounter phase
class dice:
    #initilizes: runs when new dice object is created
    def __init__(self):
        #outcome variables store results of each roll
        self.outcome=0
    #method for fair die roll
    def roll(self):
        #gen random int1-21
        #Generates a random integer between 1 and 20 using numpy.
        self.outcome=np.random.randint(1,21)
        #Return a rolled outcome.
        return self.outcome
#Initialize base result tracker.        
result = 0
#Initialize total check value tracker.
value = 0 

#Alert message.
print(f'QUICK! THE {monster} AND ONLY THING THAT STANDS BETWEEN YOU AND THE TREASURE HAS NOTICED YOU!')
#Prints the diffuculty class to help player.
print(f"Difficulty class: {difficulty_class}")
#Options prompt.
print("What will you do, Hero?! SNEAK around the monster by nightfall? FIGHT the monster with your weapon? or RUN away to safety")
#Gets players chosen actions. 
act = input("type SNEAK, FIGHT, or RUN: ").strip().lower()
debug_print_state(act=act)

#############################################################
#Checks if player chose to sneak.
if act == "sneak" :
     #Narrative text.
    print(f'You wait for the {monster} to fall asleep before sneaking against the cave walls as you make your way towards the treasure.')
    #Creates a dice object for sneaking.
    sk_die = dice()
    #Rolls the die and adds it to the result.
    result += sk_die.roll()
    #Adds die roll and sneak stats together.
    value += (result + skt)
    debug_print_state(roll_result=sk_die.outcome, result=result, value=value, sneak_total=skt)
    print(f"Roll calculation: {result} + sneak stat {skt} = {value} (difficulty: {difficulty_class})")
    #Check if total check value meets or exceeds the monster's difficulty class
    if value >= difficulty_class:
        #Picks a winning sneak title
        title = random.choice(list(tsw)) 
         #Success story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} did sneak, as the {monster} did sleep. And {name} {title} left with the treasure without a peep!')
    #Execute if roll/stat check fails 
    else:
        #Picks random failed sneak title.
        title = random.choice(list(tsf))
        #Failure story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} did sneak, as the {monster} caught on. And {name} {title} is long gone!')
#Checks if player chose to fight.
elif act == "fight":
    #Narrative text.
    print(f'You charge into action with you {weapon} drawn and {armor} secured.')
    #Creates a dice object for fighting.
    ft_die = dice()	
    #Roll the die and add to result.
    result += ft_die.roll() 
    #Calculate the total success value (die roll + total fight stat)
    value += (result + ftt)
    debug_print_state(roll_result=ft_die.outcome, result=result, value=value, fight_total=ftt)    
    print(f"Roll calculation: {result} + fight stat {ftt} = {value} (difficulty: {difficulty_class})")
    #Check if total check value meets or exceeds the monster's difficulty class
    if value >= difficulty_class:
        #Pick a random successful fight title. 
        title = random.choice(list(tfw)) 
        #Success story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} lunged and fought! As the {monster} head is servered on a tray, we all cheer and say. Oh {name} {title} was there to slay!')
    #Executes if checks fail.    
    else:
         #Pick a random failed fight title.
        title = random.choice(list(tff))
        #Failure story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} lunged and fought! As the {monster} attacked, the hero did say! Oh no, {name} {title} should have covered their back!')
#Check if player chose to run.        
elif act == "run":
    #Narrative text.
    print(f'You turn on you heals, seath your {weapon} and run as fast as you can away from the {monster}.')
    #Create a dice object for running.
    rn_die = dice()	
    #Roll the die and add to results.
    result += rn_die.roll()
    #Calculate total success value (die roll + total run stat).
    value += (result + rnt)
    debug_print_state(roll_result=rn_die.outcome, result=result, value=value, run_total=rnt)
    print(f"Roll calculation: {result} + run stat {rnt} = {value} (difficulty: {difficulty_class})")
    #Check if total check value meets or exceeds the monster's difficulty class
    if value >= difficulty_class:
        #Picks a random successfuk run title.
        title = random.choice(list(trw))
        #Success story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} turned around and ran! As the {monster} gave up, the Hero did say! Oh my {name} {title} is so lucky to have run away!')
    #Executes if check fails.    
    else: 
        #Pick a random failed run title.
        title = random.choice(list(trf)) 
        #Failure story output.
        print(f'There once was a hero named {name} {title} who came riding to glory from {home}. And the Hero did strut in their {armor} and brandish a {weapon} as the {monster} said I think it is high time that you lie down and bleed. So {name} {title} turned around and ran! As the {monster} caught up the hero did say! Oh my {name} {title} will seen!') 
#Execute if player types an invalid action.         
else:
    #Default penalty output for invalid choice.
    print(f'You freeze in fear as the {monster} eyes you down hungery for wimpy hero.') 
#########################################################################
#Print end of game message.
print("THE END") 
############################################################################
