#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from player import Player


class Human(Player):
    ##########################################
    # Function Name: decide_move

    # Purpose: To determine what move the human player should make.

    # Parameters: duellBoard, a board object, which stores the die for the game.
    # computerPlayer, a computer object, which has functions pertaining to computer dice movement.

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
    def decide_move(self, duellBoard, computerPlayer):

        if self.move_to_special_enemy_die(duellBoard) == True:
            return "SDIE"

        elif self.move_to_special_enemy_tile(duellBoard) == True:
            return "STILE"

        elif self.defend_special_die(duellBoard, computerPlayer) == True:
            return "DEFENDSDIE"

        elif self.defend_human_die(duellBoard, computerPlayer) == True:
            return "DEFEND"

        elif self.kill_a_computer_dice(duellBoard) == True:
            return "KILL"

        elif self.move_to_open_space(duellBoard) == True:
            return "OPEN"

    ##########################################
    # Function Name: move_to_special_enemy_die

    # Purpose: To determine if it is possible to capture the special 1x1 enemy die and if so make the move.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to move to the 1x1 die, false if it is not possible to move to the 1x1 die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # humanRight, an integer, the right number of a die.
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
                    humanRight = duellBoard.get_human_right(tile)

                    # Go through the dice and see if it can hit the 1x1 die
                    frontal = duellBoard.calculate_frontal(humanRow, computerSpecialRow)
                    lateral = duellBoard.calculate_lateral(humanColumn, computerSpecialColumn)

                    if (frontal + lateral) == humanTop:
                        collision = self.check_collision(duellBoard, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, "F")
                        lastSpace = self.check_last_path_space(duellBoard, computerSpecialRow, computerSpecialColumn)

                        if collision == False and lastSpace == "SDIE":

                            print("H", humanTop, humanRight, " can be rolled frontally first from tile (",
                                  humanRow, ", ", humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                  ". It wil end up on (", computerSpecialRow, ", ", computerSpecialColumn, "). Will win by taking the opponent's 1x1 die!", sep="")

                            return True

                        # Check laterally
                        else:
                            collision = self.check_collision(duellBoard, humanRow, humanColumn, computerSpecialRow, computerSpecialColumn, "L")
                            lastSpace = self.check_last_path_space(duellBoard, computerSpecialRow, computerSpecialColumn)

                            if collision == False and lastSpace == "SDIE":

                                print("H", humanTop, humanRight, " can be rolled laterally first from tile (",
                                      humanRow, ", ", humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal,
                                      ". It ended up on (", computerSpecialRow, ", ", computerSpecialColumn, "). Will win by taking the opponents 1x1 die!", sep="")

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
    # humanSpecialRow, an integer, the row where the 1x1 die is located.
    # humanSpecialColumn, an integer, the column where the 1x1 die is located.
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
        humanSpecialRow = duellBoard.get_human_special_row()
        humanSpecialColumn = duellBoard.get_human_special_column()

        # The special human tile
        winningTileRow = 8
        winningTileColumn = 5

        frontal = duellBoard.calculate_frontal(humanSpecialRow, winningTileRow)
        lateral = duellBoard.calculate_lateral(humanSpecialColumn, winningTileColumn)

        if (frontal + lateral) == 1:
            collision = self.check_collision(duellBoard, humanSpecialRow, humanSpecialColumn, winningTileRow, winningTileColumn, "F")
            lastSpace = self.check_last_path_space(duellBoard, winningTileRow, winningTileColumn)

            if collision == False and lastSpace != "H":

                print("H", 1, 1, " can be rolled frontally first from tile (",
                      humanSpecialRow, ", ", humanSpecialColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                      ". It wille end up on (", winningTileRow, ", ", winningTileColumn, "). Will win by moving the 1x1 die to the special tile!", sep="")

                return True

            else:

                if collision == False and lastSpace != "H":
                    direction = self.movement_direction(humanSpecialRow, humanSpecialColumn, winningTileRow, winningTileColumn)
                    duellBoard.move_dice_computer(humanSpecialRow, humanSpecialColumn, winningTileRow, winningTileColumn, "L", direction)

                    print("H", 1, 1, " can be rolled laterally first from tile (", humanSpecialRow, ", ",
                          humanSpecialColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", winningTileRow, ", ", winningTileColumn,
                          ") . Will win by moving the 1x1 die to the special tile!", sep="")

                    return True

        return False

    ##########################################
    # Function Name: defend_special_die

    # Purpose: To determine if it is possible to defend the special die with another die.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # computerPlayer, a computer object, used to access functions regarding moving computer dice.

    # Return Value: A boolean value, true if it is possible to defend the special die, false if it is not possible to defend the die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # humanSpecialRow, an integer, the row where the 1x1 die is located.
    # humanSpecialColumn, an integer, the column where the 1x1 die is located.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # path, a list, used in order to keep track of the path a human die will take to attempt to capture a computer dice.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # humanRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for computer die to attack the special human die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die that can capture the special die is found, go through and track the path the die will take in path.
    # 5) Go through the diceHuman dictionary and see if there is a die that can block the pathway of the attacking die
    # 6) If a die can block, return true and print out it’s movement
    # 7) If no die can block, return false.

    # Assistance Received: None.
    ##########################################
    def defend_special_die(self, duellBoard, computerPlayer):
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

                    # Go through the dice and see if it can hit the 1x1 die
                    frontal = duellBoard.calculate_frontal(computerRow, humanSpecialRow)
                    lateral = duellBoard.calculate_lateral(computerColumn, humanSpecialColumn)

                    if (frontal + lateral) == computerTop:
                        collision = computerPlayer.check_collision(duellBoard, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "F")
                        lastSpace = computerPlayer.check_last_path_space(duellBoard, humanSpecialRow, humanSpecialColumn)

                        if collision == False and lastSpace != "C":

                            path = []
                            self.get_computer_path_frontal(path, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, frontal, lateral)

                            # see if a comp die can block
                            for r2 in range(8, 0, -1):
                                for c2 in range(1, 10, 1):
                                    humanTile = str(r2) + str(c2)

                                    if duellBoard.get_tile_type(humanTile) == "H":
                                        humanRow = r2
                                        humanColumn = c2
                                        humanTop = duellBoard.get_human_top(humanTile)
                                        humanRight = duellBoard.get_human_right(humanTile)

                                        for key in path:
                                            newRow = int(key[0])
                                            newColumn = int(key[1])
                                            newTile = str(newRow) + str(newColumn)

                                            frontal = duellBoard.calculate_frontal(humanRow, newRow)
                                            lateral = duellBoard.calculate_lateral(humanColumn, newColumn)

                                            # Checking frontally first
                                            if (frontal + lateral) == humanTop:
                                                collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "F")
                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                if collision == False and lastSpace != "H":

                                                    print("H", humanTop, humanRight, " can be rolled frontally first from tile (",
                                                          humanRow, ", ", humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                          ". It will end up on (", newRow, ", ", newColumn, ") . Will defend the special die.", sep="")

                                                    return True

                                                # check laterally
                                                else:
                                                    collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "L")
                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                    if collision == False and lastSpace != "H":

                                                        print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ",
                                                              humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It will end up on (", newRow, ", ", newColumn,
                                                              ") . Will defend the special die.", sep="")

                                                        return True

                        # Check if the computer die can reach comp die moving laterally first
                        else:
                            frontal = duellBoard.calculate_frontal(computerRow, humanSpecialRow)
                            lateral = duellBoard.calculate_lateral(computerColumn, humanSpecialColumn)

                            collision = computerPlayer.check_collision(duellBoard, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, "L")
                            lastSpace = computerPlayer.check_last_path_space(duellBoard, humanSpecialRow, humanSpecialColumn)

                            if collision == False and lastSpace != "C":

                                path = []
                                self.get_computer_path_lateral(path, computerRow, computerColumn, humanSpecialRow, humanSpecialColumn, frontal, lateral)

                                # see if a comp die can block
                                for r2 in range(8, 0, -1):
                                    for c2 in range(1, 10, 1):
                                        humanTile = str(r2) + str(c2)

                                        if duellBoard.get_tile_type(humanTile) == "H":
                                            humanRow = r2
                                            humanColumn = c2
                                            humanTop = duellBoard.get_human_top(humanTile)
                                            humanRight = duellBoard.get_human_right(humanTile)

                                            for key in path:
                                                newRow = int(key[0])
                                                newColumn = int(key[1])
                                                newTile = str(newRow) + str(newColumn)

                                                frontal = duellBoard.calculate_frontal(humanRow, newRow)
                                                lateral = duellBoard.calculate_lateral(humanColumn, newColumn)

                                                # Checking frontally first
                                                if (frontal + lateral) == humanTop:
                                                    collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "F")
                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                    if collision == False and lastSpace != "H":

                                                        print("H", humanTop, humanRight, " can be rolled frontally first from tile (",
                                                              humanRow, ", ", humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                              ". It will end up on (", newRow, ", ", newColumn, ") . Will defend the special die.", sep="")

                                                        return True

                                                    # check laterally
                                                    else:
                                                        collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "L")
                                                        lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                        if collision == False and lastSpace != "H":

                                                            print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ",
                                                                  humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It will end up on (", newRow, ", ", newColumn,
                                                                  "). Will defend the special die.", sep="")

                                                            return True

        return False

    ##########################################
    # Function Name: defend_human_die

    # Purpose: To determine if it is possible to defend a human dice.

    # Parameters: duellBoard, a board object, which holds the game dice.
    # computerPlayer, a computer object, used to access functions regarding moving computer dice.

    # Return Value: A boolean value, true if it is possible to defend the special die, false if it is not possible to defend the die.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # path, a list, used in order to keep track of the path a human die will take to attempt to capture a computer dice.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # humanRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for a computer die to attack a human die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die that can capture a human die is found, go through and track the path the die will take in path.
    # 5) Go through the human dictionary and see if there is a die that can block the pathway of the attacking die
    # 6) If a die can block, return true and print out it’s movement
    # 7) If no die can block, return false.

    # Assistance Received: None.
    ##########################################
    def defend_human_die(self, duellBoard, computerPlayer):
        # Go through the computer dice
        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "C":
                    computerRow = r
                    computerColumn = c
                    computerTop = duellBoard.get_computer_top(tile)

                    # Go through the dice and see if it can hit any human die
                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            humanTile = str(i) + str(j)

                            # Found a comp tile
                            if duellBoard.get_tile_type(humanTile) == "H":
                                frontal = duellBoard.calculate_frontal(computerRow, i)
                                lateral = duellBoard.calculate_lateral(computerColumn, j)

                                # The computer die can move the correct spaces to get to the human die
                                if (frontal + lateral) == computerTop:
                                    collision = computerPlayer.check_collision(duellBoard, computerRow, computerColumn, i, j, "F")
                                    lastSpace = computerPlayer.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace != "C":

                                        path = []
                                        self.get_computer_path_frontal(path, computerRow, computerColumn, i, j, frontal, lateral)

                                        # see if a comp die can block
                                        for r2 in range(8, 0, -1):
                                            for c2 in range(1, 10, 1):
                                                humanTile = str(r2) + str(c2)

                                                if duellBoard.get_tile_type(humanTile) == "H":
                                                    humanRow = r2
                                                    humanColumn = c2
                                                    humanTop = duellBoard.get_human_top(humanTile)
                                                    humanRight = duellBoard.get_human_right(humanTile)

                                                    for key in path:
                                                        newRow = int(key[0])
                                                        newColumn = int(key[1])
                                                        newTile = str(newRow) + str(newColumn)

                                                        frontal = duellBoard.calculate_frontal(humanRow, newRow)
                                                        lateral = duellBoard.calculate_lateral(humanColumn, newColumn)
                    
                                                        # Checking frontally first
                                                        if (frontal + lateral) == humanTop:
                                                            collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "F")
                                                            lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)
                                                      
                                                            if collision == False and lastSpace != "H":
                                                              
                                                                print("H", humanTop, humanRight, " can be rolled frontally first from tile (",
                                                                      humanRow, ", ", humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                                      ". It will end up on (", newRow, ", ", newColumn, ". Will defend a die.", sep="")

                                                                return True

                                                            # check laterally
                                                            else:
                                                                collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "L")
                                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                                if collision == False and lastSpace != "H":
                                                          
                                                                    print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ",
                                                                          humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It will end up on (", newRow, ", ", newColumn, 
                                                                          "). Will defend a die.", sep="")

                                                                    return True

                                    # Check if the computer die can reach comp die moving laterally first
                                    else:
                                        frontal = duellBoard.calculate_frontal(computerRow, i)
                                        lateral = duellBoard.calculate_lateral(computerColumn, j)

                                        collision = computerPlayer.check_collision(duellBoard, computerRow, computerColumn, i, j, "L")
                                        lastSpace = computerPlayer.check_last_path_space(duellBoard, i, j)

                                        if collision == False and lastSpace != "C":

                                            path = []
                                            self.get_computer_path_lateral(path, computerRow, computerColumn, i, j, frontal, lateral)

                                            # see if a comp die can block
                                            for r2 in range(8, 0, -1):
                                                for c2 in range(1, 10, 1):
                                                    humanTile = str(r2) + str(c2)

                                                    if duellBoard.get_tile_type(humanTile) == "H":
                                                        humanRow = r2
                                                        humanColumn = c2
                                                        humanTop = duellBoard.get_human_top(humanTile)
                                                        humanRight = duellBoard.get_human_right(humanTile)

                                                        for key in path:
                                                            newRow = int(key[0])
                                                            newColumn = int(key[1])
                                                            newTile = str(newRow) + str(newColumn)

                                                            frontal = duellBoard.calculate_frontal(humanRow, newRow)
                                                            lateral = duellBoard.calculate_lateral(humanColumn, newColumn)

                                                            # Checking frontally first
                                                            if (frontal + lateral) == humanTop:
                                                                collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "F")
                                                                lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)
                                                               
                                                                if collision == False and lastSpace != "H":
                                                                   
                                                                    print("H", humanTop, humanRight, " can be rolled frontally first from tile (",
                                                                          humanRow, ", ", humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral,
                                                                          ". It ended up on (", newRow, ", ", newColumn, "). Will defend a die.", sep="")

                                                                    return True

                                                                # check laterally
                                                                else:
                                                                    collision = self.check_collision(duellBoard, humanRow, humanColumn, newRow, newColumn, "L")
                                                                    lastSpace = self.check_last_path_space(duellBoard, newRow, newColumn)

                                                                    if collision == False and lastSpace != "H":
                                                                      
                                                                        print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ",
                                                                              humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", newRow, ", ", newColumn, 
                                                                              "). Will defend a die.", sep="")

                                                                        return True

        return False

    ##########################################
    # Function Name: kill_a_computer_dice

    # Purpose: To determine if it is possible to attack a computer die.

    # Parameters: duellBoard, a board object, which holds the game dice.

    # Return Value: A boolean value, true if it is possible to attack, false if it is not possible to attack.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # computerRow, an integer, the row where a computer die is located.
    # computerColumn, an integer, the column where a computer die is located.
    # computerTop, an integer, the top number of a die.
    # frontal, an integer, the total number of spaces moved frontally.
    # lateral, an integer, the total number of spaces moved laterally.
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # humanRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through and see if it’s possible for a human die to attack any of the computer die.
    # 2) Calculate the frontal and lateral movement and checking if it’s equal to the top of the die.
    # 3) If it’s equal call the check_collision and check_last_path_space function to test if the path works, checking moving frontally first then laterally.
    # 4) If a die can attack a computer die suggest the move.
    # 5) Return true if a computer die can be attacked.
    # 6) Return false if a computer die can't be attacked.

    # Assistance Received: None.
    ##########################################
    def kill_a_computer_dice(self, duellBoard):
        for r in range(8, 0, -1):
            for c in range(1, 10, 1):
                tile = str(r) + str(c)

                if duellBoard.get_tile_type(tile) == "H":
                    humanRow = r
                    humanColumn = c
                    humanTop = duellBoard.get_human_top(tile)
                    humanRight = duellBoard.get_human_right(tile)

                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            computerTile = str(i) + str(j)

                            # Found a computer die to attempt to kill
                            if duellBoard.get_tile_type(computerTile) == "C":
                                computerRow = i
                                computerColumn = j

                                frontal = duellBoard.calculate_frontal(humanRow, i)
                                lateral = duellBoard.calculate_lateral(humanColumn, j)

                                if (frontal + lateral) == humanTop:
                                    collision = self.check_collision(duellBoard, humanRow, humanColumn, i, j, "F")
                                    lastSpace = self.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace == "C":
   
                                        print("H", humanTop, humanRight, " can be rolled frontally first from tile (", humanRow, ", ",
                                              humanColumn, ") horizontally by ", frontal, " and laterally by ", lateral, ". It will end up on (", i, ", ", j, 
                                              "). Can capture an enemy die.", sep="")

                                        return True

                                    else:
                                        collision = self.check_collision(duellBoard, humanRow, humanColumn, i, j, "L")
                                        lastSpace = self.check_last_path_space(duellBoard, i, j)

                                        if collision == False and lastSpace == "C":
                                         
                                            print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ",
                                                  humanColumn, ") laterally by ", lateral, " and horizontally by ", frontal, ". It ended up on (", i, ", ", j,
                                                  "). Can capture an enemy die.", sep="")

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
    # humanRow, an integer, the row where a human die is located.
    # humanColumn, an integer, the column where a human die is located.
    # humanTop, an integer, the top number of a die.
    # humanRight, an integer, the right number of a die.
    # collision, a boolean, which holds true if there was a collision or false if there was none.
    # lastSpace, an integer, which holds what value was at the last space.

    # Algorithm:
    # 1) Go through the current diceHuman map.
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

                if duellBoard.get_tile_type(tile) == "H":
                    humanRow = r
                    humanColumn = c
                    humanTop = duellBoard.get_human_top(tile)
                    humanRight = duellBoard.get_human_right(tile)

                    for i in range(1, 9, 1):
                        for j in range(1, 10, 1):
                            frontal = duellBoard.calculate_frontal(humanRow, i)
                            lateral = duellBoard.calculate_lateral(humanColumn, j)

                            if (frontal + lateral) == humanTop:

                                collision = self.check_collision(duellBoard, humanRow, humanColumn, i, j, "F")
                                lastSpace = self.check_last_path_space(duellBoard, i, j)

                                if collision == False and lastSpace == "0":

                                    print("H", humanTop, humanRight, " can be rolled frontally first from tile (", humanRow, ", ", humanColumn,
                                          ") horizontally by ", frontal, " and laterally by ", lateral, ". It will end up on (", i, ", ", j,
                                          "). It can be moved to an open space.",  sep="")

                                    return True

                                else:
                                    collision = self.check_collision(duellBoard, humanRow, humanColumn, i, j, "L")
                                    lastSpace = self.check_last_path_space(duellBoard, i, j)

                                    if collision == False and lastSpace == "0":

                                        print("H", humanTop, humanRight, " can be rolled laterally first from tile (", humanRow, ", ", humanColumn,
                                              ") laterally by ", lateral, " and horizontally by ", frontal, ". It will end up on (", i, ", ", j,
                                              "). It can be moved to an open space.", sep="")

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
        top = duellBoard.get_human_top(tile)

        if(total == top):
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

        # Enemy on the tile
        if (duellBoard.get_tile_type(tile) == "C"):
            if ((duellBoard.get_computer_top(tile) == 1) and (duellBoard.get_computer_right(tile) == 1)):
                # Killed the special die
                return "SDIE"
            elif (newRow == 8) and (newColumn == 5):
                # The enemy key piece with an enemy die on it
                return "STILEENMEY"
            else:
                # Just an enemy die
                return "C"

        # Landed on a human die
        elif (duellBoard.get_tile_type(tile) == "H"):
            return "H"

        elif (newRow == 8) and (newColumn == 5):
            return "STILE"

        elif (duellBoard.get_tile_type(tile) == "0"):
            return "0"

        else:
            return "None"

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
        row = int(row)
        column = int(column)
        newRow = int(newRow)
        newColumn = int(newColumn)

        movement = self.movement_direction(row, column, newRow, newColumn)

        # Moving forward first
        if direction == "F" or direction == "f":
            # Only forward
            if(movement == "F"):
                # Moving forwards from the original tile
                for i in range(row+1, newRow, 1):
                    tile = str(i) + str(column)
                    if(duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only backwards
            elif (movement == "B"):
                # Moving backwards from the original tile
                for i in range(row-1, newRow, -1):
                    tile = str(i) + str(column)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only left
            elif (movement == "L"):
                # Moving left from the original tile
                for i in range(column-1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only right
            elif (movement == "R"):
                # Moving right from the original tile
                for i in range(column+1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Front and left
            elif (movement == "FL"):
                # Moving frontally before moving left
                for i in range(row+1, newRow+1, 1):
                    tile = str(i) + str(column)
                    if(duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving left from the original tile
                for i in range(column-1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Front and right
            elif (movement == "FR"):
                # Moving frontally before moving right
                for i in range(row+1, newRow+1, 1):
                    tile = str(i) + str(column)
                    if(duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving to the right
                for i in range(column+1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Backwards and left
            elif (movement == "BL"):
                # Moving backwards before moving left
                for i in range(row - 1, newRow-1, -1):
                    tile = str(i) + str(column)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving left from the original tile
                for i in range(column - 1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Backwards and right
            elif (movement == "BR"):
                # Moving backwards before moving right
                for i in range(row - 1, newRow-1, -1):
                    tile = str(i) + str(column)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving to the right
                for i in range(column+1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile)!= "0"):
                        return True

            # Didn't return in any previous case so return flase, no collision
            return False

        # Moving laterally first
        elif direction == "L" or direction == "l":
            # Only forward
            if (movement == "F"):
                # Moving forwards from the original tile
                for i in range(row + 1, newRow, 1):
                    tile = str(i) + str(column)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only backwards
            elif (movement == "B"):
                # Moving backwards from the original tile
                for i in range(row - 1, newRow, -1):
                    tile = str(i) + str(column)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only left
            elif (movement == "L"):
                # Moving left from the original tile
                for i in range(column - 1, newColumn, -1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Only right
            elif (movement == "R"):
                # Moving right from the original tile
                for i in range(column + 1, newColumn, 1):
                    tile = str(newRow) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Moving left before moving front
            elif (movement == "FL"):
                # Moving left from the original tile
                for i in range(column - 1, newColumn-1, -1):
                    tile = str(row) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving forwards
                for i in range(row + 1, newRow, 1):
                    tile = str(i) + str(newColumn)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Moving right then forwards
            elif (movement == "FR"):
                # Moving right from the original tile
                for i in range(column + 1, newColumn+1, 1):
                    tile = str(row) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving forwards
                for i in range(row + 1, newRow, 1):
                    tile = str(i) + str(newColumn)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Moving left then backwards
            elif (movement == "BL"):
                # Moving left from the original tile
                for i in range(column - 1, newColumn-1, -1):
                    tile = str(row) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving backwards
                for i in range(row-1, newRow, -1):
                    tile = str(i) + str(newColumn)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            #Moving right then backwards
            elif (movement == "BR"):
                # Moving right from the original tile
                for i in range(column + 1, newColumn+1, 1):
                    tile = str(row) + str(i)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

                # Moving backwards
                for i in range(row-1, newRow, -1):
                    tile = str(i) + str(newColumn)
                    if (duellBoard.get_tile_type(tile) != "0"):
                        return True

            # Didn't return in any previous case so return false, no collision
            return False

    ##########################################
    # Function Name: movement_direction

    # Purpose: To figure out which way the die will be moving to get to it's destination.

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
        if (newRow > row) and (column == newColumn):
            return "F"
        # Only backwards
        elif (newRow < row) and (column == newColumn):
            return "B"
        # Only left
        elif (newColumn < column) and (row == newRow):
            return "L"
        # Only right
        elif (newColumn > column) and (row == newRow):
            return "R"
        # Front and left
        elif (newRow > row) and (newColumn < column):
            return "FL"
        # Front and right
        elif (newRow > row) and (newColumn > column):
            return "FR"
        # Back and left
        elif (newRow < row) and (newColumn < column):
            return "BL"
        # Back and right
        elif (newRow < row) and (newColumn > column):
            return "BR"
        # Invalid
        else:
            return "INVALID"

    ##########################################
    # Function Name: get_computer_path_frontal

    # Purpose: To get the path a computer die will travel when it moves frontally first.

    # Parameters: path, a list, used to hold the tiles the human die will travel.
    # computerRow, an integer, the row where a computer die is located.
    # computerCol, an integer, the column where a computer die is lcoated.
    # humanRow, an integer, the row where a human die is located.
    # humanCol, an integer, the column where a human die is located.
    # frontal, an integer, the number of spaces moved frontally.
    # lateral, an integer, the number of spaces moved laterally.

    # Return Value: None.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # finalRow, an integer, the final row a computer die will move to.

    # Algorithm:
    # 1) Check if the computer die is moving forwards or backwards and get the movement.
    # 2) Check if the computer die is moving left or right after it made it's horizontal movement.
    # 3) Keep track of all the tiles moved to in the path dictionary.

    # Assistance Received: None.
    ##########################################
    def get_computer_path_frontal(self, path, computerRow, computerCol, humanRow, humanCol, frontal, lateral):

        # The front or backwards movement
        if computerRow <= humanRow:
            finalRow = computerRow + frontal

            # Moving forwards
            for i in range(computerRow, finalRow+1, 1):
                tile = str(i) + str(computerCol)
                path.append(tile)

            if computerCol <= humanCol:
                # Moving right
                for i in range(computerCol, computerCol+lateral+1, 1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

            elif computerCol >= humanCol:
                # Moving left
                for i in range(computerCol, computerCol-lateral-1, -1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

        elif computerRow > humanRow:
            finalRow = computerRow - frontal

            # Moving backwards
            for i in range(computerRow, finalRow - 1, -1):
                tile = str(i) + str(computerCol)
                path.append(tile)

            if computerCol <= humanCol:
                # Moving right
                for i in range(computerCol, computerCol + lateral + 1, 1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

            elif computerCol >= humanCol:
                # Moving left
                for i in range(computerCol, computerCol - lateral - 1, -1):
                    tile = str(finalRow) + str(i)
                    path.append(tile)

    ##########################################
    # Function Name: get_computer_path_lateral

    # Purpose: To get the path a human die will travel when it moves laterally first.

    # Parameters: path, a list, used to hold the tiles the computer die will travel.
    # computerRow, an integer, the row where a computer die is located.
    # computerCol, an integer, the column where a computer die is located.
    # humanRow, an integer, the row where a human die is located.
    # humanCol, an integer, the column where a human die is located.
    # frontal, an integer, the number of spaces moved frontally.
    # lateral, an integer, the number of spaces moved laterally.

    # Return Value: None.

    # Local Variables: tile, a string, used in order to access the value held at a tile.
    # finalCol, an integer, the final column a computer die will move to.

    # Algorithm:
    # 1) Check if the human die is moving left or right and get the movement.
    # 2) Check if the computer die is moving forwards or backwards after it made it's lateral movement.
    # 3) Keep track of all the tiles moved to in the path dictionary.

    # Assistance Received: None.
    ##########################################
    def get_computer_path_lateral(self, path, computerRow, computerCol, humanRow, humanCol, frontal, lateral):
        
        if computerCol <= humanRow:
            finalCol = computerCol + lateral

            for i in range(computerCol, finalCol+1, 1):
                tile = str(computerRow) + str(i)
                path.append(tile)

            if computerRow <= humanRow:
                for i in range(computerRow, computerRow + frontal + 1, 1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

            elif computerRow >= humanRow:
                for i in range(computerRow, computerRow - frontal - 1, -1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

        elif computerCol > humanCol:
            finalCol = computerCol - lateral

            for i in range(computerCol, finalCol-1, -1):
                tile = str(computerRow) + str(i)
                path.append(tile)

            if computerRow <= humanRow:
                for i in range(computerRow, computerRow + frontal + 1, 1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)

            elif computerRow >= humanRow:
                for i in range(computerRow, computerRow - frontal - 1, -1):
                    tile = str(i) + str(finalCol)
                    path.append(tile)