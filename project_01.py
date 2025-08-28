# Snake Water Gun game

import random

computer = random.choice([-1, 0, 1])
you = int(input("Enter your choice : "))
reverse_dict = {-1:"snake", 0:"gun", 1:"water"}


print(f" you chose {reverse_dict[you]} \ncomputer chose {reverse_dict[computer]} ")

if(computer == you):
    print("its draw")

else:
    if(computer == -1 and you == 0):
        print("you win !")

    elif(computer == -1 and you == 1):
        print("you win !")

    elif(computer == 0 and you == -1):
        print("you lose !")

    elif(computer == 1 and you == -1):
        print("you win !")

    elif(computer == 1 and you == 0):
        print("you lose !")

    elif(computer == 0 and you == 1):
        print("you lose !")

    else:
        print("something went wrong")


print("Thanks !!!")