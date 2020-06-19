import sys

def main():
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

    while True:
        i = 0
        while True:
            if (i%2 != 0):
                player = "O"
            else:
                player = "X"
                
            print("---------Player " + player + "--------------")
            print("Enter Row Number: ")
            row = int(input())
            print("Enter Column Number: ")
            col = int(input())

            if (board[row][col] == " "):
                board[row][col] = player
                i+=1
            else:
                print("This slot is taken fool!")

            printBoard(board)

def printBoard(board):
    i = 0
    print("===========")
    for row in board:
        print(row[0] + " | " + row[1] + " | " + row[2])
        
        if (i < 2):
            print("- + - + -")
        i+=1
    print("===========")

        
        
if __name__ == '__main__':
    main()