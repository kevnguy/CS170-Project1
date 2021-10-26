goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]     
        
class Node:
    def __init__(self, puzzle, cost, depth) -> None:
        self.puzzle = puzzle
        self.cost = cost
        self.depth = depth
        self.children = []
        self.parent

def main():
    print(goal)

if __name__ == "__main__":
    main()
