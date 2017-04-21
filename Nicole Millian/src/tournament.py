#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

class Tournament:

    ##########################################
    # Function Name: __init__

    # Purpose: The Tournament class default constructor, used to initialize humanWins and computerWins to 0.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def __init__(self):
        self.__humanWins = 0
        self.__computerWins = 0

    ##########################################
    # Function Name: determine_winner

    # Purpose: Used in order to determine if the tournament was a draw, the human won, or the computer won.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def determine_winner(self):
        if self.__computerWins > self.__humanWins:
            print("The Computer won the tournament!")
        elif self.__computerWins < self.__humanWins:
            print("Congratulations, you have won the tournament!")
        elif self.__computerWins == self.__humanWins:
            print("The tournament has ended in a draw!")

    ##########################################
    # Function Name: get_computer_wins

    # Purpose: To get the number of wins the computer player has.

    # Parameters: None.

    # Return Value: Returns an integer value, the number of rounds the computer won.

    # Assistance Received: None.
    ##########################################
    def get_computer_wins(self):
        return self.__computerWins

    ##########################################
    # Function Name: get_human_wins

    # Purpose: To get the number of wins the human player has.

    # Parameters: None.

    # Return Value: Returns an integer value, the number of rounds the human won.

    # Assistance Received: None.
    ##########################################
    def get_human_wins(self):
        return self.__humanWins

    ##########################################
    # Function Name: update_computer_wins

    # Purpose: To add one to the number of wins the computer player has in computerWins.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def update_computer_wins(self):
        self.__computerWins = self.__computerWins + 1

    ##########################################
    # Function Name: get_human_wins

    # Purpose: To add one to the number of wins the human player has in humanWins.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def update_human_wins(self):
        self.__humanWins = self.__humanWins + 1

    ##########################################
    # Function Name: set_human_wins

    # Purpose: To set the number of human wins from a serialized file.

    # Parameters: serial, an integer, the number of human wins.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_human_wins(self, serial):
        self.__humanWins = int(serial)

    ##########################################
    # Function Name: set_computer_wins

    # Purpose: To set the number of computer wins from a serialized file.

    # Parameters: serial, an integer, the number of computer wins.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_computer_wins(self, serial):
        self.__computerWins = int(serial)