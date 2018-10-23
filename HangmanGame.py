import random,time

words=['Hangman','Parrot','Bird','Awkward','Banjo','Bungler','Crypt','Fervid','Easy','Haiku']
word=  random.choice(words).lower()
len_word=len(word)

print("You have to guess a {} char long word".format(len_word))
print("You have 8 chances to complete the word")
time.sleep(1)
print("A single character may also appear more than once\n All characters are lowercase")
time.sleep(2)
print("Press Ctrl+C to quit")


try:
    # creates a variable with an empty value
    guesses = ''


    turns = 8
    # check if the turns are more than zero
    while turns > 0:
        # make a counter that starts with zero
        failed = 0
        # for every character in secret_word
        for char in word:

            # see if the character is in the players guess
            if char in guesses:

                # print then out the character
                print(char,end='')


            else:

                # if not found, print a dash
                print("_ ",end='')


                # and increase the failed counter with one
                failed += 1

        # if failed is equal to zero

        # print You Won
        if failed == 0:
            print("\nYou won")
            # exit the script
            break

        # ask the user go guess a character
        guess = input("\nguess a character:")

        # set the players guess to guesses
        guesses += guess

        # if the guess is not found in the secret word
        if guess not in word:
            # turns counter decreases with 1 (now 9)
            turns -= 1

            # print wrong
            print("Wrong")

        # how many turns are left
        print("You have", + turns, 'more guesses')

        # if the turns are equal to zero
        if turns == 0:
            # print "You Loose"
            print("You Loose")
            print("The word is \"{}\"".format(word))
except KeyboardInterrupt as k:
    print("\nYou have quit the game.\n Goodbye.")