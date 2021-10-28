class Game:
    """
    Class that holds inputed states and prints solution
    """
    def __init__(self,start, heuristic) -> None:
        self.start = start
        self.heuristic = heuristic

    def printSolution(self,node) -> None:
        """
        Helper function to print puzzle solution
        """
        if node.parent is None:
            node.printBoard()
            print()
            return
        else:
            self.printSolution(node.parent)
            node.printBoard()
            print()

if __name__ == "__main__":
    pass

