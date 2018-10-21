import random

def guess(number):

    def recfun():
        guesscounter = 0
        guess = int(input("Try to Guess the number b/w 1 to 100?"))


        if guess < number:
            print("its quite low! Go more Up")
            recfun()
        elif guess > number:
            print("its quite High! Go little Down")
            recfun()
        elif guess == number:
            print("You Guessed it correctly")

    recfun()

def main():
    number=random.randint(1,101)
    guess(number)

    again=input("Wanna play again? y/n")
    if again=='y':
        main()

if __name__=="__main__":main()
