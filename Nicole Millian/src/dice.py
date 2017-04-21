#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

class Dice:

    ##########################################
    # Function Name: __init__

    # Purpose: This is the Dice default constructor, to set the top and right values of the object.

    # Parameters:
    # top_num, an integer, the top number of  a die
    # right_num, an integer, the right umber of a die

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def __init__(self, top_num, right_num):
        self.__top = top_num
        self.__right = right_num

    ##########################################
    # Function Name: get_top

    # Purpose: To return the class variable top.

    # Parameters: None.

    # Return Value: Return an integer, the top die number.

    # Assistance Received: None.
    ##########################################
    def get_top(self):
        return self.__top

    ##########################################
    # Function Name: get_right

    # Purpose: To return the class variable right.

    # Parameters: None.

    # Return Value: Returns an integer, the right die number.

    # Assistance Received: None.
    ##########################################
    def get_right(self):
        return self.__right

    ##########################################
    # Function Name: set_top

    # Purpose: To set the class variable top to the correct number.

    # Parameters:
    # top_num, an integer, the top number of  a die

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_top(self, top_num):
        self.__top = top_num

    ##########################################
    # Function Name: set_right

    # Purpose: To set the class variable right to the correct number.

    # Parameters:
    # right_num, an integer, the right number of  a die

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_right(self, right_num):
        self.__right = right_num


