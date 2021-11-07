from Node import Node
from Game import Game
from Search import Evaluater
from timeit import default_timer as timer

"""
Refrences Used
    https://docs.python.org/3/library/1
    https://www.programiz.com/python-programming
"""
def menu():
    print("Welcome to my 8-puzzle program\n")
    inputPuzzle = []
    while True:
        chooseInput = input("Enter 1 to use default puzzle or 2 to input a custom puzzle\n")
        if chooseInput == '1' or chooseInput == '2': 
            break
        else: 
            continue

    if chooseInput == '1':
        # solu 2
        # inputPuzzle = [[1,2,3],
        #                [4,5,6],
        #                [0,7,8]]
        #solu 4
        # inputPuzzle = [[1,2,3],
        #                [5,0,6],
        #                [4,7,8]]
        #solu 8
        # inputPuzzle = [[1,3,6],
        #                [5,0,2],
        #                [4,7,8]]
        #solu 12
        # inputPuzzle = [[1,3,6],
        #                [5,0,7],
        #                [4,8,2]]
        #solu 16
        # inputPuzzle = [[1,6,7],
        #                [5,0,3],
        #                [4,8,2]]
        #solu 20
        # inputPuzzle = [[7,1,2],
        #                [4,8,5],
        #                [6,3,0]]
        #sol 24
        # inputPuzzle = [[0,7,2],
        #                [4,6,1],
        #                [3,5,8]]
        #solu 31
        inputPuzzle = [[8,6,7],
                      [2,5,4],
                      [3,0,1]]
    else:
        row = int(input("\nPlease enter the number of rows in the puzzle: "))
        col = int(input("Please enter the number of columns in the puzzle: "))
        print("Please enter the rows of your puzzle with 0 representing the blank space. ")
        print("Enter only numbers, delimit the values with a space, and press enter after each row")
        for i in range(row):
            inputPuzzle.append([int(item) for item in input("Enter row {}: ".format(i+1)).split()])

    print("\nNext, please choose the desired search heuristic")
    print("[1] A* with no heuristic (Uniform Cost Search)")
    print("[2] A* with Misplaced Tile Heuristic")
    print("[3] A* with Manhattan Distance Heuristic")
    heuristicChoice = int(input())-1

    print("\nWould you like to suppress information about the best node to expand? y/n")
    detail = input()
    if detail == 'y' or detail == 'Y': searchOutput = 0
    else: searchOutput = 1

    return inputPuzzle, heuristicChoice, searchOutput

def main():
    """
    Main function
    """
    start, heuristic, detail = menu()
    root = Node(start)
    newGame = Game(root, heuristic, detail)
    evaluate = Evaluater(newGame)
    begin = timer()
    solution = evaluate.search()
    end = timer()

    if solution is not None: 
        print('\n'+'-'*40)
        newGame.printSolution(solution)
        print("Elapsed time: {:.2f} seconds".format(end-begin))

if __name__ == "__main__":
    main()
