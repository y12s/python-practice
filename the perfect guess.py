import random 
randNumber = random.randint(1,100)

userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))

    if(userGuess == randNumber):
        print("correct guess. you won!!")
    else:
        if(userGuess>randNumber):

            print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed it wrong! enter a larger number")

    guesses += 1

print(f"you guessed the number in {guesses} guesses")
with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())
if (guesses<hiscore):
    print('you have just broken the high score!!')
with open("hiscore.txt", "w") as f:
    f.write(str(guesses))
