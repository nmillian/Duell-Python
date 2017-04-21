#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

class Player:

    ##########################################
    # Function Name: __init__

    # Purpose: To constructor for the Player class, sets the name to the entered name.

    # Parameters: name, a string, what the private variable name should be set to.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def __init__(self, name):
        self.__name = name

    ##########################################
    # Function Name: get_name

    # Purpose: To return the private name variable.

    # Parameters: None.

    # Return Value: name, a string, the private variable which holds the player name.

    # Assistance Received: None.
    ##########################################
    def get_name(self):
        return self.__name

    ##########################################
    # Function Name: set_name

    # Purpose: To set the player name to the desired string.

    # Parameters: name, a string, what the private variable name should be set to.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_name(self, name):
        self.__name = name
