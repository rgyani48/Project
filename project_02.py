#Random Number game
import random
n = random.randint(1,100)
a = 0
guesses = 1

while(a != n):

    a = int(input("Guess the Number :"))

    if(a > n):
        print("please enter lowest number")
        guesses += 1

    elif(a < n):
        print("please enter greater number")
        guesses += 1

print(f"you guess in {guesses} attempts")