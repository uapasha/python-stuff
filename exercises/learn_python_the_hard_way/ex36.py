from sys import exit
from random import randint
from random import choice
import time
import webbrowser

LIST_OF_POWERS = ["throwing lightsaber", "dark lighting", "hight jump", "healing", "quick run"]

class Jedi:
    def __init__ (self,name, skills, powers, side_dark, side_light, items):
        self.name = name
        self.skills = skills
        self.powers = powers
        self.side_dark = side_dark
        self.side_light = side_light
        self.items = items
    def print_jedi (self):
        print "Name: %s \nSkils: %d \nPowers: %s \
                \nDark\Light: %d\%d \nItems: %s " % (self.name, self.skills,
                self.powers, self.side_dark, self.side_light, self.items)

def play():
    print "Hello!"
    print "This is a game where you can become a real Jedi or Dart Lord!"
    name = raw_input( "Lets give you a birth..\nWhat's your name? \n > ")
    jedi = jedi_born(name)
    
    time.sleep(4)
    for i in range(1000):
        print ">>>>>>>>>>>>>>>>"
        print "Here is your young padavan: "
        jedi.print_jedi()
        time.sleep(3)
        print ">>>>>>>>>>>>>>>>"
        print "%s, what you want to do now? \n- Train (train), \n- Gain experience (exp)\
\n- Look for your special lightsaber (look) \nor \n- Take an examination (exam)" % jedi.name
        choice = raw_input (" > ")

        if "train" in choice:
            train(jedi)
        elif "exp" in choice:
            make_decision(jedi)
        elif "look" in choice:
            find_lightsaber(jedi)
        elif "exam" in choice:
            pass_exam(jedi)
        else:
            print"Wrong choice"   
            
        
        
        

def check_luck(influence):
    """ dices some event. input can be "max", "low" or "norm" """
    if influence == "norm":
        influence = 1
    elif influence == "max":
        influence = 1.3
    elif influence == "low":
        influence = 0.3
    else:
        print "wrong choice of influence!"
        return None
    result = influence*randint(0,71)
    if result > 100:
        return 100
    else:
        return result

def jedi_born(name):
    """ don't forget to provide name! """ 
    jedi = Jedi(name, check_luck("low"), [], check_luck("low"), check_luck("low"), [])
    return jedi

def train(jedi):
    print "Its time to gain some skills and power, %s" % jedi.name
    choice = raw_input ("What do you want to train? skills or powers?\n > ")

    if choice == "skills":
        train_skils(jedi)
    elif choice == "powers":
        train_powers(jedi)
    else:
        print "Wrong!"
        train(jedi)
            
def train_skils(jedi):
    print "Your skills are: %d" % jedi.skills
    print "training skills..."
    print "wzhwhzhwhhwhz.."
    jedi.skills = jedi.skills + check_luck("low")
    print "%s, now your skills are much higher: %d!!" % (jedi.name, jedi.skills)
    time.sleep(3)
def train_powers(jedi):
    
    print "Your powers are: %s" % jedi.powers
    print "gaining new powers..."
    print "wzhwhzhwhhwhz.."
    new_power = choice(LIST_OF_POWERS)
    if new_power not in jedi.powers:
        print "You'we got new power!it is - %s" % new_power
        jedi.powers.append(new_power)
        print "%s, now your powers are: %s!!" % (jedi.name, jedi.powers)
        time.sleep(3)
    else:
        print "Sorry, %s, no new power today.." % jedi.name
        time.sleep(3)
    

def make_decision(jedi):
    print "Its time to choose your side, %s, : Dark or Light!" % jedi.name
    print "Now you're Dark\Light: %d\%d" % (jedi.side_dark, jedi.side_light)
    print "Make decision: light or dark??"
    dec = raw_input(">")

    if dec == "light":
        jedi.side_light = jedi.side_light + check_luck("norm")
        print "Now you're Dark\Light: %d\%d" % (jedi.side_dark, jedi.side_light)
        time.sleep(3)

        if jedi.side_light > jedi.side_dark:
            print "You're holy jedi!"
        elif jedi.side_light < jedi.side_dark:
            print "You're Dart Lord!"
        else:
            print "You're nothing!"
    elif dec == "dark":
        jedi.side_dark = jedi.side_dark + check_luck("norm")
        print "Now you're Dark\Light: %d\%d" % (jedi.side_dark, jedi.side_light)
        time.sleep(3)
        if jedi.side_light > jedi.side_dark:
            print "You're holy jedi!"
            time.sleep(3)
        elif jedi.side_light < jedi.side_dark:
            print "You're Dart Lord!"
            time.sleep(3)
        else:
            print "You're nothing!"
            time.sleep(3)
    else:
        print "Wrong!"
        make_decision(jedi)

def find_lightsaber(jedi):
    print "Its time to find your own lightsaber, %s!" % jedi.name
    for i in range (1, 4):
        
        print "Looookiinnnng...."
        time.sleep(2)
    success = check_luck("norm")
    if success > 30:
        print("..............")
        print "Yeaahh!! You made it!\nYou now have lightsaber, %s!" %jedi.name
        jedi.items.append("LIGHTSABER")
        time.sleep(3)
        jedi.print_jedi()
    else:
        print "Sorry! maybe next time!"
        time.sleep(3)
        
def pass_exam(jedi):
    print"...passing exam..."
    print "You are: "
    jedi.print_jedi()
    time.sleep(4)
    req = 0
    if jedi.skills >= 70:
        req += 1

    if len(jedi.powers)>2:
        req +=1

    if jedi.side_dark >= 60 or jedi.side_light > 60:
        req +=1

    if "LIGHTSABER" in jedi.items:
        req +=1


    if req > 2:
         print "Congrats! You win!!"
         print "TAda!!!"
         time.sleep(3)
         webbrowser.open("http://usercontent1.hubimg.com/8630852_f520.jpg")
         exit(0)
    else:
        print "No! You aren't ready! Train, gain skills and more!"
        time.sleep(3)

#Luke = jedi_born("Luke")
#pass_exam(Luke)

#Luke.print_jedi()
#train(Luke)
#make_decision(Luke)
#find_lightsaber(Luke)
play()
