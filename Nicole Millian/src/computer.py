#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from player import Player
from human import Human
from board import Board

class Computer(Player):

    ##########################################
    # Function Name: decide_move

    # Purpose: To determine what move the computer should make.

    # Parameters: duellBoard, a board object, which stores the die for the game.
    # humanPlayer, a human object, which has functions pertaining to human dice movement.

    # Return Value: Returns a string of the move decided.

    # Local Variables: None.

    # Algorithm:
    # 1) Check if it's possible to win via moving to the enemy 1x1 die or the 1x1 die to the special tile.
    # 2) Check if it's possible to defend the special die.
    # 3) Check if it's possible to defend a normal die.
    # 4) Check if it's possible to kill an enemy die.
    # 5) Check if it's possible to move any of the die to an open space.
    # 6) If none of the above work it's not possible to make a move.

    # Assistance Received: None.
    ##########################################
    def decide_move(self, duellBoard, humanPlayer):

        if self.move_to_special_enemy_die(duellBoard) == True:
            return "SDIE"

        elif self.move_to_special_enemy_tile(duellBoard) == True:
            return "STILE"

        elif self.defend_special_die(duellBoard, humanPlayer) == True:
            return "DEFENDSDIE"

        elif self.defend_computer_die(duellBoard, humanPlayer) == True:
            return "DEFEND"

        elif self.kill_a_human_dice(duellBoard) == True:
            return "KILL"

        elif self.move_to_open_space(duellBoard) == True:
            return "OPEN"

        else:
            return "NONE"

    ##########################################
    # Function Name: move_to_special_enemy_die

    # Purpose: To determine if it is possible to capture the special 1x1 enemy die and if so make the move.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to move to the 1x1 die, false if it is not possible to move to the 1x1 die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # computerRight, an integer, the right number of a die.
    # frontal, an integer, the total number of spaces moved frontally
    # lateral, an integer, the total number of spaces moved laterally
    # specialRow, an integer, the row where the 1x1 die is located
    # specialColumn, an integer, the column where the 1x1 die is located
    # collision, a boolean, which holds true if there was a collision or false if there was none
    # lastSpace, an integer, which holds what value was at the last space

    # Algorithm:
    # 1) Get the row and column of the special die
    # 2) Go through and see if it’s possible for a computer die to move to the special die by calculating the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die that can capture the special die is found, print out what movement the die will make and return true.
    # 5) If no die can capture the special die, return false.

    # Assistance Received: None.
    ##########################################
    def move_to_special_enemy_die(self, duellBoard):

        humanSpecialRow = duellBoard.get_human_special_row()
        humanSpecialColumn = duellBoard.get_human_special_column()

        # Go through the computer dice
        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "C":
                    computerRow = r
                    computerColumn = c
                    computerTop = duellBoard.get_computer_top(tile)
                    computerRight = duellBoard.get_computer_right(tile)

                    # Go through the dice and see if it can hit the 1x1 die
                    frontal = duellBoard.calculate_frontal(computerRow, humanSpecialRow)
                    lateral = duellBoard.calculate_lateral(computerColumn, humanSpecialColumn)

                    if (frontal + lateral) == computerTop:
                        collision = self.check_collision(duellBoard, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "F")
                        lastSpace = self.check_last_path_space(duellBoard, humanSpecialRow, humanSpecialColumn)

                        if (collision == False) and (lastSpace == "SDIE"):
                            direction = self.movement_direction(computerRow, computerColumn, humanSpecialRow, humanSpecialColumn)
                            duellBoard.move_dice_computer(computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "F", direction)

                            newTile = str(humanSpecialRow) + str(humanSpecialColumn)
                            print("C", computerTop, computerRight, " was rolled frontally first from tile (",
                                  computerRow, ", ", computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                  ". It ended up on (", humanSpecialRow, ", ", humanSpecialColumn, ") the die is now C",
                                  duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer won by capturing the 1x1 die!", sep="")

                            return True

                        # Check laterally
                        else:
                            collision = self.check_collision(duellBoard, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "L")
                            lastSpace = self.check_last_path_space(duellBoard, humanSpecialRow, humanSpecialColumn)

                            if collision == False and lastSpace == "SDIE":
                                direction = self.movement_direction(computerRow, computerColumn, humanSpecialRow, humanSpecialColumn)
                                duellBoard.move_dice_computer(computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "L", direction)

                                newTile = str(humanSpecialRow) + str(humanSpecialColumn)
                                print("C", computerTop, computerRight, " was rolled laterally first from tile (",
                                      computerRow, ", ", computerColumn, ") it was rolled laterally by ", lateral, " and horizontally by ", frontal,
                                      ". It ended up on (", humanSpecialRow, ", ", humanSpecialColumn, ") the die is now C",
                                      duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer won by capturing the 1x1 die!", sep="")

                                return True
        return False

    ##########################################
    # Function Name: move_to_special_enemy_tile

    # Purpose:  To determine if it is possible to capture the special tile with the 1x1 die.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to move the 1x1 die to the special tile, false if it is not possible.

    # Local Variables: winningTileRow, an integer, the row where the human special tile is located.
    # winningTileColumn, an integer, the column where the human special tile is located.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # computerSpecialRow, an integer, the row where the 1x1 die is located.
    # computerSpecialColumn, an integer, the column where the 1x1 die is located.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for the 1x1 die to move to the special tile by calculating the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 2) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 3) If the 1x1 can capture the tile print out what movement the die will make and make the move and return true.
    # 4) If the die can't capture the special tile, return false.

    # Assistance Received: None.
    ##########################################
    def move_to_special_enemy_tile(self, duellBoard):
        computerSpecialRow = duellBoard.get_computer_special_row()
        computerSpecialColumn = duellBoard.get_computer_special_column()

        # The special human tile
        winningTileRow = 1
        winningTileColumn = 5

        frontal = duellBoard.calculate_frontal(computerSpecialRow, winningTileRow)
        lateral = duellBoard.calculate_lateral(computerSpecialColumn, winningTileColumn)

        if (frontal + lateral) == 1:
            collision = self.check_collision(duellBoard, computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn, "F")
            lastSpace = self.check_last_path_space(duellBoard, winningTileRow, winningTileColumn)

            if collision == False and lastSpace != "C":
                direction = self.movement_direction(computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn)
                duellBoard.move_dice_computer(computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn, "F", direction)

                print("C", 1, 1, " was rolled frontally first from tile (",
                      computerSpecialRow, ", ", computerSpecialColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                      ". It ended up on (", winningTileRow, ", ", winningTileColumn, ") the die is now C",
                      1, 1, ". The computer won by moving the 1x1 die to the special tile!", sep="")

                return True

            else:
                collision = self.check_collision(duellBoard, computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn, "L")
                lastSpace = self.check_last_path_space(duellBoard, winningTileRow, winningTileColumn)

                if collision == False and lastSpace != "C":
                    direction = self.movement_direction(computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn)
                    duellBoard.move_dice_computer(computerSpecialRow, computerSpecialColumn, winningTileRow, winningTileColumn, "L", direction)

                    print("C", 1, 1, " was rolled laterally first from tile (", computerSpecialRow, ", ",
                          computerSpecialColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", winningTileRow, ", ", winningTileColumn, ") the die is now C",
                          1, 1, ". The computer won by moving the 1x1 die to the special tile!", sep="")

                    return True

        return False

    ##########################################
    # Function Name: defend_special_die

    # Purpose: To determine if it is possible to defend the special die with another die.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # humanPlayer, a human object, used to access functions regarding moving human dice.

    # Return Value: A boolean value, true if it is possible to defend the special die, false if it is not possible to defend the die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # computerSpecialRow, an integer, the row where the 1x1 die is located.
    # computerSpecialColumn, an integer, the column where the 1x1 die is located.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # path, a list, used in order to keep track of the path a human die will take to attempt to capture a computer dice.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # computerRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for a human die to attack the special computer die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die that can capture the special die is found, go through and track the path the die will take in path.
    # 5) Go through the computer dictionary and see if there is a die that can block the pathway of the attacking die
    # 6) If a die can block, return true and print out it’s movement
    # 7) If no die can block, return false.

    # Assistance Received: None.
    ##########################################
    def defend_special_die(self, duellBoard, humanPlayer):
        computerSpecialRow = duellBoard.get_computer_special_row()
        computerSpecialColumn = duellBoard.get_computer_special_column()

        # Go through the human dice
        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "H":
                    humanRow = r
                    humanColumn = c
                    humanTop = duellBoard.get_human_top(tile)

                    # Go through the dice and see if it can hit the 1x1 die
                    frontal = duellBoard.calculate_frontal(humanRow, computerSpecialRow)
                    lateral = duellBoard.calculate_lateral(humanColumn, computerSpecialColumn)

                    if (frontal + lateral) == humanTop:
                        collision = humanPlayer.check_collision(duellBoard, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, "F")
                        lastSpace = humanPlayer.check_last_path_space(duellBoard, computerSpecialRow, computerSpecialColumn)

                        if collision == False and lastSpace != "H":
                            print("HUMAN tryin to kill", humanRow, humanColumn)
                            print("COMPUTER tryin to dead", computerSpecialRow, computerSpecialColumn)

                            path = []
                            self.get_human_path_frontal(path, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, frontal, lateral)

                            # see if a comp die can block
                            for r2 in range(8, 0, -1):
                                for c2 in range(1, 10, 1):
                                    computerTile = str(r2) + str(c2)

                                    if duellBoard.get_tile_type(computerTile) == "C":
                                        computerRow = r2
                                        computerColumn = c2
                                        computerTop = duellBoard.get_computer_top(computerTile)
                                        computerRight = duellBoard.get_computer_right(computerTile)

                                        for key in path:
                                            newRow = int(key[0])
                                            newColumn = int(key[1])

                                            newTile = str(newRow) + str(newColumn)

                                            frontal = duellBoard.calculate_frontal(computerRow, newRow)
                                            lateral = duellBoard.calculate_lateral(computerColumn, newColumn)

                                            # Checking frontally first
                                            if (frontal + lateral) == computerTop:
                                                collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "F")
                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)
                                                print("Defeding with computer die", computerRow, computerColumn, "moving to", newRow, newColumn, "front", frontal, "lat", lateral)

                                                if collision == False and lastSpace != "C":
                                                    direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                    duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "F", direction)

                                                    print("C", computerTop, computerRight, " was rolled frontally first from tile (",
                                                          computerRow, ", ", computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                          ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                          duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended the special die.", sep="")

                                                    return True

                                                # check laterally
                                                else:
                                                    collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "L")
                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                    if collision == False and lastSpace != "C":
                                                        direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                        duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "L", direction)
                                                        print("Defeding with computer die", computerRow, computerColumn, "moving to", newRow, newColumn, "front", frontal, "lat", lateral)

                                                        print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ",
                                                              computerColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                              duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended the special die.", sep="")

                                                        return True

                        # Check if the human die can reach comp die moving laterally first
                        else:
                            frontal = duellBoard.calculate_frontal(humanRow, computerSpecialRow)
                            lateral = duellBoard.calculate_lateral(humanColumn, computerSpecialColumn)

                            collision = humanPlayer.check_collision(duellBoard, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, "L")
                            lastSpace = humanPlayer.check_last_path_space(duellBoard, computerSpecialRow, computerSpecialColumn)

                            if collision == False and lastSpace != "H":
                                print("HUMAN tryin to kill", humanRow, humanColumn)
                                print("COMPUTER tryin to dead", computerSpecialRow, computerSpecialColumn)

                                path = []
                                self.get_human_path_lateral(path, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, frontal, lateral)

                                # see if a comp die can block
                                for r2 in range(8, 0, -1):
                                    for c2 in range(1, 10, 1):
                                        computerTile = str(r2) + str(c2)

                                        if duellBoard.get_tile_type(computerTile) == "C":
                                            computerRow = r2
                                            computerColumn = c2
                                            computerTop = duellBoard.get_computer_top(computerTile)
                                            computerRight = duellBoard.get_computer_right(computerTile)

                                            for key in path:
                                                newRow = int(key[0])
                                                newColumn = int(key[1])
                                                newTile = str(newRow) + str(newColumn)

                                                frontal = duellBoard.calculate_frontal(computerRow, newRow)
                                                lateral = duellBoard.calculate_lateral(computerColumn, newColumn)

                                                # Checking frontally first
                                                if (frontal + lateral) == computerTop:
                                                    collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "F")
                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                    if collision == False and lastSpace != "C":
                                                        direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                        duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "F", direction)

                                                        print("C", computerTop, computerRight, " was rolled frontally first from tile (",
                                                              computerRow, ", ", computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                              ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                              duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended the special die.", sep="")

                                                        return True

                                                    # check laterally
                                                    else:
                                                        collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "L")
                                                        lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                        if collision == False and lastSpace != "C":
                                                            direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                            duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "L", direction)

                                                            print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ",
                                                                  computerColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                                  duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended the special die.", sep="")

                                                            return True

        return False

    ##########################################
    # Function Name: defend_computer_die

    # Purpose: To determine if it is possible to defend a computer dice.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # humanPlayer, a human object, used to access functions regarding moving human dice.

    # Return Value: A boolean value, true if it is possible to defend the special die, false if it is not possible to defend the die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # path, a list, used in order to keep track of the path a human die will take to attempt to capture a computer dice.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # computerRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for a human die to attack a computer die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die that can capture a computer die is found, go through and track the path the die will take in path.
    # 5) Go through the computer dictionary and see if there is a die that can block the pathway of the attacking die
    # 6) If a die can block, return true and print out it’s movement
    # 7) If no die can block, return false.

    # Assistance Received: None.
    ##########################################
    def defend_computer_die(self, duellBoard, humanPlayer):

        # Go through the human dice
        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "H":
                    humanRow = r
                    humanColumn = c
                    humanTop = duellBoard.get_human_top(tile)

                    # Go through the dice and see if it can hit any computer die
                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            computerTile = str(i) + str(j)

                            # Found a comp tile
                            if duellBoard.get_tile_type(computerTile) == "C":
                                frontal = duellBoard.calculate_frontal(humanRow, i)
                                lateral = duellBoard.calculate_lateral(humanColumn, j)

                                # The human die can move the correct spaces to get to the comp die
                                if (frontal + lateral) == humanTop:
                                    collision = humanPlayer.check_collision(duellBoard, humanRow, humanColumn, i, j, "F")
                                    lastSpace = humanPlayer.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace != "H":

                                        path = []
                                        self.get_human_path_frontal(path, humanRow, humanColumn, i, j, frontal, lateral)

                                        # see if a comp die can block
                                        for r2 in range(8, 0, -1):
                                            for c2 in range(1, 10, 1):
                                                computerTile = str(r2) + str(c2)

                                                if duellBoard.get_tile_type(computerTile) == "C":
                                                    computerRow = r2
                                                    computerColumn = c2
                                                    computerTop = duellBoard.get_computer_top(computerTile)
                                                    computerRight = duellBoard.get_computer_right(computerTile)

                                                    for key in path:

                                                        newRow = int(key[0])
                                                        newColumn = int(key[1])

                                                        newTile = str(newRow) + str(newColumn)

                                                        frontal = duellBoard.calculate_frontal(computerRow, newRow)
                                                        lateral = duellBoard.calculate_lateral(computerColumn, newColumn)


                                                        # Checking frontally first
                                                        if (frontal + lateral) == computerTop:
                                                            collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "F")
                                                            lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                            if collision == False and lastSpace != "C":
                                                                direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                                duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "F", direction)

                                                                print("C", computerTop, computerRight, " was rolled frontally first from tile (",
                                                                      computerRow, ", ", computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                                      ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                                      duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended a die.", sep="")

                                                                return True

                                                            # check laterally
                                                            else:
                                                                collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "L")
                                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                                if collision == False and lastSpace != "C":
                                                                    direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                                    duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "L", direction)

                                                                    print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ",
                                                                          computerColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                                          duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended a die.", sep="")


                                                                    return True

                                    # Check if the human die can reach comp die moving laterally first
                                    else:
                                        frontal = duellBoard.calculate_frontal(humanRow, i)
                                        lateral = duellBoard.calculate_lateral(humanColumn, j)

                                        collision = humanPlayer.check_collision(duellBoard, humanRow, humanColumn, i, j, "L")
                                        lastSpace = humanPlayer.check_last_path_space(duellBoard, i, j)

                                        if collision == False and lastSpace != "H":

                                            path = []
                                            self.get_human_path_lateral(path, humanRow, humanColumn, i, j, frontal, lateral)

                                            # see if a comp die can block
                                            for r2 in range(8, 0, -1):
                                                for c2 in range(1, 10, 1):
                                                    computerTile = str(r2) + str(c2)

                                                    if duellBoard.get_tile_type(computerTile) == "C":
                                                        computerRow = r2
                                                        computerColumn = c2
                                                        computerTop = duellBoard.get_computer_top(computerTile)
                                                        computerRight = duellBoard.get_computer_right(computerTile)

                                                        for key in path:

                                                            newRow = int(key[0])
                                                            newColumn = int(key[1])

                                                            newTile = str(newRow) + str(newColumn)

                                                            frontal = duellBoard.calculate_frontal(computerRow, newRow)
                                                            lateral = duellBoard.calculate_lateral(computerColumn, newColumn)

                                                            # Checking frontally first
                                                            if (frontal + lateral) == computerTop:
                                                                collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "F")
                                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                                if collision == False and lastSpace != "C":
                                                                    direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                                    duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "F", direction)

                                                                    print("C", computerTop, computerRight, " was rolled frontally first from tile (",
                                                                          computerRow, ", ", computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                                          ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                                          duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended a die.", sep="")

                                                                    return True

                                                                # check laterally
                                                                else:
                                                                    collision = self.check_collision(duellBoard, computerRow, computerColumn, newRow, newColumn, "L")
                                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                                    if collision == False and lastSpace != "C":
                                                                        direction = self.movement_direction(computerRow, computerColumn, newRow, newColumn)
                                                                        duellBoard.move_dice_computer(computerRow, computerColumn, newRow, newColumn, "L", direction)

                                                                        print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ",
                                                                              computerColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", newRow, ", ", newColumn, ") the die is now C",
                                                                              duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". The computer defended a die.", sep="")

                                                                        return True

        return False

    ##########################################
    # Function Name: kill_a_human_dice

    # Purpose: To determine if it is possible to attack a human die.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to attack, false if it is not possible to attack.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # computerRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for a computer die to attack any of the human die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die can attack a human die make the move and move to the space of the human die.
    # 5) Return true if a human die can be attacked.
    # 6) Return false if a human die can't be attacked.

    # Assistance Received: None.
    ##########################################
    def kill_a_human_dice(self, duellBoard):

        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "C":
                    computerRow = r
                    computerColumn = c
                    computerTop = duellBoard.get_computer_top(tile)
                    computerRight = duellBoard.get_computer_right(tile)

                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            humanTile = str(i) + str(j)

                            # Found a human die to attempt to kill
                            if duellBoard.get_tile_type(humanTile) == "H":
                                humanRow = i
                                humanColumn = j

                                frontal = duellBoard.calculate_frontal(computerRow, i)
                                lateral = duellBoard.calculate_lateral(computerColumn, j)

                                if (frontal + lateral) == computerTop:
                                    collision = self.check_collision(duellBoard, computerRow, computerColumn, i, j, "F")
                                    lastSpace = self.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace == "H":
                                        direction = self.movement_direction(computerRow, computerColumn, i, j)
                                        duellBoard.move_dice_computer(computerRow, computerColumn, i, j, "F", direction)

                                        print("C", computerTop, computerRight, " was rolled frontally first from tile (", computerRow, ", ",
                                              computerColumn, ") horizontally by ", frontal, " and laterally by ", lateral, ". It ended up on (", i, ", ", j, ") the die is now C",
                                              duellBoard.get_computer_top(humanTile), duellBoard.get_computer_right(humanTile), ". The computer captured an enemy die.", sep="")

                                        return True

                                    else:
                                        collision = self.check_collision(duellBoard, computerRow, computerColumn, i, j, "L")
                                        lastSpace = self.check_last_path_space(duellBoard, i, j)

                                        if collision == False and lastSpace == "H":
                                            direction = self.movement_direction(computerRow, computerColumn, i, j)
                                            duellBoard.move_dice_computer(computerRow, computerColumn, i, j, "L", direction)

                                            print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ",
                                                  computerColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", i, ", ", j, ") the die is now C",
                                                  duellBoard.get_computer_top(humanTile), duellBoard.get_computer_right(humanTile), ". The computer captured an enemy die.", sep="")

                                            return True
        # Could not find a die to kill
        return False

    ##########################################
    # Function Name: move_to_open_space

    # Purpose: To determine if it is possible for a die to move to an open space.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to defend the special die, false if it is not possible to defend the die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # computerRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through the current diceComputer map.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die can make a move, make the movement and return true.
    # 5) If no die can make a move, return false.

    # Assistance Received: None.
    ##########################################
    def move_to_open_space(self, duellBoard):

        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "C":
                    computerRow = r
                    computerColumn = c
                    computerTop = duellBoard.get_computer_top(tile)
                    computerRight = duellBoard.get_computer_right(tile)

                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            newTile = str(i) + str(j)
                            frontal = duellBoard.calculate_frontal(computerRow, i)
                            lateral = duellBoard.calculate_lateral(computerColumn, j)

                            if (frontal + lateral) == computerTop:

                                collision = self.check_collision(duellBoard, computerRow, computerColumn, i, j, "F")
                                lastSpace = self.check_last_path_space(duellBoard, i, j)

                                if collision == False and lastSpace == "0":
                                    direction = self.movement_direction(computerRow, computerColumn, i, j)
                                    duellBoard.move_dice_computer(computerRow, computerColumn, i, j, "F", direction)

                                    print("C", computerTop, computerRight, " was rolled frontally first from tile (", computerRow, ", ", computerColumn,
                                          ") horizontally by ", frontal, " and laterally by ", lateral, ". It ended up on (", i, ", ", j, ") the die is now C",
                                          duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". It moved to an open space.",  sep="")

                                    return True

                                else:
                                    collision = self.check_collision(duellBoard, computerRow, computerColumn, i, j, "L")
                                    lastSpace = self.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace == "0":
                                        direction = self.movement_direction(computerRow, computerColumn, i, j)
                                        duellBoard.move_dice_computer(computerRow, computerColumn, i, j, "L", direction)

                                        print("C", computerTop, computerRight, " was rolled laterally first from tile (", computerRow, ", ", computerColumn,
                                              ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", i, ", ", j, ") the die is now C",
                                              duellBoard.get_computer_top(newTile), duellBoard.get_computer_right(newTile), ". It moved to an open space.", sep="")

                                        return True
        # Could not find an open space
        return False

    ##########################################
    # Function Name: is_valid_movement

    # Purpose: To determine if the number of movement spaces is equal to the number on the top of the die.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # row, an integer, used to represent the row of the die player wants to move.
    # column, an integer, used to represent the column of the die the player wants to move.
    # frontal, an integer, the number of spaces moved horizontally.
    # lateraly, an integer, the number of spaced moved laterally.

    # Return Value: Returns a boolean, True if the number of spaces moved and the top die are the same, otherwise returns False.

    # Assistance Received: None.
    ##########################################
    def is_valid_movement(self, duellBoard, row, column, frontal, lateral):
        tile = str(row) + str(column)

        total = frontal + lateral
        top = duellBoard.get_computer_top(tile)

        if total == top:
            return True
        else:
            return False

    ##########################################
    # Function Name: check_last_path_space

    # Purpose: To check what is located at the last space being moved to, a space, human, computer, special die, or special space.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # newRow, an integer, the location of the row where the die should move to.
    # newColumn, an integer, the location of the column where the die should move to.

    # Return Value: Returns a string describing what kind of tile the last space was.

    # Local Variables: tile, a string, the newRow and newColumn concatenated together to make a tile.

    # Algorithm:
    # 1) Check if the last space has an enemy die.
    # 2) If it has an enemy die, check if it's the special die, on the special space, or a normal die.
    # 3) Check if it's your die, which will be a collision.
    # 4) Check if it's the special space, the game will be over.
    # 5) Check if it's an empty space.
    # 6) If none of the above work it's an error.

    # Assistance Received: None.
    ##########################################
    def check_last_path_space(self, duellBoard, newRow, newColumn):
        tile = str(newRow) + str(newColumn)
        if duellBoard.get_tile_type(tile) == "H":
            if duellBoard.get_human_top(tile) == 1 and duellBoard.get_human_right(tile) == 1:
                return "SDIE"

            elif newRow == 1 and newColumn == 5:
                return "STILEENEMY"

            else:
                return "H"

        elif duellBoard.get_tile_type(tile) == "C":
            return "C"

        elif newRow == 1 and newColumn == 5:
            return "STILE"

        elif duellBoard.get_tile_type(tile) == "0":
            return "0"

        else:
            return "ERROR"

    ##########################################
    # Function Name: check_collision

    # Purpose: To determine if there is a collision on the pathway the die will take.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # row, an integer, the row the die is starting at.
    # column, an integer, the column the die is starting at.
    # newRow, an integer, the row where the die will end up.
    # newColumn, an integer, the column where the die will end up.
    # direction, a string, which determines which way the die will move first.

    # Return Value: Returns a boolean value, true means there was a collision, false means there was no collision

    # Local Variables: movement, a string, which holds the movement direction of the die

    # Algorithm:
    # 1) Get the movement of the die by calling the movement_direction function.
    # 2) If the direction is frontal first check the pathway moving frontally first before moving laterally.
    # 3) If the direction is lateral first check the pathway moving laterally first before moving frontally.
    # 4) Depending on what movement represents, check the pathway.
    # 5) If a collision is found the function returns true.
    # 6) If no collision is found the function returns false.

    # Assistance Received: None.
    ##########################################
    def check_collision(self, duellBoard, row, column, newRow, newColumn, direction):

        movement = self.movement_direction(row, column, newRow, newColumn)

        # Moving forwards first
        if (direction == "F") or (direction == "f"):
            if movement == "F":
                for i in range(row - 1, newRow, -1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "B":
                for i in range(row + 1, newRow, 1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "L":
                for i in range(column + 1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "R":
                for i in range(column - 1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "FL":
                for i in range(row - 1, newRow-1, -1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(column, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "FR":
                for i in range(row - 1, newRow-1, -1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(column, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "BL":
                for i in range(row + 1, newRow+1, 1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(column, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "BR":
                for i in range(row + 1, newRow+1, 1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(column, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            return False

        elif (direction == "l") or (direction == "L"):

            if movement == "F":
                for i in range(row - 1, newRow, -1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "B":
                for i in range(row + 1, newRow, 1):
                    tile = str(i) + str(column)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "L":
                for i in range(column + 1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "R":
                for i in range(column - 1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "FL":
                for i in range(column+1, newColumn+1, 1):
                    tile = str(row) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(row-1, newRow, -1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "FR":
                for i in range(column-1, newColumn-1, -1):
                    tile = str(row) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(row-1, newRow, -1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "BL":
                for i in range(column+1, newColumn+1, 1):
                    tile = str(row) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(row+1, newRow, 1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            elif movement == "BR":
                for i in range(column-1, newColumn-1, -1):
                    tile = str(row) + str(i)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

                for i in range(row+1, newRow, 1):
                    tile = str(i) + str(newColumn)
                    if duellBoard.get_tile_type(tile) != "0":
                        return True

            return False

    ##########################################
    # Function Name: movement_direction

    # Purpose: To figure out which way the die will be movnig to get to it's destination.

    # Parameters: row, an integer, the row the die is starting at.
    # column, an integer, the column the die is starting at.
    # newRow, an integer, the row where the die will end up.
    # newColumn, an integer, the column where the die will end up.

    # Return Value: Returns a string, which stands for the movement direction.

    # Local Variables: None.

    # Algorithm:
    # 1) Go through and check if the die is moving forwards or backwards, depending on if the newRow is smaller or greater than the row.
    # 2) Go through and check if the die is moving left or right, depending on if the newColumn is smaller or greater than the column
    # 3) If the newRow and row are equal or the newColumn and column are equal the die is only being moved in one direction.
    # 4) Return when a direction has been found.

    # Assistance Received: None.
    ##########################################
    def movement_direction(self, row, column, newRow, newColumn):
        row = int(row)
        column = int(column)
        newRow = int(newRow)
        newColumn = int(newColumn)

        # Only forward
        if (newRow < row) and (column == newColumn):
            return "F"

        # Only backwards
        elif (newRow > row) and (column == newColumn):
            return "B"

        # Only left
        elif (newColumn > column) and (row == newRow):
            return "L"

        # Only right
        elif (newColumn < column) and (row == newRow):
            return "R"

        elif (newRow < row) and (newColumn > column):
            return "FL"

        elif (newRow < row) and (newColumn < column):
            return "FR"

        elif (newRow > row) and (newColumn > column):
            return "BL"

        elif (newRow > row) and (newColumn < column):
            return "BR"

        else:
            return "ERROR"

    ##########################################
    # Function Name: get_human_path_frontal

    # Purpose: To get the path a human die will travel when it moves frontally first.

    # Parameters: path, a list, used to hold the tiles the human die will travel.
    # humanRow, an integer, the row where a human die is located.
    # humanCol, an integer, the column where a human die is located.
    # computerRow, an integer, the row where a computer die is located.
    # computerCol, an integer, the column where a comptuer die is lcoated.
    # frontal, an integer, the number of spaces moved frontally.
    # lateral, an integer, the number of spaces moved laterally.

    # Return Value: None.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # finalRow, an integer, the final row a human die will move to.

    # Algorithm:
    # 1) Check if the human die is moving forwards or backwards and get the movement.
    # 2) Check if the human die is moving left or right after it made it's horizontal movement.
    # 3) Keep track of all the tiles moved to in the path dictionary.

    # Assistance Received: None.
    ##########################################
    def get_human_path_frontal(self, path, humanRow, humanCol, computerRow, computerCol, frontal, lateral):
        # The front or backwards movement
        if humanRow <= computerRow:
            finalRow = humanRow + frontal

            # Moving forwards
            for i in range(humanRow, finalRow+1, 1):
                tile = str(i) + str(humanCol)
                path.append(tile)

            if humanCol <= computerCol:
                # Moving right
                for i in range(humanCol, humanCol+lateral+1, 1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

            elif humanCol >= computerCol:
                # Moving left
                for i in range(humanCol, humanCol-lateral-1, -1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

        elif humanRow > computerRow:
            finalRow = humanRow - frontal

            # Moving backwards
            for i in range(humanRow, finalRow - 1, -1):
                tile = str(i) + str(humanCol)
                path.append(tile)

            if humanCol <= computerCol:
                # Moving right
                for i in range(humanCol, humanCol + lateral + 1, 1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

            elif humanCol >= computerCol:
                # Moving left
                for i in range(humanCol, humanCol - lateral - 1, -1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

    ##########################################
    # Function Name: get_human_path_lateral

    # Purpose: To get the path a human die will travel when it moves laterally first.

    # Parameters: path, a list, used to hold the tiles the human die will travel.
    # humanRow, an integer, the row where a human die is located.
    # humanCol, an integer, the column where a human die is located.
    # computerRow, an integer, the row where a computer die is located.
    # computerCol, an integer, the column where a comptuer die is lcoated.
    # frontal, an integer, the number of spaces moved frontally.
    # lateral, an integer, the number of spaces moved laterally.

    # Return Value: None.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # finalCol, an integer, the final column a human die will move to.

    # Algorithm:
    # 1) Check if the human die is moving left or right and get the movement.
    # 2) Check if the human die is moving forwards or backwards after it made it's lateral movement.
    # 3) Keep track of all the tiles moved to in the path dictionary.

    # Assistance Received: None.
    ##########################################
    def get_human_path_lateral(self, path, humanRow, humanCol, computerRow, computerCol, frontal, lateral):

        if humanCol <= computerRow:
            finalCol = humanCol + lateral

            for i in range(humanCol, finalCol+1, 1):
                tile = str(humanRow) + str(i)
                path.append(tile)

            if humanRow <= computerRow:
                for i in range(humanRow, humanRow + frontal + 1, 1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

            elif humanRow >= computerRow:
                for i in range(humanRow, humanRow - frontal - 1, -1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

        elif humanCol > computerCol:
            finalCol = humanCol - lateral

            for i in range(humanCol, finalCol-1, -1):
                tile = str(humanRow) + str(i)
                path.append(tile)

            if humanRow <= computerRow:
                for i in range(humanRow, humanRow + frontal + 1, 1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

            elif humanRow >= computerRow:
                for i in range(humanRow, humanRow - frontal - 1, -1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)