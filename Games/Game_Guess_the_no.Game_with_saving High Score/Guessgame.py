import random
randomNumber = random.randint(1,100)
userGuess=None
guesses = 0

while(userGuess != randomNumber):
    try:   # try except --> to handle errors    -> ValueError, ZeroDivisionError,     
        userGuess = int(input("Enter your Guess : "))
        guesses += 1
        if(userGuess==randomNumber):
            print("\n You guessed it RIGHT !!! \n")
            print("          YOU   WIN  !!! \n")

        else:
            if(userGuess>randomNumber):
                print("You guessed wrong!! Enter a smaller number")
            elif(userGuess<randomNumber):
                print("You guessed wrong!! Enter a greater number")
            
        print(f"             You guessed the number in {guesses} guesees\n")
    except Exception as e:
        print(f"You have given a wrong input with ERROR : \n")
        print("\n")
        print(f"{e}")
    #    exit()
 
#       finally: print("About High Scores: ")    # will always do even if exit

with open("guessGameHS.txt","r")as f:
    highscore = int(f.read())        # read only in String

if(guesses<highscore):
    print("YOu have just broken the HIGH SCORE")
    with open("guessGameHS.txt", "w") as f:
        f.write(str(guesses))
else :
    print(f"Highest Record: {highscore}  You could not break the record. Try next time... ")