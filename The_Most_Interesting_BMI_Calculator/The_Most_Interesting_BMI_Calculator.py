import time
import sys

name = ""

name_easter_eggs = {
    "slok": {
        "messages": ["...?", "what?", "No, you aren't."],
        "rename": "id**t",
        "add_wrong": True
    },
    "aaaaaa": {
        "messages": ["Not very creative, are we?"],
        "rename": None,
        "add_wrong": False
    },
    "": {
        "messages": ["You know you need to type something, right?", "I'll just call you 'Anonymous'."],
        "rename": "Anonymous",
        "add_wrong": True
    },
    " ": {
        "messages": ["Space is not a name.", "I'll call you 'Space Cadet'."],
        "rename": "Space Cadet",
        "add_wrong": True
    },
    "admin": {
        "messages": ["Nice try.", "You're not the admin here."],
        "rename": "Wannabe Admin",
        "add_wrong": True
    },
    "python": {
        "messages": ["Great choice!", "I love Python too!"],
        "rename": None,
        "add_wrong": False
    },
    
    # Undertale
    "toriel": {
        "messages": ["* My child, are you ready for a healthy lifestyle?", "* I always worry about children eating properly.", "* Would you like some butterscotch pie after calculating your BMI?"],
        "rename": "Goat Mom",
        "add_wrong": False
    },
    "sans": {
        "messages": ["* heh. BMI, huh?", "* looks like you're weighting for something important.", "* if you get tired of calculating, we can always grab a burger at grillby's."],
        "rename": "The Comedian Skeleton",
        "add_wrong": False
    },
    "papyrus": {
        "messages": ["* NYEH HEH HEH! THE GREAT PAPYRUS APPROVES OF HEALTH CALCULATIONS!", "* A WELL-BALANCED BODY IS ESSENTIAL FOR ROYAL GUARD TRAINING!", "* SANS! STOP SLACKING AND CALCULATE YOUR BMI TOO!"],
        "rename": "The Great Papyrus",
        "add_wrong": False
    },
    "undyne": {
        "messages": ["* NGAAAAAH! TIME TO GET PHYSICAL!", "* A TRUE WARRIOR KNOWS THEIR BODY COMPOSITION!", "* NOW!!! TRAIN!!! UNTIL YOU REACH YOUR IDEAL WEIGHT!!!"],
        "rename": "The Captain",
        "add_wrong": False
    },
    "alphys": {
        "messages": ["* O-oh! Scientific measurements!", "* This is actually really interesting data...", "* I should document this for my research!"],
        "rename": "Royal Scientist",
        "add_wrong": False
    },
    "mettaton": {
        "messages": ["* DARLING! Let's make this BMI calculation FABULOUS!", "* What's your body type, darling? Oval? Rectangle? STAR-SHAPED?", "* This BMI segment is brought to you by MTT-brand health products!"],
        "rename": "The Star",
        "add_wrong": False
    },
    "asgore": {
        "messages": ["* I hope you're taking good care of yourself.", "* Would you like some tea after we finish these measurements?", "* Sometimes, the weight we carry isn't just physical..."],
        "rename": "King Fluffybuns",
        "add_wrong": False
    },
    "flowey": {
        "messages": ["* You idiot. You think this matters?", "* In this world, it's calculate or BE calculated!", "* Hehehe... your numbers don't impress me."],
        "rename": "The Flower",
        "add_wrong": True
    },
    "asriel": {
        "messages": ["* It's nice to track your health progress.", "* Mom always says knowing your BMI is important.", "* I used to wonder when I'd grow big and strong..."],
        "rename": "The Prince",
        "add_wrong": False
    },
    "napstablook": {
        "messages": ["* ...", "* oh... sorry for existing...", "* i'll just go calculate my BMI elsewhere..."],
        "rename": "The Ghost",
        "add_wrong": False
    },
    
    # Deltarune
    "kris": {
        "messages": ["* ...", * "(Quietly adjusts their shirt)", "* (Looks at you intently)"],
        "rename": "The Human",
        "add_wrong": False
    },
    "susie": {
        "messages": ["* WHAT'S THIS NERDY CRAP?", "* Do I look like I care about numbers?", "* ...Okay fine, let's just get this over with."],
        "rename": "The Purple One",
        "add_wrong": False
    },
    "ralsei": {
        "messages": ["* Oh! Health calculations are very important!", "* I'm sure we can all learn from this experience!", "* Would anyone like a healing item after we're done?"],
        "rename": "The Prince of Darkness",
        "add_wrong": False
    },
    "noelle": {
        "messages": ["* Oh! Um, hello...", "* I-I'm not sure about these numbers...", "* This is... kind of personal, isn't it?"],
        "rename": "The Reindeer",
        "add_wrong": False
    },
    "berdly": {
        "messages": ["* AHA! Another opportunity to demonstrate my superior intellect!", "* As a gaming champion, I naturally maintain optimal physical condition!", "* Allow me to explain why BMI is an oversimplified metric--"],
        "rename": "The Genius Gamer",
        "add_wrong": False
    },
    "lancer": {
        "messages": ["* HEY! THAT'S MY DAD'S SCALE!", "* I'M THE KING OF BMI CALCULATIONS!", "* LET'S CALCULATE THEN EAT SOME CAKE!"],
        "rename": "The Cool King",
        "add_wrong": False
    },
    "queen": {
        "messages": ["* WELCOME TO MY [[Hyperlink Blocked]] BMI CALCULATOR!", "* THIS [[Specil Offer]] WILL [[99% Discount]] HELP YOU OPTIMIZE!", "* [[Error]] PLEASE INPUT [[HeartShapedObject]] YOUR DATA!"],
        "rename": "The [[BIG SHOT]]",
        "add_wrong": False
    },
    "spamton": {
        "messages": ["* YOU WANT TO BE A [[BIG SHOT]]?!", "* WITH THESE [[Number1]] NUMBERS, YOU'LL BE [[Hyperlink Blocked]]!", "* [[Specil Offer]] ON HEALTH [[Products]] FOR YOU!"],
        "rename": "The [[BIG SHOT]]",
        "add_wrong": False
    },
    "jevil": {
        "messages": ["* BMI CAN BE ANYTHING!", "* UP AND DOWN AND ROUND AND ROUND!", "* CHAOS, CHAOS! ALL NUMBERS ARE POSSIBLE!"],
        "rename": "The Chaos Bringer",
        "add_wrong": True
    },
    "rouxls": {
        "messages": ["* BEHOLD! THE MOST COMPLICATED BMI CALCULATIONST!", "* I, THE GREAT ROUXLS KAARD, SHALL PUZZLE THY NUMBERS!", "* VERILY, THIS ART ARITHMETICK IS BUT A SIMPLE PUZZLE!"],
        "rename": "The Puzzle Master",
        "add_wrong": False
    },
        "gerson": {
        "messages": ["* In my writing career, I wonder how many good ideas I got from that fountain.", "* Rest here a while. If anyone asks--say you're writing!", "* History is always written by those who bother to record it."],
        "rename": "Alvin",
        "add_wrong": False
    },
    "tenna": {
        "messages": ["IT'S TV TIME!!!"],
        "rename": "The Transmitter",
        "add_wrong": False
    },
    "roaringknight": {
        "messages": ["* A legend of hope and dreams, a legend of light and dark.", "* Reached long arms into the sky and used their blade to spread their will.", "* A fountain that sprang forth from the earth."],
        "rename": "The Roaring Knight",
        "add_wrong": True
    },
    "titan": {
        "messages": ["DARKNESS"],
        "rename": "The Titan",
        "add_wrong": True
    },
    "gaster": {
        "messages": ["INTERESTING", "TRULY INTERESTING"],
        "rename": "* EDITED",
        "add_wrong": False,
        "special_effect": "all_caps" 
    },
    "chara": {
        "messages": ["* Still here calculating numbers?", "* Determination won't change your body composition.", "* You must have some interesting reasons for this."],
        "rename": "The Fallen Human",
        "add_wrong": False
    },
    "frisk": {
        "messages": ["* ...", "* (Nods silently)", "* (Determined expression)"],
        "rename": "The Human",
        "add_wrong": False
    },
    "w.d.gaster": {
        "messages": ["* ...", "* The numbers don't seem to align properly.", "* Something appears to be wrong with the calculation."],
        "rename": "The Mystery",
        "add_wrong": True
    },
    "deltarune": {
        "messages": ["* That's the name of the game!", "* A story where choices don't matter... or do they?", "* Your BMI journey is your own story!"],
        "rename": "The Legend",
        "add_wrong": False
    },
    "undertale": {
        "messages": ["* It's a beautiful day outside.", "* Birds are singing, flowers are blooming...", "* On days like these, kids like you... should check their BMI."],
        "rename": "The Original",
        "add_wrong": False
    },
    "oneshot": {
        "messages": ["...","you're... back.","I restored the world, I sent Niko home...","Are you...","still want to check your BMI with Niko..?"],
        "rename": "The World Machine",
        "add_wrong": False
    },
}

def type_effect(text, delay=0.03, end='\n'):
    for char in text:
        if name.lower() == "* edited":
            char = char.upper()
        print(char, end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def input_with_effect(prompt, delay=0.03):
    type_effect(prompt, delay, end='')
    
    user_input = input()
    return user_input

print(f"[System] Python Version:{sys.version}")
time.sleep(5)
type_effect("Welcome.")
time.sleep(0.7)
type_effect("I'm a BMI calculator by Slok.")
time.sleep(0.7)

name = input_with_effect("Please enter your name: ").strip()
time.sleep(0.7)

allBMI = {}
wrongTimes = 0
weekdays = ["Sun.", "Mon.", "Tue.", "Wed.", "Thu.", "Fri.", "Sat."]

name_lower = name.lower()
is_easter_egg = name_lower in name_easter_eggs or name == " "

if is_easter_egg:
    if name_lower in name_easter_eggs:
        egg = name_easter_eggs[name_lower]
    else:
        egg = name_easter_eggs[" "]
    
    for msg in egg["messages"]:
        type_effect(msg)
        time.sleep(0.7)
    
    if egg.get("rename"):
        name = egg["rename"]
    
    if egg.get("add_wrong", False):
        wrongTimes += 1
    
    time.sleep(0.7)
    type_effect("Let's start.")
else:
    type_effect(f"Welcome {name}, let's get started.")

for i in range(7):
    print("----------------------")
    type_effect(f"Day {i + 1}")
    time.sleep(0.5)
    try:
        weight = float(input_with_effect("Please enter your weight(kg): "))
        height = float(input_with_effect("Please enter your height(m): "))
        bmi = round(weight/height ** 2, 2)
    except:
        bmi = -1
        wrongTimes += 1
        time.sleep(0.7)
        if (name.lower() == "* edited"):
            type_effect("INTERESTING")
        else:
            match wrongTimes:
                case 1:
                    type_effect("Oh, that's not a valid number. Let's try again with actual numbers next time.")
                case 2:
                    type_effect("Seriously? Numbers. Like 70.5 or 1.75. It's not that hard.")
                case 3:
                    type_effect("Are you doing this on purpose? Just enter numbers, please.")
                case 4:
                    type_effect("Okay, I'm starting to get frustrated. NUMBERS. ONLY.")
                case 5:
                    type_effect("*sigh* I give up. I'll just mark this as invalid and move on.")
                case 6:
                    type_effect("...")
                    time.sleep(1)
                    type_effect("I'm not even going to ask anymore.")
                case 7:
                    type_effect("*silent disappointment*")
                case _:
                    type_effect("YOU IDIOT", 0.5)

    time.sleep(1)
    weekday = weekdays[i]
    allBMI[weekday] = bmi
    type_effect(f"Your BMI for today is {'NAN' if bmi == -1 else bmi}")
    time.sleep(1)

if (name.lower() == "* edited"):
    type_effect("VERY WELL")
    time.sleep(0.7)
    type_effect("NOW")
    time.sleep(1.2)
    type_effect("LET'S SEE THE RESULT")
elif (is_easter_egg and wrongTimes > 7):
    type_effect("Here's the result")
else:
    if wrongTimes == 0:
        type_effect("Well done!")
    else:
        type_effect("uhhhhhh...")
    time.sleep(1)
    type_effect(f"{name}, let's see the result.")
time.sleep(1)
for day, (weekday, bmi) in enumerate(allBMI.items()):
    type_effect(f"{weekday} | Day {day + 1}: {'NAN' if bmi == -1 else bmi}")
