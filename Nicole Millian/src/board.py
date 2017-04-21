#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from dice import Dice


class Board:

    ##########################################
    # Function Name: __init__

    # Purpose: The Board class default constructor, used to initialize the duellBoard, diceHuman, and diceComputer dictionaries.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def __init__(self):
        self.__duellBoard = {}
        self.__diceHuman = {}
        self.__diceComputer = {}

        self.initialize_default_board()
        self.initialize_human_dice()
        self.initialize_computer_dice()

    ##########################################
    # Function Name: initialize_default_board

    # Purpose: Initialize the duellBoard dictionary with the correct default types, either H, C, or 0.

    # Parameters: None.

    # Return Value: None.

    # Local Variables: None

    # Algorithm:
    # 1) Using a nested for loop that begins at (8,1) and ends at (1,9) to go through the tiles.
    # 2) If the row is 8 then it's the computer's home row, so assign C to all the tiles.
    # 3) If the row is 1 then it's the human's home row, so assign H to all the tiles.
    # 4) All other rows are set to all 0 for empty spaces.

    # Assistance Received: None.
    ##########################################
    def initialize_default_board(self):
        for i in range(8, 0, -1):
            for j in range(1, 10, 1):

                tile = str(i) + str(j)

                if i == 8:
                    self.__duellBoard[tile] = "C"

                elif i == 1:
                    self.__duellBoard[tile] = "H"

                else:
                    self.__duellBoard[tile] = "0"

    ##########################################
    # Function Name: initialize_human_dice

    # Purpose: To set the initial dice values in the diceHuman dictionary.

    # Parameters: None.

    # Return Value: None.

    # Local Variables: None

    # Algorithm:
    # 1) Create 9 Dice objects.
    # 2) Assign each Dice object a top and right number as per the default values.
    # 3) Assign each default die to the correct tile using the row and column as the key.

    # Assistance Received: None.
    ##########################################
    def initialize_human_dice(self):
        dice1 = Dice(5, 6)
        self.__diceHuman['11'] = dice1

        dice2 = Dice(1, 5)
        self.__diceHuman['12'] = dice2

        dice3 = Dice(2, 1)
        self.__diceHuman['13'] = dice3

        dice4 = Dice(6, 2)
        self.__diceHuman['14'] = dice4

        dice5 = Dice(1, 1)
        self.__diceHuman['15'] = dice5

        dice6 = Dice(6, 2)
        self.__diceHuman['16'] = dice6

        dice7 = Dice(2, 1)
        self.__diceHuman['17'] = dice7

        dice8 = Dice(1, 5)
        self.__diceHuman['18'] = dice8

        dice9 = Dice(5, 6)
        self.__diceHuman['19'] = dice9

    ##########################################
    # Function Name: initialize_computer_dice

    # Purpose: To set the initial dice values in the diceComputer dictionary.

    # Parameters: None.

    # Return Value: None.

    # Local Variables: None

    # Algorithm:
    # 1) Create 9 Dice objects.
    # 2) Assign each Dice object a top and right number as per the default values.
    # 3) Assign each default die to the correct tile using the row and column as the key.

    # Assistance Received: None.
    ##########################################
    def initialize_computer_dice(self):
        dice1 = Dice(5, 6)
        self.__diceComputer['81'] = dice1

        dice2 = Dice(1, 5)
        self.__diceComputer['82'] = dice2

        dice3 = Dice(2, 1)
        self.__diceComputer['83'] = dice3

        dice4 = Dice(6, 2)
        self.__diceComputer['84'] = dice4

        dice5 = Dice(1, 1)
        self.__diceComputer['85'] = dice5

        dice6 = Dice(6, 2)
        self.__diceComputer['86'] = dice6

        dice7 = Dice(2, 1)
        self.__diceComputer['87'] = dice7

        dice8 = Dice(1, 5)
        self.__diceComputer['88'] = dice8

        dice9 = Dice(5, 6)
        self.__diceComputer['89'] = dice9

    ##########################################
    # Function Name: reset_board

    # Purpose: To reset the diceHuman, diceComputer, and duellBoard dictionaries to their original values.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def reset_board(self):
        self.__diceComputer.clear()
        self.initialize_computer_dice()

        self.__diceHuman.clear()
        self.initialize_human_dice()

        self.__duellBoard.clear()
        self.initialize_default_board()

    ##########################################
    # Function Name: get_tile_type

    # Purpose: To return the type of piece stored at each tile, either H, C, or 0.

    # Parameters: None.

    # Return Value: Returns 0 for an empty space, H for a human die, C for a computer die.

    # Assistance Received: None.
    ##########################################
    def get_tile_type(self, tile):
        return self.__duellBoard.get(tile)

    ##########################################
    # Function Name: get_human_top

    # Purpose: To return the top human die number stored at a specific tile.

    # Parameters: None.

    # Return Value: Returns an integer, the top human die number.

    # Assistance Received: None.
    ##########################################
    def get_human_top(self, tile):
        die = self.__diceHuman.get(tile)
        return die.get_top()

    ##########################################
    # Function Name: get_human_right

    # Purpose: To return the right human die number stored at a specific tile.

    # Parameters: None.

    # Return Value: Returns an integer, the right human die number.

    # Assistance Received: None.
    ##########################################
    def get_human_right(self, tile):
        die = self.__diceHuman.get(tile)
        return die.get_right()

    ##########################################
    # Function Name: get_computer_top

    # Purpose: To return the top computer die number stored at a specific tile.

    # Parameters: None.

    # Return Value: Returns an integer, the top computer die number.

    # Assistance Received: None.
    ##########################################
    def get_computer_top(self, tile):
        die = self.__diceComputer.get(tile)
        return die.get_top()

    ##########################################
    # Function Name: get_computer_right

    # Purpose: To return the right computer die number stored at a specific tile.

    # Parameters: None.

    # Return Value: Returns an integer, the right computer die number.

    # Assistance Received: None.
    ##########################################
    def get_computer_right(self, tile):
        die = self.__diceComputer.get(tile)
        return die.get_right()

    ##########################################
    # Function Name: get_computer_special_row

    # Purpose: To return the row the computer 1x1 die is at.

    # Parameters: None.

    # Return Value: Returns an integer, the row the 1x1 die is at.

    # Assistance Received: None.
    ##########################################
    def get_computer_special_row(self):

        for specialRow in range(8, 0, -1):
            for specialColumn in range(1, 10, 1):
                tile = str(specialRow) + str(specialColumn)
                if self.get_tile_type(tile) == "C":
                    if self.get_computer_top(tile) == 1 and self.get_computer_right(tile) == 1:
                        return int(specialRow)

    ##########################################
    # Function Name: get_computer_special_column

    # Purpose: To return the column the computer 1x1 die is at.

    # Parameters: None.

    # Return Value: Returns an integer, the column the 1x1 die is at.

    # Assistance Received: None.
    ##########################################
    def get_computer_special_column(self):
        for specialRow in range(8, 0, -1):
            for specialColumn in range(1, 10, 1):
                tile = str(specialRow) + str(specialColumn)
                if self.get_tile_type(tile) == "C":
                    if self.get_computer_top(tile) == 1 and self.get_computer_right(tile) == 1:
                        return int(specialColumn)

    ##########################################
    # Function Name: get_human_special_row

    # Purpose: To return the row the human 1x1 die is at.

    # Parameters: None.

    # Return Value: Returns an integer, the row the 1x1 die is at.

    # Assistance Received: None.
    ##########################################
    def get_human_special_row(self):

        # Find the human special die
        for specialRow in range(8, 0, -1):
            for specialColumn in range(1, 10, 1):
                tile = str(specialRow) + str(specialColumn)
                if self.get_tile_type(tile) == "H":
                    if self.get_human_top(tile) == 1 and self.get_human_right(tile) == 1:
                        return int(specialRow)

    ##########################################
    # Function Name: get_human_special_row

    # Purpose: To return the column the human 1x1 die is at.

    # Parameters: None.

    # Return Value: Returns an integer, the column the 1x1 die is at.

    # Assistance Received: None.
    ##########################################
    def get_human_special_column(self):

        for specialRow in range(8, 0, -1):
            for specialColumn in range(1, 10, 1):
                tile = str(specialRow) + str(specialColumn)
                if self.get_tile_type(tile) == "H":
                    if self.get_human_top(tile) == 1 and self.get_human_right(tile) == 1:
                        return int(specialColumn)

    ##########################################
    # Function Name: calculate_frontal

    # Purpose: Calculates the number of tiles moved in the horizontal direction.

    # Parameters: None.

    # Return Value: Returns an integer, the number of spaces moved horizontally, either row-newRow or newRow-row, depending on which is bigger.

    # Assistance Received: None.
    ##########################################
    def calculate_frontal(self, row, newRow):
        if row >= newRow:
            return row - newRow
        else:
            return newRow - row

    ##########################################
    # Function Name: calculate_lateral

    # Purpose: Calculates the number of tiles moved in the lateral direction

    # Parameters: None.

    # Return Value: Returns an integer, the number of spaces moved laterally, either column-newColumn or newColumn-column, depending on which is bigger.

    # Assistance Received: None.
    ##########################################
    def calculate_lateral(self, column, newColumn):
        if column >= newColumn:
            return column - newColumn
        else:
            return newColumn - column

    ##########################################
    # Function Name: move_dice_human

    # Purpose: To move the human dice to the appropriate spot with the appropriate new die numbers.

    # Parameters: player, a human object, used to get the movement direction the die is moving.
    # row, an integer, used to represent the row of the die player wants to move.
    # column, an integer, used to represent the column of the die the player wants to move.
    # newRow, an integer, the location of the row where the die should move to.
    # newColumn, an integer, the location of the column where the die should move to.
    # firstDirection, a string, whether the die should be moving frontally or laterally first.

    # Return Value: None.

    # Local Variables: frontal, an integer, used to calculate the number of horizontal movement spaces.
    # lateral, an integer, used to calculate the number of lateral movement spaces.
    # direction, a string, used to hold which direction the dice is moving.
    # tile, a string, the row and column concatenated in order to make the space on the board the original die is located at.
    # newTile, a string, the newRow and newColumn concatenated in order to make the space on the board the die is moving to.

    # Algorithm:
    # 1) Get the direction the die is moving across the board.
    # 2) If the last tile is a computer die, remove it from the diceComputer dictionary, because it is now dead.
    # 3) Make the tile in the dictionary a 0 because it's becoming an empty space.
    # 3) Make the newTile in the dictionary a H because it's becoming a human die.
    # 4) Add the die to the newTile in the diceHuman dictionary.
    # 5) Remove the die located at tile in the diceHuman dictionary.
    # 6) Call the movement functions in order to update the die numbers correctly at newTile in the diceHuman dictionary.

    # Assistance Received: None.
    ##########################################
    def move_dice_human(self, humanPlayer, row, column, newRow, newColumn, firstDirection):
        tile = str(row) + str(column)
        newTile = str(newRow) + str(newColumn)

        direction = humanPlayer.movement_direction(row, column, newRow, newColumn)

        if self.get_tile_type(newTile) == "C":
            del self.__diceComputer[newTile]

        if direction == "F":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            frontal = self.calculate_frontal(int(row), int(newRow))

            # Make the new die have the correct numbers
            self.move_frontal_human(newRow, newColumn, frontal)

        elif direction == "B":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            frontal = self.calculate_frontal(int(row), int(newRow))

            # Make the new die have the correct numbers
            self.move_backwards_human(newRow, newColumn, frontal)

        elif direction == "L":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))

            # Make the new die have the correct numbers
            self.move_left_human(newRow, newColumn, lateral)

        elif direction == "R":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))

            # Make the new die have the correct numbers
            self.move_right_human(newRow, newColumn, lateral)

        elif direction == "FL":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_frontal_human(newRow, newColumn, frontal)
                self.move_left_human(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_left_human(newRow, newColumn, lateral)
                self.move_frontal_human(newRow, newColumn, frontal)

        elif direction == "FR":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_frontal_human(newRow, newColumn, frontal)
                self.move_right_human(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_human(newRow, newColumn, lateral)
                self.move_frontal_human(newRow, newColumn, frontal)

        elif direction == "BL":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_backwards_human(newRow, newColumn, frontal)
                self.move_right_human(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_human(newRow, newColumn, lateral)
                self.move_backwards_human(newRow, newColumn, frontal)

        elif direction == "BR":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "H"

            # Put the new die in the table
            self.__diceHuman[newTile] = self.__diceHuman[tile]
            # Remove the old die
            del self.__diceHuman[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_backwards_human(newRow, newColumn, frontal)
                self.move_right_human(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_human(newRow, newColumn, lateral)
                self.move_backwards_human(newRow, newColumn, frontal)

    ##########################################
    # Function Name: move_frontal_human

    # Purpose: To set the correct top die when moving forwards.

    # Parameters: row, an integer, the row where the die will end up moving to
    # column, an integer, the column where the die will end up moving to
    # spaces, an integer, the number of spaces the die will be moved frontally

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update only the top die with a new number, as it is moving forward the right stays the same.

    # Assistance Received: None.
    ##########################################
    def move_frontal_human(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range (0, spaces, 1):
            # The one is on top
            if self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(2)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(5)

            # The two is on top
            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(1)

            # The three is on top
            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(5)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(2)

            # The four is on top
            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(5)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(2)

            # The five is on top
            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(6)

            # The six is on top
            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(5)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(2)

    ##########################################
    # Function Name: move_backwards_human

    # Purpose: To set the correct top die when moving backwards.

    # Parameters: row, an integer, the row where the die will end up moving to
    # column, an integer, the column where the die will end up moving to
    # spaces, an integer, the number of spaces the die will be moved.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update only the top die with a new number, as it is moving backwards the right stays the same.

    # Assistance Received: None.
    ##########################################
    def move_backwards_human(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range (0, spaces, 1):
            # The one is on top
            if self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(5)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(2)

            # The two is on top
            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(6)

            # The three is on top
            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(2)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(5)

            # The four is on top
            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(1)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(2)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(5)

            # The five is on top
            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(6)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(1)

            # The six is on top
            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(4)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(2)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(3)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(5)

    ##########################################
    # Function Name: move_left_human

    # Purpose: To set the correct top die when moving left.

    # Parameters: row, an integer, the row where the die will end up moving to
    # column, an integer, the column where the die will end up moving to
    # spaces, an integer, the number of spaces the die will be moved.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update the top and right die the correct numbers.

    # Assistance Received: None.
    ##########################################
    def move_left_human(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(6)

            # The two is on top
            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(5)

            # The three is on top
            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(4)

            # The four is on top
            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(3)

            # The five is on top
            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(2)

            # The six is on top
            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(1)

    ##########################################
    # Function Name: move_right_human

    # Purpose: To set the correct top die when moving right.

    # Parameters: row, an integer, the row where the die will end up moving to.
    # column, an integer, the column where the die will end up moving to.
    # spaces, an integer, the number of spaces the die will be moved.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update the top and right die the correct numbers.

    # Assistance Received: None.
    ##########################################
    def move_right_human(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(1)

            elif self.__diceHuman[tile].get_top() == 1 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(1)

            # The two is on top
            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(2)

            elif self.__diceHuman[tile].get_top() == 2 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(2)

            # The three is on top
            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(3)

            elif self.__diceHuman[tile].get_top() == 3 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(3)

            # The four is on top
            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(4)

            elif self.__diceHuman[tile].get_top() == 4 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(4)

            # The five is on top
            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 6:
                self.__diceHuman[tile].set_top(1)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 1:
                self.__diceHuman[tile].set_top(6)
                self.__diceHuman[tile].set_right(5)

            elif self.__diceHuman[tile].get_top() == 5 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(5)

            # The six is on top
            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 2:
                self.__diceHuman[tile].set_top(5)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 3:
                self.__diceHuman[tile].set_top(4)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 5:
                self.__diceHuman[tile].set_top(2)
                self.__diceHuman[tile].set_right(6)

            elif self.__diceHuman[tile].get_top() == 6 and self.__diceHuman[tile].get_right() == 4:
                self.__diceHuman[tile].set_top(3)
                self.__diceHuman[tile].set_right(6)

    ##########################################
    # Function Name: move_dice_computer

    # Purpose: To move the computer dice to the appropriate spot with the appropriate new die numbers.

    # Parameters: row, an integer, used to represent the row of the die player wants to move.
    # column, an integer, used to represent the column of the die the player wants to move.
    # newRow, an integer, the location of the row where the die should move to.
    # newColumn, an integer, the location of the column where the die should move to.
    # firstDirection, a string, whether the die should be moving frontally or laterally first.
    # direction, a string, the direction the die is moving across the board.

    # Return Value: None.

    # Local Variables: frontal, an integer, used to calculate the number of horizontal movement spaces.
    # lateral, an integer, used to calculate the number of lateral movement spaces.
    # direction, a string, used to hold which direction the dice is moving.
    # tile, a string, the row and column concatenated in order to make the space on the board the original die is located at.
    # newTile, a string, the newRow and newColumn concatenated in order to make the space on the board the die is moving to.

    # Algorithm:
    # 1) Get the direction the die is moving across the board.
    # 2) If the last tile is a human die, remove it from the diceHuman dictionary, because it is now dead.
    # 3) Make the tile in the duellBoard dictionary a 0 because it's becoming an empty space.
    # 3) Make the newTile in the duellBoard dictionary a C because it's becoming a computer die.
    # 4) Add the die to the newTile in the diceComputer dictionary.
    # 5) Remove the die located at tile in the diceComputer dictionary.
    # 6) Call the movement functions in order to update the die numbers correctly at newTile in the diceComputer dictionary.

    # Assistance Received: None.
    ##########################################
    def move_dice_computer(self, row, column, newRow, newColumn, firstDirection, direction):
        tile = str(row) + str(column)
        newTile = str(newRow) + str(newColumn)

        if self.get_tile_type(newTile) == "H":
            del self.__diceHuman[newTile]

        if direction == "F":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            frontal = self.calculate_frontal(int(row), int(newRow))

            # Make the new die have the correct numbers
            self.move_frontal_computer(newRow, newColumn, frontal)

        elif direction == "B":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            frontal = self.calculate_frontal(int(row), int(newRow))

            # Make the new die have the correct numbers
            self.move_backwards_computer(newRow, newColumn, frontal)

        elif direction == "L":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))

            # Make the new die have the correct numbers
            self.move_left_computer(newRow, newColumn, lateral)

        elif direction == "R":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))

            # Make the new die have the correct numbers
            self.move_right_computer(newRow, newColumn, lateral)

        elif direction == "FL":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_frontal_computer(newRow, newColumn, frontal)
                self.move_left_computer(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_left_computer(newRow, newColumn, lateral)
                self.move_frontal_computer(newRow, newColumn, frontal)

        elif direction == "FR":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_frontal_computer(newRow, newColumn, frontal)
                self.move_right_computer(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_computer(newRow, newColumn, lateral)
                self.move_frontal_computer(newRow, newColumn, frontal)

        elif direction == "BL":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_backwards_computer(newRow, newColumn, frontal)
                self.move_right_computer(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_computer(newRow, newColumn, lateral)
                self.move_backwards_computer(newRow, newColumn, frontal)

        elif direction == "BR":
            # Update the old tile to be 0
            self.__duellBoard[tile] = "0"
            # Make the new tile a H
            self.__duellBoard[newTile] = "C"

            # Put the new die in the table
            self.__diceComputer[newTile] = self.__diceComputer[tile]
            # Remove the old die
            del self.__diceComputer[tile]

            # Set the die correctly
            lateral = self.calculate_lateral(int(column), int(newColumn))
            frontal = self.calculate_frontal(int(row), int(newRow))

            if firstDirection == "f" or firstDirection == "F":
                self.move_backwards_computer(newRow, newColumn, frontal)
                self.move_right_computer(newRow, newColumn, lateral)

            elif firstDirection == "l" or firstDirection == "L":
                self.move_right_computer(newRow, newColumn, lateral)
                self.move_backwards_computer(newRow, newColumn, frontal)

    ##########################################
    # Function Name: move_frontal_computer

    # Purpose: To set the correct top die when moving forwards.

    # Parameters: row, an integer, the row where the die will end up moving to.
    # column, an integer, the column where the die will end up moving to.
    # spaces, an integer, the number of spaces the die will be moved.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update only the top die with a new number, as it is moving forward the right stays the same.

    # Assistance Received: None.
    ##########################################
    def move_frontal_computer(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(2)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(5)

            # The two is on top
            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(1)

            # The three is on top
            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(5)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(2)

            # The four is on top
            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(5)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(2)

            # The five is on top
            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(6)

            # The six is on top
            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(5)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(2)

    ##########################################
    # Function Name: move_backwards_computer

    # Purpose: To set the correct top die when moving backwards.

    # Parameters: row, an integer, the row where the die will end up moving to
    # column, an integer, the column where the die will end up moving to
    # spaces, an integer, the number of spaces the die will be moved backwards

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update only the top die with a new number, as it is moving backwards the right stays the same.

    # Assistance Received: None.
    ##########################################
    def move_backwards_computer(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(5)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(2)

            # The two is on top
            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(6)

            # The three is on top
            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(2)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(5)

            # The four is on top
            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(1)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(2)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(5)

            # The five is on top
            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(6)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(1)

            # The six is on top
            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(4)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(2)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(3)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(5)

    ##########################################
    # Function Name: move_left_computer

    # Purpose: To set the correct top die when moving left.

    # Parameters: row, an integer, the row where the die will end up moving to
    # column, an integer, the column where the die will end up moving to
    # spaces, an integer, the number of spaces the die will be moved to the left.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update the top and right die the correct numbers.

    # Assistance Received: None.
    ##########################################
    def move_left_computer(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(6)

            # The two is on top
            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(5)

            # The three is on top
            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(4)

            # The four is on top
            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(3)

            # The five is on top
            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(2)

            # The six is on top
            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(1)

    ##########################################
    # Function Name: move_right_human

    # Purpose: To set the correct top die when moving right.

    # Parameters: row, an integer, the row where the die will end up moving to.
    # column, an integer, the column where the die will end up moving to.
    # spaces, an integer, the number of spaces the die will be moved.

    # Return Value: None.

    # Local Variables: None.

    # Algorithm:
    # 1) Loop until the number of spaces moved has been met.
    # 2) In each iteration find the top and right die that matches the current one.
    # 3) Update the top and right die the correct numbers.

    # Assistance Received: None.
    ##########################################
    def move_right_computer(self, row, column, spaces):
        tile = str(row) + str(column)

        for i in range(0, spaces, 1):
            # The one is on top
            if self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(1)

            elif self.__diceComputer[tile].get_top() == 1 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(1)

            # The two is on top
            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(2)

            elif self.__diceComputer[tile].get_top() == 2 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(2)

            # The three is on top
            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(3)

            elif self.__diceComputer[tile].get_top() == 3 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(3)

            # The four is on top
            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(4)

            elif self.__diceComputer[tile].get_top() == 4 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(4)

            # The five is on top
            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 6:
                self.__diceComputer[tile].set_top(1)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 1:
                self.__diceComputer[tile].set_top(6)
                self.__diceComputer[tile].set_right(5)

            elif self.__diceComputer[tile].get_top() == 5 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(5)

            # The six is on top
            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 2:
                self.__diceComputer[tile].set_top(5)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 3:
                self.__diceComputer[tile].set_top(4)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 5:
                self.__diceComputer[tile].set_top(2)
                self.__diceComputer[tile].set_right(6)

            elif self.__diceComputer[tile].get_top() == 6 and self.__diceComputer[tile].get_right() == 4:
                self.__diceComputer[tile].set_top(3)
                self.__diceComputer[tile].set_right(6)

    ##########################################
    # Function Name: clear_for_serial

    # Purpose: To clear the diceHuman, diceComputer, and duellBoard dictionaries before reading in values from a saved file.

    # Parameters: None.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def clear_for_serial(self):
        self.__duellBoard.clear()
        self.__diceHuman.clear()
        self.__diceComputer.clear()

    ##########################################
    # Function Name: set_tile_type

    # Purpose: To set the duellBoard tile to the correct value, either H, C, or 0.

    # Parameters: row, an integer, the row a die is located.
    # column, an integer, the column a die is located.
    # type, a string, the type to set as, either a C, H, or 0.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_tile_type(self, row, column, type):
        tile = str(row) + str(column)
        self.__duellBoard[tile] = type

    ##########################################
    # Function Name: set_serial_computer

    # Purpose: To set the diceComputer tile to the correct dice value.

    # Parameters: row, an integer, the row a die is located.
    # column, an integer, the column a die is located.
    # top, an integer, the top value of a die.
    # right, an integer, the right value of a die.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_serial_computer(self, row, column, top, right):
        tile = str(row) + str(column)
        self.__diceComputer[tile] = Dice(int(top), int(right))

    ##########################################
    # Function Name: set_serial_human

    # Purpose: To set the diceHuman tile to the correct dice value.

    # Parameters: row, an integer, the row a die is located.
    # column, an integer, the column a die is located.
    # top, an integer, the top value of a die.
    # right, an integer, the right value of a die.

    # Return Value: None.

    # Assistance Received: None.
    ##########################################
    def set_serial_human(self, row, column, top, right):
        tile = str(row) + str(column)
        self.__diceHuman[tile] = Dice(int(top), int(right))