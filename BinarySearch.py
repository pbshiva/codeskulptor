# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print
    print "*********** NEW GAME **************"
    print "I'm going to guess from 0 to",high,"you have",attempt,"attempts"
    global secretNumber     
    secretNumber = random.randint(0,high)   
    
def reset():
    if rangeHun:
        range100()
    else:
        range1000()
    

def checkAttempt():
    if attempt == 0:
        print "You used all attemps! it was",secretNumber,"Let's try this again"
        reset()
    print attempt,"attempts left, ROLL IT"
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high
    high = 100
    global attempt
    attempt = 7
    global rangeHun
    rangeHun = True
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high
    high = 1000
    global attempt
    attempt = 10
    global rangeHun
    rangeHun = False
    new_game()
    
def input_guess(guess):
    global attempt       
    # main game logic goes here
    guess = int(guess)
    if guess > secretNumber :
        print "Your guess",guess, "is HIGHER than secret number"
    elif guess < secretNumber :
        print "Your guess",guess, "is lower than secret number"
    else:
        print "YOU GUESSED, THE SECRET NUMBER it is ",secretNumber
        print "lets do this again, this is fun"
        reset()
        return
    attempt -= 1
    checkAttempt()

    
# create frame
frame = simplegui.create_frame('Guessing game', 200, 200)
button1 = frame.add_button('Set Range 0 to 100', range100)
button2 = frame.add_button('Set Range 0 to 1000', range1000)
inp = frame.add_input('Your Guess', input_guess, 50)
frame.start

# register event handlers for control elements and start frame


# call new_game 
range100()


# always remember to check your completed program against the grading rubric
