#############################################################
# Name:  Nicole Millian                                     #
# Project:  Python - Extra Credit Project                   #
# Class:  CMPS 366 Organization of Programming Languages    #
# Date:  December 13, 2016                                  #
#############################################################

from player import Player
from human import Human
from game import Game
from board import Board
from boardDisplay import BoardDisplay
from computer import Computer
from tournament import Tournament


##########################################
# Function Name: human_input

# Purpose: Used to validate that the human player entered an integer for a row and column.

# Parameters: text, a string, the value the human player entered.

# Return Value: Returns either an integer if the value the player entered could be converted, or an error message if it could not.

# Assistance Received: None.
##########################################
def human_input(text):
    try:
        return int(text)
    except ValueError:
        print("You did not enter an integer.")
        return "Error"

##########################################
# Function Name: first_player

# Purpose: Used to display which player, the human or computer, gets to move first.

# Parameters: None.

# Return Value: None.

# Assistance Received: None.
##########################################
def first_player():
    # Decide the first player
    print("Deciding which player moves first...")
    duellGame.decide_first_player()

    print("You rolled:", duellGame.get_human_roll())
    print("The computer rolled:", duellGame.get_computer_roll())

    if duellGame.get_current_player() == "Human":
        print("You get to move first.")

    else:
        print("The computer gets to move first.")

##########################################
# Function Name: file_exists

# Purpose: To check if a fileName exists.

# Parameters: fileName, a string, the name a human entered to read from.

# Return Value: Returns a boolean value, true if the file exists, false if the file does not exist.

# Assistance Received: None.
##########################################
def file_exists(fileName):
    fileName += ".txt"

    try:
        f = open(fileName, "r")
        f.close()
    except IOError as e:
            return False
    return True

# The beginning of the main program
print("Welcome to Duell!")
humanName = input("What's your name? ")
computerName = "Computer"

displayBoard = BoardDisplay()
duellBoard = Board()

computerPlayer = Computer("Computer")
humanPlayer = Human(humanName)

duellGame = Game()
duellTournament = Tournament()

# Asking for a saved game or a new game
gameType = input("Do you want to start a new game or a saved game? (Enter N or S): ")
while gameType not in {"S", "s", "N", "n"}:
    gameType = input("Do you want to start a new game or a saved game? (Enter N or S): ")

# Start a new game
if gameType == "N" or gameType == "n":
    # Decide the first player
    first_player()
    displayBoard.print_board(duellBoard)
    game = True

# Read in from a save file
else:
    validFile = False
    while validFile == False:
        fileName = input("Enter a file name to resume from: ")
        validFile = file_exists(fileName)

        if validFile == True:
            duellGame.game_serialization_read(fileName, duellBoard, duellTournament)
            displayBoard.print_board(duellBoard)

    game = True

# Begin playing the game
while game:
    # The human is playing
    if duellGame.get_current_player() == "Human":
        print(humanPlayer.get_name(), "is now playing.")

        moveType = input("Do you want help or make a move? (Enter H or M): ")
        while moveType not in {"H", "h", "m", "M"}:
            moveType = input("Do you want help or make a move? (Enter H or M): ")

        # Human player wants help
        if moveType == "h" or moveType == "H":
            humanPlayer.decide_move(duellBoard, computerPlayer)

        # Picking the original tile
        validInitial = False
        while validInitial == False:
            # Make a move
            row = input("Please enter a row: ")
            check = human_input(row)

            while check == "Error":
                row = input("Please enter a row: ")
                check = human_input(row)

            column = input("Please enter a column: ")
            check = human_input(column)

            while check == "Error":
                column = input("Please enter a column: ")
                check = human_input(column)

            tile = str(row) + str(column)

            if duellBoard.get_tile_type(tile) != "H":
                validInitial = False
                print("You did not pick a human die to move, please choose again.")
            else:
                validInitial = True

        # Picking destination tile
        validTile = False
        while validTile == False:
            newRow = input("Please enter a destination row: ")
            check = human_input(newRow)

            while check == "Error":
                newRow = input("Please enter a destination row: ")
                check = human_input(newRow)

            newColumn = input("Please enter a destination column: ")
            check = human_input(newColumn)

            while check == "Error":
                newColumn = input("Please enter a destination column: ")
                check = human_input(newColumn)

            newTile = str(newRow) + str(newColumn)

            if duellBoard.get_tile_type(newTile) == "H" or duellBoard.get_tile_type(newTile) is None:
                validTile = False
                print("You did not pick a valid tile to move to.")
            else:
                validTile = True

        if row == newRow:
            direction = "L"
        elif column == newColumn:
            direction = "F"
        else:
            # Picking direction to move first
            direction = input("Which direction do you want to move first frontal or lateral? (Enter F or L): ")
            while direction not in {"F", "f", "L", "l"}:
                direction = input("Which direction do you want to move first frontal or lateral? (Enter F or L): ")

        # The movement frontal and laterally
        frontal = duellBoard.calculate_frontal(int(row), int(newRow))
        lateral = duellBoard.calculate_lateral(int(column), int(newColumn))

        # Check collision
        collision = humanPlayer.check_collision(duellBoard, row, column, newRow, newColumn, direction)

        # Check valid move spaces
        validMovement = humanPlayer.is_valid_movement(duellBoard, row, column, frontal, lateral)

        if collision == False and validMovement == True:
            lastSpace = humanPlayer.check_last_path_space(duellBoard, newRow, newColumn)

            # Human tile, invalid
            if lastSpace == "H":
                print("You did not pick a valid tile to move to.")

            # Empty space
            elif lastSpace == "0":
                print("You moved to an open space.")
                duellBoard.move_dice_human(humanPlayer, row, column, newRow, newColumn, direction)

                displayBoard.print_board(duellBoard)
                duellGame.set_current_player("Computer")
                # Set the current player back to computer

                saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")
                while saveAnswer not in {"Y", "y", "N", "n"}:
                    saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")

                if saveAnswer == "Y" or saveAnswer == "y":
                    duellGame.game_serialization_write(duellBoard, duellTournament)

            # Enemy die
            elif lastSpace == "C":
                print("You captured an enemy die.")
                duellBoard.move_dice_human(humanPlayer, row, column, newRow, newColumn, direction)

                displayBoard.print_board(duellBoard)
                duellGame.set_current_player("Computer")
                # Set the current player back to computer

                saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")
                while saveAnswer not in {"Y", "y", "N", "n"}:
                    saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")

                if saveAnswer == "Y" or saveAnswer == "y":
                    duellGame.game_serialization_write(duellBoard, duellTournament)

            # The enemy 1x1 die
            elif lastSpace == "SDIE":
                print("You won the round by capturing the opponent's 1x1 die!")
                duellBoard.move_dice_human(humanPlayer, row, column, newRow, newColumn, direction)
                duellTournament.update_human_wins()

                displayBoard.print_board(duellBoard)

                playAgain = input("Do you want to play again? (Enter Y or N): ")
                while playAgain not in {"Y", "N", "y", "n"}:
                    playAgain = input("Do you want to play again? (Enter Y or N): ")

                if playAgain == "Y" or playAgain == "y":
                    duellBoard.reset_board()
                    displayBoard.print_board(duellBoard)
                    currentPlayer = first_player()

                else:
                    duellTournament.determine_winner()
                    print("You scored:", duellTournament.get_human_wins())
                    print("Computer scored:", duellTournament.get_computer_wins())
                    game = False

            # The special tile
            elif lastSpace == "STILEENEMY" or lastSpace == "STILE":
                if duellBoard.get_human_top(tile) == "1" and duellBoard.get_human_top(tile) == "1":
                    print("You won the round by capturing the opponent's (8, 5) tile with your 1x1 die!")
                    duellBoard.move_dice_human(humanPlayer, row, column, newRow, newColumn, direction)
                    duellTournament.update_human_wins()

                    displayBoard.print_board(duellBoard)

                    playAgain = input("Do you want to play again? (Enter Y or N): ")
                    while playAgain not in {"Y", "N", "y", "n"}:
                        playAgain = input("Do you want to play again? (Enter Y or N): ")

                    if playAgain == "Y" or playAgain == "y":
                        duellBoard.reset_board()
                        displayBoard.print_board(duellBoard)
                        currentPlayer = first_player()

                    else:
                        duellTournament.determine_winner()
                        print("You scored:", duellTournament.get_human_wins())
                        print("Computer scored:", duellTournament.get_computer_wins())
                        game = False

                else:
                    duellBoard.move_dice_human(humanPlayer, row, column, newRow, newColumn, direction)
                    displayBoard.print_board(duellBoard)

        else:
            if collision == True:
                print("There was a collision on the path you selected, please change your move.")
            elif validMovement == False:
                print("The number of spaces moved were not the same as the top die number, please change your move.")

    # The computer is playing
    else:
        print("Computer is now playing.")
        move = computerPlayer.decide_move(duellBoard, humanPlayer)

        if move == "SDIE":
            # Won the game
            displayBoard.print_board(duellBoard)
            duellTournament.update_computer_wins()
            print("The computer won the round by capturing your 1x1 die!")
            playAgain = input("Do you want to play again? (Enter Y or N): ")
            while playAgain not in {"Y", "N", "y", "n"}:
                playAgain = input("Do you want to play again? (Enter Y or N): ")

            if playAgain == "Y" or playAgain == "y":
                duellBoard.reset_board()
                displayBoard.print_board(duellBoard)
                currentPlayer = first_player()

            else:
                duellTournament.determine_winner()
                print("You scored:", duellTournament.get_human_wins())
                print("Computer scored:", duellTournament.get_computer_wins())
                game = False

        elif move == "STILE":
            # Won the game
            displayBoard.print_board(duellBoard)
            duellTournament.update_computer_wins()
            print("The computer won the round by capturing the special tile with the 1x1 die!")
            playAgain = input("Do you want to play again? (Enter Y or N): ")
            while playAgain not in {"Y", "N", "y", "n"}:
                playAgain = input("Do you want to play again? (Enter Y or N): ")

            if playAgain == "Y" or playAgain == "y":
                duellBoard.reset_board()
                displayBoard.print_board(duellBoard)
                currentPlayer = first_player()

            else:
                duellTournament.determine_winner()
                print("You scored:", duellTournament.get_human_wins())
                print("Computer scored:", duellTournament.get_computer_wins())
                game = False

        else:
            displayBoard.print_board(duellBoard)
            duellGame.set_current_player("Human")

            saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")
            while saveAnswer not in {"Y", "y", "N", "n"}:
                saveAnswer = input("Would you like to save and quit? (Enter Y or N): ")

            if saveAnswer == "Y" or saveAnswer == "y":
                duellGame.game_serialization_write(duellBoard, duellTournament)
