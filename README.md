# CS170 - Project 1: 8-puzzle
## Project Description
This project is an application search and informed search. The objective is to write a program that can solve and 8-puzzle using:
- Uniform Cost Search
- A* with Misplaced Tile heuristic 
- A* with Manhattan Distance heuristic

## Program Description
The code is written in python 3 with the classes:node, game, and the search. The node class is a data structure representing a state in the game. This includes a representation of the puzzle board, parent node, depth, location of the zero, and node cost.The game class holds the initial state of the puzzle and user inputted information. Finally, the search class includes the implemented search algorithm to find a solution. 
As mentioned above, the algorithm used is A* with different heuristics. Repeated and invalid states are ignored during expansion.

## Input and Ouput
Upon running the `main.py` the user may choose to use a defualt puzzle or enter their own. The program will accept any _nxm_ puzzle and then ask the user for the selected algorithm.

If the user chooses to not suppress search information, information about the cost of the node and its board will be printed after each expansion. Otherwise, if a solution is found, the solution depth, number of nodes expanded, and maximum queue size is printed along with the solution. Elapsed search time is outputted but not included in the report.

## Usage
Clone the reposoitory and run `main.py`. Follow the instructions outputted in the console.

