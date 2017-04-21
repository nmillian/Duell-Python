#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from board import Board


class BoardDisplay:

    ##########################################
    # Function Name: print_board

    # Purpose: Display the game boad.

    # Parameters: duellBoard, a board object, which holds the die and their locations.

    # Return Value: None.

    # Local Variables: None

    # Algorithm:
    # 1) Display the row of column numbers.
    # 2) Go through the duellBoard map, starting at (8,1) using two nested for loops.
    # 3) At each new row print the row number.
    # 3) If the tile type is 0 then print 0 becuase it’s empty.
    # 4) If the tile type is C then print the top and right computer die numbers.
    # 5) If the tile type is H then print the top and right human die numbers.

    # Assistance Received: None.
    ##########################################
    def print_board(self, duellBoard):

        # Display column numbers
        for c in range(1, 10, 1):
            print("  ", c, end='')

        for i in range(8, 0, -1):

            print("\n")
            print(i, " ", end='')

            for j in range(1, 10, 1):
                tile = str(i) + str(j)

                if(duellBoard.get_tile_type(tile) == "H"):
                    die = "H" + str(duellBoard.get_human_top(tile)) + str(duellBoard.get_human_right(tile))
                    print(die, "", end='')

                elif(duellBoard.get_tile_type(tile) == "C"):
                    die = "C" + str(duellBoard.get_computer_top(tile)) + str(duellBoard.get_computer_right(tile))
                    print(die, "", end='')

                else:
                    print("0", "  ", end='')

        print("\n")