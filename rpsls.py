# Rock-paper-scissors-lizard-Spock program
import random

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

def name_to_number(name):
    """
    Converts the choice to number
    Will be used to compute choice made by player
    """
    if (name == 'rock'):
        return 0
    elif (name == 'Spock'):
        return 1
    elif (name == 'paper'):
        return 2
    elif (name == 'lizard'):
        return 3
    elif (name == 'scissors'):
        return 4
    else:
        print "Invalid choice made by player"


def number_to_name(number):
    """
    Coverts the number to readable choice
    Will be used to display choice made by computer
    """
    if (number == 0):
        return 'rock'
    elif (number == 1):
        return 'Spock'
    elif (number == 2):
        return 'paper'
    elif (number == 3):
        return 'lizard'
    elif (number == 4):
        return 'scissors'
    else:
        print "Invalid choice made by computer"

# Game function

def rpsls(player_choice): 
    #print "=============== Game begins ================"
    print "Player chooses ", player_choice

    player_number = name_to_number(player_choice)
    
    if player_number is None:
        #Halt the game... Invalid choice
        print "********** REGAME ***********"
        print
        return

    #Random generated on step of 1
    comp_number = random.randrange(0,5,1)

    comp_choice = number_to_name(comp_number)
    
    if comp_choice is None:
        #Halt the game... Invalid choice
        print "********** REGAME ***********"
        print
        return
    
    print "Computer chooses: ", comp_choice

    difference = (comp_number - player_number) % 5
    
    #print difference

    if( difference == 1 or difference == 2):
        print "Computer wins!"
    elif(difference == 3 or difference == 4):
        print "Player wins!"
    else:
        print "Player and computer tie!"
    
    #Empty print for new line
    print 
    
# test calls - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

#Friends are going to make funny choices, don't they ;)
rpsls("bazooka")

#rubric complaint.
