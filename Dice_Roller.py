import random
print("Welcome to the Best Dice Roller Ever!")
dice = ["d4", "d20", "d6", "d8", "d10", "d12",]
def d20():
    roll = random.randint(1,20)
    if roll == 1:
        print("Critcal Fail!" ) and print(roll)
        return roll
    elif roll == 20:
        print("Critical Success!") and print(roll)
        return roll
    else:
        return roll
def d4():
    roll = random.randint(1, 4)
    return roll
def d6():
    roll = random.randint(1, 6)
    return roll
def d8():
    roll = random.randint(1,8)
    return roll
def d10(): 
    roll = random.randint(1, 10)
    return roll
def d12():
    roll =random.randint(1,12)
    return roll
repeat = True
while repeat == True:

    dice_sel = input("What dice do you wanna roll? ")
    if dice_sel in dice:
        num_dice = int(input("How many times?"))
    else:
        while dice_sel not in dice:
            if dice_sel not in dice:
                print('Try d4, d6, d8, d10, d12, d20?')
            dice_sel = input("What dice do you wanna roll? ")
            
        num_dice = int(input("How many times?"))



    rolled = 0
    if dice_sel == "d20":
        while rolled < num_dice:
            print(d20())
            rolled = rolled + 1
    elif dice_sel == "d4":
        while rolled < num_dice:
            print(d4())
            rolled = rolled + 1
    elif dice_sel == "d6":
        while rolled < num_dice:
            print(d6())
            rolled = rolled + 1
    elif dice_sel == "d8":
        while rolled < num_dice:
            print(d8())
            rolled = rolled + 1
    elif dice_sel == "d10":
        while rolled < num_dice:
            print(d10())
            rolled = rolled + 1
    elif dice_sel == "d12":
        while rolled < num_dice:
            print(d12())
            rolled = rolled + 1
    else:
        print("try again")
    repeat_question = True
    again = input("Repeat?") 
    while repeat_question == True: 
        if again == "no":
            repeat_question = False
            repeat = False
        elif again == "yes":
            print("Good Choice!")
            repeat_question = False
            repeat == True
            
        else:
            again = input("Not valid, Repeat?")
            reap_question = True
print("Thanks")
