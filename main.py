import sys

def one():
    max = 1000
    multiples = []

    for i in range(1, max):
        if (i % 3 == 0 or i % 5 == 0):
            multiples.append(i)
            print(i)

    sum = 0
    for j in multiples:
        sum = sum + j

    print(sum)

def two():
    max = 4000000
    fibonacciSeries = [1, 1]

    key = 1
    sum = 0
    while fibonacciSeries[key] <= max:
        nextNumber = fibonacciSeries[key-1] + fibonacciSeries[key]
        fibonacciSeries.append(nextNumber)

        if nextNumber % 2 == 0:
            sum = sum + nextNumber

        key+=1

    print(fibonacciSeries)
    print(sum)

def three():
    n = 600851475143
    primeFactors = []
    i = 2

    while n > 1:
        if n % i == 0:
            factors.append(i)
            n //= i
            i -= 1
        i += 1
    
    print(primeFactors)

def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    print(board)

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

            if (board[row][col] == 0):
                if (player == "X"):
                    board[row][col] = 1
                else:
                    board[row][col] = 2
                i+=1
            else:
                print("This slot is taken fool!")


            print(board)


        
        
if __name__ == '__main__':
    main()