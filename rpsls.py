# Rock-paper-scissors-lizard-Spock program
import random
import simplegui
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#
# Then make a random choice from given range ( 0 - 4)
# Then use modulo arithmetic to decide the winner

# helper functions
result = ['','','']
def name_to_number(name):
    """
    Converts the choice to number
    Will be used to compute choice made by player
    """
    global result
    if (name == 'rock'):
        return 0
    elif (name == 'spock'):
        return 1
    elif (name == 'paper'):
        return 2
    elif (name == 'lizard'):
        return 3
    elif (name == 'scissor'):
        return 4
    else:
        print "Invalid choice made by player"
        result[1] = "Invalid choice Player!"


def number_to_name(number):
    """
    Coverts the number to readable choice
    Will be used to display choice made by computer
    """
    global result
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    elif (number == 4):
        return 'scissor'
    else:
        print "Invalid choice made by computer"
        result[1] = "Invalid choice computer!"

# Game function

def rpsls(player_choice): 
    global result
    #print "=============== Game begins ================"
    print "Player chooses ", player_choice
    result[0] = "Player chooses %s"%player_choice.upper()

    player_number = name_to_number(player_choice)
    
    if player_number is None:
        #Halt the game... Invalid choice
        print "********** REGAME ***********"
        result[2] = "** REGAME **"
        print
        return

    #Random generated on step of 1
    comp_number = random.randrange(0,5,1)

    comp_choice = number_to_name(comp_number)
    
    if comp_choice is None:
        #Halt the game... Invalid choice
        print "********** REGAME ***********"
        result[2] = "** REGAME **"
        print
        return
    
    print "Computer chooses: ", comp_choice
    result[1] = "Computer chooses: %s"%comp_choice.upper()

    difference = (comp_number - player_number) % 5
    
    #print difference

    if( difference == 1 or difference == 2):
        print "Computer wins!"
        result[2] = "Computer wins!"
    elif(difference == 3 or difference == 4):
        print "Player wins!"
        result[2] = "Player wins!"
    else:
        print "Player and computer tie!"
        result[2] = "TIE!"
    
    #Empty print for new line
    print 
    
def draw(canvas):
    canvas.draw_text(result[0], [20,20], 24, "Green")
    canvas.draw_text(result[1], [20,50], 24, "Green")
    canvas.draw_text(result[2], [20,100], 36, "Red")

def rock():

    rpsls("rock")
def paper():
    rpsls("paper")
def scissor():
    rpsls("scissor")
def lizard():
    rpsls("lizard")
def spock():
    rpsls("spock")

# Create a frame 
frame = simplegui.create_frame("RPSLS", 300, 250)
# Register event handlers
frame.set_draw_handler(draw)
choice1 = frame.add_button('ROCK',rock,100)
choice2 = frame.add_button('PAPER',paper,100)
choice3 = frame.add_button('SCISSOR',scissor,100)
choice4 = frame.add_button('LIZARD',lizard,100)
choice5 = frame.add_button('SPOCK',spock,100)
# Start the frame
frame.start()
