#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from random import randint


class Game:

    ##########################################
    # Function Name: __init__

    # Purpose: This is the Game default constructor, to set the computer and human wins to 0 and the currentPlayer to none.

    # Parameters:None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def __init__(self):
        self.__numberHuman = 0
        self.__numberComputer = 0
        self.__currentPlayer = "None"

    ##########################################
    # Function Name: decide_first_player

    # Purpose: Used in order to roll a random number between 1 and 6 for the computer and human player to decide who plays first.
    # Sets the currentPlayer variable to either Human or Computer depending on who rolled a higher die.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def decide_first_player(self):
        while self.__numberComputer == self.__numberHuman:
            self.__numberHuman = randint(1, 6)
            self.__numberComputer = randint(1, 6)

        if self.__numberHuman < self.__numberComputer:
            self.__currentPlayer = "Computer"
        else:
            self.__currentPlayer = "Human"

    ##########################################
    # Function Name: get_human_roll

    # Purpose: To get the roll the human die rolled when deciding which player goes first.

    # Parameters: None.

    # Return Value: Returns an integer, the number the human rolled when deciding who plays first.

    # Assistance Received: None.
    ##########################################
    def get_human_roll(self):
        return self.__numberHuman

    ##########################################
    # Function Name: get_computer_roll

    # Purpose: To get the roll the comptuer die rolled when deciding which player goes first.

    # Parameters: None.

    # Return Value: Returns an integer, the number the comptuer rolled when deciding who plays first.

    # Assistance Received: None.
    ##########################################
    def get_computer_roll(self):
        return self.__numberComputer

    ##########################################
    # Function Name: get_current_player

    # Purpose: To get the player who is currently making a move.

    # Parameters: None.

    # Return Value: Return a string, the currentPlayer, either Human or Computer.

    # Assistance Received: None.
    ##########################################
    def get_current_player(self):
        return self.__currentPlayer

    ##########################################
    # Function Name: set_current_player

    # Purpose: To update the currentPlayer to the next player, either Human or Computer.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_current_player(self, nextPlayer):
        self.__currentPlayer = nextPlayer

    ##########################################
    # Function Name: game_serialization_read

    # Purpose: To read in the save file and correctly assign values to variables in order to resume the game from a saved state.

    # Parameters: fileName, a string, the name of a file to read from.
    # duellBoard, a board object, which stores the die for the game.
    # duellTournament, a tournament object, which stores how many wins the computer and human player have.

    # Return Value: None.

    # Local Variables: line, a list, used in order to hold each line read in.
    # words, a list, used in order to split a line into individual words.
    # tile, a string, the tile to update the contents of on the board.

    # Algorithm:
    # 1) Append .txt to the fileName and open the file for reading.
    # 2) Read in each line from the file.
    # 3) Split the line into words.
    # 4) If the word is Computer or Human update the tournament scores.
    # 5) If the word is Next update the currentPlayer.
    # 6) If the word begins with a C or H parse the next two chars in the word as the top die number and the right die number
    # 7) Store the die at the correct tile in the diceHuman or diceComputer dictionary and update the duellBoard dictionary with the correct type.

    # Assistance Received: None.
    ##########################################
    def game_serialization_read(self, fileName, duellBoard, duellTournament):
        duellBoard.clear_for_serial()

        fileName += ".txt"

        fo = open(fileName, "r")

        row = 10

        for line in fo.readlines():
            line.rstrip("\n")
            column = 0

            words = line.split()
            row = row - 1

            for word in words:
                if word != "Board:":

                    if words[0] == "Computer":
                        wins = str(words[2])
                        duellTournament.set_computer_wins(wins)

                    elif words[0] == "Human":
                        wins = str(words[2])
                        duellTournament.set_human_wins(wins)

                    elif words[0] == "Next":
                        self.set_current_player(str(str(words[2])))

                    else:
                        column = column + 1

                        if str(word[0]) == "C":
                            top = int(word[1])
                            right = int(word[2])
                            duellBoard.set_tile_type(row, column, "C")
                            duellBoard.set_serial_computer(row, column, top, right)

                        elif str(word[0]) == "H":
                            top = int(word[1])
                            right = int(word[2])
                            duellBoard.set_tile_type(row, column, "H")
                            duellBoard.set_serial_human(row, column, top, right)

                        else:
                            duellBoard.set_tile_type(row, column, "0")

        fo.close()

    ##########################################
    # Function Name: game_serialization_write

    # Purpose: To write the current state of the game to a saved file in order to resume it at a later point.

    # Parameters: duellBoard, a board object, which stores the die for the game.
    # duellTournament, a tournament object, which stores how many wins the computer and human player have.

    # Return Value: None.

    # Local Variables: tile, a string, the tile to update the contents of on the board.

    # Algorithm:
    # 1) Append the string, name, with .txt in order to create a file.
    # 2) Cycle through the board using a nested for loop, beginning in the to left corner (8,1) and ending at (1, 9)
    # 3) Check the tile type at each space, 0 for empty, C for computer, and H for human.
    # 4) Get the top and right numbers and write them to the file accordingly if it's a human or computer die, otherwise write 0.
    # 5) Write the computer wins, human wins, and the next player to the file.

    # Assistance Received: None.
    ##########################################
    def game_serialization_write(self, duellBoard, duellTournament):

        fileName = input("What would you like to name the file?: ")

        fileName += ".txt"

        fo = open(fileName, "w")

        fo.write("Board: \n")

        for r in range (8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)
                if duellBoard.get_tile_type(tile) == "C":
                    fo.write("C")
                    fo.write(str(duellBoard.get_computer_top(tile)))
                    fo.write(str(duellBoard.get_computer_right(tile)))
                    fo.write(" ")

                elif duellBoard.get_tile_type(tile) == "H":
                    fo.write("H")
                    fo.write(str(duellBoard.get_human_top(tile)))
                    fo.write(str(duellBoard.get_human_right(tile)))
                    fo.write(" ")

                else:
                    fo.write("0")
                    fo.write(" ")

            fo.write("\n")

        fo.write("Computer wins: ")
        fo.write(str(duellTournament.get_computer_wins()))
        fo.write("\n")

        fo.write("Human wins: ")
        fo.write(str(duellTournament.get_human_wins()))
        fo.write("\n")

        fo.write("Next player: ")
        fo.write(str(self.get_current_player()))
        fo.write("\n")

        fo.close()

        quit()