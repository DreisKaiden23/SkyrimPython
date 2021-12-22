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

choice2 = int(input("Bob ross walks into the room, he wants his money back that you stole 20 years prior. (1) Attempt to fight Bob Ross (very hard), (2) Reason with Bob Ross, (3) Intimidate Bob Ross with your coolness :sunglasses:\n1/2/3\n"))

if choice1 == 1:
    roll2 = random.randrange(0, strength)
    if roll2 >= 50:
        print("You win the duel against bob ross! He forgets everything about the $5 you stole from him 20 years ago.")
    else:
        print ("Bob Ross dumpsters you in this fight, he is simply too powerful. I told you this was very hard!\nGAME OVER\n")
        exit()

if choice1 == 2:
    roll2 = random.randrange(0, intellect)
    if roll2 >= 20:
        print("Bob ross is a very reasonable person, he realizes that it is dumb to get in an argument over $5 from 20 years ago!")
    else:
        print ("Bob Ross does not want to reason HE WANTS HIS MONEY BACK!!! He paints your whole face out of extinction.\nGAME OVER\n")
        exit()

if choice1 == 3:
    roll2 = random.randrange(0, coolness)
    if roll2 >= 30:
        print("Bob Ross is scared of you, you are way too cool for him. He bows down to your glory")
    else:
        print ("Bob Ross is way cooler than you. It was a mistake to think that you could EVER be cooler than Bob Ross! How foolish!\nGAME OVER\n")
        exit()