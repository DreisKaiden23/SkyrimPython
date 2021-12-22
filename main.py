# 5 skills 1-100
# user needs to make 3 decisions in a row
# the outcomes are based on skill levels
# 250 skill points
# 3 choices per event
# 5 events

# setting skill points
import random
print("Hello adventurer!!! Your name is Steve Jobs, and you have 5 skills to choose from! insert a value 0-100 for each skill!")
programming = int(input("What do you want your programming stat to be?"))
strength = int(input("What do you want your strength stat to be?"))
intellect = int(input("What do you want your intellect stat to be?"))
reflex = int(input("What do you want your reflexes stat to be?"))
coolness = int(input("What do you want your coolness stat to be?"))
skillPoints = int(250 - programming - strength - intellect - reflex - coolness)
if skillPoints >> 250:
    print("That is too many skill points! How dare you betray me and try to fool me!")
    exit()
else:
    choice1 = int(input("Well done you haven't cheated... yet... As you are steve jobs, you see a computer. Would you like to (1) Impress the computer, (2) Threaten the computer, or (3) Turn the computer on\n1/2/3\n"))
# adventure starts
def roll(a):
    return random.randrange(0,int(a))
if choice1 == 1:
    roll = random.randrange(0, coolness)
    if roll >= 40:
        print("The computer feels intimidated by your skills! The computer turns itself on out of fear of your coolness")
    else:
        print ("You fail to impress the computer. Did you really expect that to work?\nGAME OVER\n")
        exit()

if choice1 == 2:
    roll = random.randrange(0, strength)
    if roll >= 40:
        print("The computer feels intimidated by your skills! The computer turns itself on out of fear of your coolness")
    else:
        print ("You fail to scare the computer into submission. Did you really expect that to work?\nGAME OVER\n")
        exit()

if choice1 == 3:
    roll = random.randrange(0, reflex)
    if roll >= 1:
        print("You turned on the computer. Easy peasy lemon squeezy!!!11!!!!")
    else:
        print ("How did you fail to turn on a computer! I'm impressed. The game has to stop, but you must have put 0 in as your reflex! I'm impressed!\nGAME OVER\n")
        exit()

choice2 = int(input(""))
    