# 5 skills 1-100
# user needs to make 3 decisions in a row
# the outcomes are based on skill levels
# 250 skill points
# 3 choices per event
# 5 events

# setting skill points
import random
print("Hello adventurer!!! Your name is Steve Jobs, and you have 5 skills to choose from! insert a value 0-100 for each skill!")
skillPoints = 250
programming = int(input("What do you want your programming stat to be?"))
if programming > 100:
    print("That is too many points! How dare you try and fool me Osowski!")
    exit()
elif programming < 0:
    print("You can't have below 0 points in a category! How dare you try to fool me osowski!")
    exit()
print("you have " + str(skillPoints - programming) + " skill points remaining.")
strength = int(input("What do you want your strength stat to be?"))
if strength > 100:
    print("That is too many points! How dare you try and fool me Osowski!")
    exit()
elif strength < 0:
    print("You can't have below 0 points in a category! How dare you try to fool me osowski!")
    exit()
print("you have " + str(skillPoints - programming - strength) + " skill points remaining.")
intellect = int(input("What do you want your intellect stat to be?"))
if intellect > 100:
    print("That is too many points! How dare you try and fool me Osowski!")
    exit()
elif intellect < 0:
    print("You can't have below 0 points in a category! How dare you try to fool me osowski!")
    exit()
print("you have " + str(skillPoints - programming - strength - intellect) + " skill points remaining.")
reflex = int(input("What do you want your reflexes stat to be?"))
if reflex > 100:
    print("That is too many points! How dare you try and fool me Osowski!")
    exit()
elif reflex < 0:
    print("You can't have below 0 points in a category! How dare you try to fool me osowski!")
    exit()
print("you have " + str(skillPoints - programming - strength - intellect - reflex) + " skill points remaining.")
coolness = int(input("What do you want your coolness stat to be?"))
if coolness > 100:
    print("That is too many points! How dare you try and fool me Osowski!")
    exit()
elif coolness < 0:
    print("You can't have below 0 points in a category! How dare you try to fool me osowski!")
    exit()
skillPointsActual = int(250 - programming - strength - intellect - reflex - coolness)
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
# Choice 2
choice2 = int(input("Bob ross walks into the room, he wants his money back that you stole 20 years prior. (1) Attempt to fight Bob Ross (very hard), (2) Reason with Bob Ross, (3) Intimidate Bob Ross with your coolness :sunglasses:\n1/2/3\n"))

if choice2 == 1:
    roll2 = random.randrange(0, strength)
    if roll2 >= 50:
        print("You win the duel against bob ross! He forgets everything about the $5 you stole from him 20 years ago.")
    else:
        print ("Bob Ross dumpsters you in this fight, he is simply too powerful. I told you this was very hard!\nGAME OVER\n")
        exit()

if choice2 == 2:
    roll2 = random.randrange(0, intellect)
    if roll2 >= 20:
        print("Bob ross is a very reasonable person, he realizes that it is dumb to get in an argument over $5 from 20 years ago!")
    else:
        print ("Bob Ross does not want to reason HE WANTS HIS MONEY BACK!!! He paints your whole face into extinction.\nGAME OVER\n")
        exit()

if choice2 == 3:
    roll2 = random.randrange(0, coolness)
    if roll2 >= 30:
        print("Bob Ross is scared of you, you are way too cool for him. He bows down to your glory")
    else:
        print ("Bob Ross is way cooler than you. It was a mistake to think that you could EVER be cooler than Bob Ross! How foolish!\nGAME OVER\n")
        exit()
# Choice 3
choice3 = int(input("You come across 3 doors, one door has a big apple on it, which looks very cool AND awesome, the 2nd one has a big question mark on it, and one is guarded by Bill Gates himself but he has a top hat on, he looks very scary and hard to fight.\ndo you go through (1) Apple, (2) Question Mark, or (3) Bill Gates \n1/2/3\n"))
if choice3 == 1:
    roll3 = random.randrange(0, coolness)
    if roll3 >= 30:
        print("The big apple door opens with ease, this was probably the most boring option though :(")
    else:
        print ("The apple door was just too scary for you. \nGAME OVER\n")
        exit()

if choice3 == 2:
    roll3 = random.randrange(0, intellect)
    if roll3 >= 10:
        print("The question mark door ends up just being a regular door. It was very easy to open.")
    else:
        print ("While the door was just a door with a question mark on it, you still failed to open it. Thats pretty impressive!\nGAME OVER\n")
        exit()

if choice3 == 3:
    roll3 = random.randrange(0, strength)
    if roll3 >= 80:
        print("Bill Gates is a very strong opponent, but you end up winning! Bill Gates has been defeated.")
    else:
        print ("Bill Gates is much too powerful for you. Why did you ever think you would beat him?\nGAME OVER\n")
        exit()
# Choice 4
choice4 = int(input("Finally, you get to create your company. There are many names to choose from. Do you choose (1) Apple, (2) Banana, or (3) Grape\n1/2/3\n"))
if choice4 == 1:
    roll4 = random.randrange(0, intellect)
    if roll4 >= 10:
        print("You have successfully named your company Apple")
        companyName = str("Apple")
    else:
        print ("Just the thought of naming a company was too scary. Maybe try to put some more into intellect next time!\nGAME OVER\n")
        exit()

if choice4 == 2:
    roll4 = random.randrange(0, intellect)
    if roll4 >= 10:
        print("You have successfully named your company Banana")
        companyName = str("Banana")
    else:
        print ("Just the thought of naming a company was too scary. Maybe try to put some more into intellect next time!\nGAME OVER\n")
        exit()

if choice4 == 3:
    roll4 = random.randrange(0, intellect)
    if roll4 >= 10:
        print("You have successfully named your company Grape")
        companyName = str("Grape")
    else:
        print ("Just the thought of naming a company was too scary. Maybe try to put some more into intellect next time!\nGAME OVER\n")
        exit()
# Choice 5, FINAL!
choice5 = int(input("With you and your unstoppable company, " + companyName + " you decide to trancend to another level. Do you make " + companyName + " the equivilent of (1) Activision Blizzard, (2) Google, or (3) Kwik Trip\n1/2/3\n"))
if choice5 == 1:
    roll5 = random.randrange(0, coolness + reflex)
    if roll5 >= 10:
        print("You have successfully  " + companyName + " the equivilent of ActiBlizz. Thats not a good thing. \nBAD ENDING\n")
        exit()
    else:
        print ("Even you couldn't make Activision Blizzard, a company well known for its internal problems. \nGAME OVER\n")
        exit()

if choice5 == 2:
    roll5 = random.randrange(0, programming + strength)
    if roll5 >= 50:
        print("You have successfully made " + companyName + " the equivilent of Google. This isn't bad, but isn't great either.\nMEDIOCRE ENDING\n")
    else:
        print ("You went for the middle option but failed. Maybe try making ActiBlizz instead? wait, nevermind. Don't do that...\nGAME OVER\n")
        exit()

if choice5 == 3:
    roll5 = random.randrange(0, intellect + programming)
    if roll5 >= 100:
        print("You have successfully made " + companyName + " the equivilent of Kwik Trip. " + companyName + " becomes the new standard of workers rights. You should be proud!\nGOOD ENDING\n")
    else:
        print ("You failed, but thats ok! Kwik trip is a very powerful company, trying to make " + companyName + " a company of that level is difficult.\nGAME OVER\n")
        exit()
