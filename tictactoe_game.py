board = [' ' for x in range(10)]  # Creating spaces in the board


def display_board(board):  # Printing the board in sequence
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


def play():  # Main Function
    print('Welcome!')
    display_board(board)

    while not(isBoardFull(board)):  # Check if board is full
        if not(check_win('O', board)):  # Check if player has won
            player1_turn()
            display_board(board)
        else:
            print('O\'s have won!')
            break
        if not(check_win('X', board)):  # Check if player has won
            player2_turn()
            display_board(board)
        else:
            print('X\'s have won!')
            break
    if isBoardFull(board):  # Check if board is full resulting in a tie
        print('Board Full Game Over!')


def player1_turn():  # Player 1 'X' turn
    turn = True

    while turn:
        position = input("Select your X position from 1-9: ")
        try:
            position = int(position)
            if position > 0 and position < 10:  # Check if input is within range
                if check_pos(position):  # Check if position is occupied or not
                    turn = False
                    insert('X', position)
                else:
                    print("Sorry, position is occupied! Try another.")
            else:
                print("Position should be within range 1-9.")
        except:
            print("Please enter a number between 1-9!")


def player2_turn():  # Player 2 'O' turn
    turn = True

    while turn:
        position = input("Select your O position from 1-9: ")
        try:
            position = int(position)
            if position > 0 and position < 10:  # Check if input is within range
                if check_pos(position):  # Check if position is occupied or not
                    turn = False
                    insert('O', position)
                else:
                    print("Sorry, position is occupied! Try another.")
            else:
                print("Position should be within range 1-9.")
        except:
            print("Please enter a number between 1-9!")


def insert(letter, pos):  # Inserting a player's move
    board[pos] = letter


def check_win(letter, board_pos):  # Check if the player has won the game
    return (board_pos[1] == letter and board_pos[2] == letter and board_pos[3] == letter) or (board_pos[4] == letter and board_pos[5] == letter and board_pos[6] == letter) or (board_pos[7] == letter and board_pos[8] == letter and board_pos[9] == letter) or (board_pos[1] == letter and board_pos[4] == letter and board_pos[7] == letter) or (board_pos[2] == letter and board_pos[5] == letter and board_pos[8] == letter) or (board_pos[3] == letter and board_pos[6] == letter and board_pos[9] == letter) or (board_pos[1] == letter and board_pos[5] == letter and board_pos[9] == letter) or (board_pos[3] == letter and board_pos[5] == letter and board_pos[7] == letter)


def check_pos(pos):  # Check if position is occupied
    return board[pos] == ' '


def isBoardFull(board):  # Check if board is full
    if board.count(' ') > 1:
        return False
    else:
        return True


while True:  # Main loop to play the game
    ans = input('Play? Yes or No?')
    if ans.lower() == 'yes' or ans.lower() == 'y':
        board = [' ' for x in range(10)]
        print('-X-X-X-X-')
        play()
    else:
        break
