import random

def win(board):
    if (board[0] == board[1] == board[2]) or (board[0] == board[3] == board[6]) :
        if board[0] == computer_choice:
            return 0
        elif board[0] == choice:
            return 1

    elif (board[3] == board[4] == board[5]) or (board[1] == board[4] == board[7]) or (board[0] == board[4] == board[8]) or (board[6] == board[4] == board[2]):
        if board[4] == computer_choice:
            return 0
        elif board[4] == choice:
            return 1
        
    elif (board[6] == board[7] == board[8]) or (board[2] == board[5] == board[8]):
        if board[8] == computer_choice:
            return 0
        elif board[8] == choice:
            return 1

    elif " " not in board:
        return 2

    else:
        return None

board = [" "]*9
print(f"""
Please note the tile notations that you should use for input.

-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
-------------
""")

choice = input("X or O? ").lower()
computer_choice = ""
if choice == "x": computer_choice = "o"
elif choice == "o": computer_choice = "x"

while win(board) != 2 and win(board)!=1 and win(board)!=0:
    location = int(input("Enter the tile number (1-9): ")) - 1
    if board[location] == " " :
        board[location] = choice
        if win(board) == None:
                i = random.randint(0, 8)
                while board[i] != " ":
                    i = random.randint(0, 8)
                else:
                    board[i] = computer_choice
                    print(f"""
-------------
| {board[0]} | {board[1]} | {board[2]} |
-------------
| {board[3]} | {board[4]} | {board[5]} |
-------------
| {board[6]} | {board[7]} | {board[8]} |
-------------
""")
                    continue
    
    else:
        print("Error! You cannot replace an existing tile")


else:
    print(f"""
-------------
| {board[0]} | {board[1]} | {board[2]} |
-------------
| {board[3]} | {board[4]} | {board[5]} |
-------------
| {board[6]} | {board[7]} | {board[8]} |
-------------
""")
    if win(board) == 1:
        print("User Wins! Congratulations!")    
    elif win(board) == 0:
        print("Computer Wins! Better Luck Next Time!")
    elif win(board) == 2:
        print("Draw!")
        