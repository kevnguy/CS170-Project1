from Node import Node
from Game import Game
from Search import Evaluater
from timeit import default_timer as timer

"""
https://docs.python.org/3/library/heapq.html
https://www.programiz.com/python-programming

8 6 7
2 5 4
3 0 1
31 depth solution
"""
def menu():
    print("Welcome to my scuffed program")
    chooseInput = ''
    heuristicChoice = 1
    inputPuzzle = []
    while True:
        chooseInput = input("Enter 0 to use default puzzle or 1 to input a custom puzzle\n")
        if chooseInput == '1' or chooseInput == '2': 
            break
        else: 
            continue

    if chooseInput == '0':
        inputPuzzle = [[8,6,7],
                       [2,5,4],
                       [3,0,1]]
    else:
        row = int(input("Please enter the number of rows in the puzzle: "))
        col = int(input("Please enter the number of columns in the puzzle: "))
        print("Please enter the rows of your puzzle with 0 representing the blankspace. " +
               "Enter only number, delimit the values with a space, and press enter after each row")
        for i in range(row):
            inputPuzzle.append([int(item) for item in input("Enter {}st row: ".format(i+1)).split()])

    print("\nNext, please choose the desired search heuristic")
    print("[1] A* with no heuristic (Uniform Cost Search)")
    print("[2] A* with Misplaced Tile Heuristic")
    print("[3] A* with Manhattan Distance Heuristic\n")
    heuristicChoice = int(input())-1

    return inputPuzzle, heuristicChoice

def main():
    """
    Main function
    """
    start, heuristic = menu()
    root = Node(start)
    newGame = Game(root, heuristic)
    evaluate = Evaluater(newGame)
    begin = timer()
    solution = evaluate.search()
    end = timer()

    if solution is not None: 
        newGame.printSolution(solution)
        print("Elapsed time: {:4f} seconds".format(end-begin))

if __name__ == "__main__":
    main()