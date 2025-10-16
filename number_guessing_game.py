import random
num=random.randint(1,50)
guesses=[]
for attempt in range(5):
    a=int(input("Guess a number between 0 and 51: "))
    guesses.append(a)
    if a==num:
        if (attempt+1)==1:
            print(f"Correct!You guessed the number correctly on your {attempt+1}st try!")
        elif(attempt+1)==2:
            print(f"Correct!You guessed the number correctly on your {attempt+1}nd try!")
        elif (attempt+1)==3:
            print(f"Correct!You guessed the number correctly on your {attempt+1}rd try!")
        else:
            print(f"Correct!You guessed the number correctly on your {attempt+1}th try!")
        break
    elif a>num:
        print("Too high")
    else:
        print("Too low")
else:
    print("Sorry! The correct number was {}".format(num))
    print(f"Your guesses were: {guesses}")

