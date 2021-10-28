class Node:
    """
    Class that represents the puzzle board
    """
    def __init__(self, board, zeroPos=None, parent=None) -> None:
        self.board = board
        self.parent = parent
        if self.parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        if zeroPos is None:
            self.findZero()
        else:
            self.loc_zero = zeroPos
        self.cost = 0

    def findZero(self):
        """ 
        Helper used to locate blankspace (0) in given node
        """
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 0:
                    self.loc_zero = (i,j)

    def printBoard(self) -> None:
        """
        Helper used to print the puzzle board
        """
        for row in self.board:
            for col in row:
                print("{:^2}".format(col), end=' ')
            print()
    
    def __lt__(self, other):
        return (self.cost, self.depth) < (other.cost, other.depth)

    """
    Helper functions to expand states - 4 possible moves
    """
    def moveUp(self):
        i,j =  self.loc_zero
        if i == 0:
            return None
        self.board[i][j], self.board[i - 1][j] = self.board[i - 1][j], self.board[i][j]
        self.loc_zero = (i-1,j)
        return self

    def moveDown(self):
        i,j =  self.loc_zero
        if i == len(self.board)-1:
            return None
        self.board[i][j], self.board[i + 1][j] = self.board[i + 1][j], self.board[i][j]
        self.loc_zero = (i+1,j)
        return self

    def moveLeft(self):
        i,j =  self.loc_zero
        if j == 0:
            return None
        self.board[i][j], self.board[i][j - 1] = self.board[i][j - 1], self.board[i][j]
        self.loc_zero = (i,j-1)
        return self

    def moveRight(self):
        i,j =  self.loc_zero
        if j == len(self.board[0])-1:
            return None
        self.board[i][j], self.board[i][j + 1] = self.board[i][j + 1], self.board[i][j]
        self.loc_zero = (i,j+1)
        return self

if __name__ == "__main__":
    pass