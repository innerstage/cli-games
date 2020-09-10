from numpy.random import choice


def check_for_combination(board, a, b, c):
    if board[a-1] == board[b-1] and board[b-1] == board[c-1]:
        return board[a-1]
    else:
        return False


def check_completion(board):
    for i in range(9):
        if board[i] == " ":
            return False
        else:
            return True


def print_board(board):
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("---|---|---")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("\n")


def get_empty(board):
    return [i+1 for i in range(9) if board[i] == " "]
    

def ask_player(board):
    print_board(board)
    print("Empty: ", get_empty(board))
    play = int(input("What's your play?: "))
    board[play-1] = "X"

    return board


def ask_cpu(board):
    play = choice(get_empty(board))
    board[play-1] = "O"
    print("CPU played:", play, "\n")

    return board


def completion(char):
    if char=="O":
        print("GAME OVER")
    elif char=="X":
        print("YOU WIN!")


if __name__ == "__main__":
    completed = False
    board = [" " for i in range(9)]
    COMBINATIONS = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    while(completed==False):
        for c in COMBINATIONS:
            result = check_for_combination(board, c[0], c[1], c[2])
            if result in ["X", "O"]:
                completed = True
                completion(result)
                break
        if completed == True:
            print_board(board)
            break
        
        board = ask_player(board)
        board = ask_cpu(board)