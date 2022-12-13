# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

#globals
max_guesses = 7
total_guesses = 0
high_range = False

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number 
    if (high_range == False):
        secret_number = random.randint(0,99)
    else:
        secret_number = random.randint(0,999)
    global total_guesses 
    total_guesses = 0
    if (high_range == False):
        print ("New Game. Range is from 0 to 100.")
    else:
        print ("New Game. Range is from 0 to 1000.")
    print ("Number of remaining guesses is %d\n" % (max_guesses - total_guesses))
    frame.start()                                      

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global max_guesses
    max_guesses = 7
    global high_range
    high_range = False
    print ("Changing number range to [0, 100]\n")
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_guesses 
    max_guesses = 10    
    global high_range
    high_range = True
    print ("Changing number range to [0, 1000]\n")
    new_game()

def input_guess(guess):
    # main game logic goes here	
    global total_guesses 
    total_guesses += 1
    guess_int = int(guess)    
    print ("Guess was %d" % (guess_int))
    print ("Number of remaining guesses is %d" % (max_guesses - total_guesses))
    if (guess_int == secret_number):
        print ("Correct!\n")
        new_game()
       
    if ( total_guesses >= max_guesses):
        print ("You ran out of guesses. The number was %d\n" % (secret_number))
        new_game()   
    elif (guess_int > secret_number):
        print ("Lower!\n")
    else:
        print ("Higher!\n");  
       
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Restart",new_game)
frame.add_button("Range is 0 - 100",range100, 200)
frame.add_button("Range is 100 - 1000",range1000, 200)
guess = frame.add_input("Enter a guess:",input_guess,50)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric