from Coordinate import Coordinate as C
from Move import Move

WHITE = True
BLACK = False
X = 0
Y = 1

class Piece :


    def __init__ (self, board, side, position, movesMade=0) :
        self.board = board
        self.side = side
        self.position = position
        movesMade = 0

    def __str__(self) :
        sideString = 'White' if self.side == WHITE else 'Black'
        return 'Type : ' + type(self).__name__ + ' - Position : ' + str(self.position) + " - Side : " + sideString + ' -- Value : ' + str(self.value)

    def movesInDirectionFromPos(self, pos, direction, side) :
        for dis in range(1, 8) :
            movement = C(dis * direction[X], dis * direction[Y])
            newPos = pos + movement
            if self.board.isValidPos(newPos) :
                pieceAtNewPos = self.board.pieceAtPosition(newPos)
                if pieceAtNewPos is None :
                    yield Move(self, newPos)
                
                elif pieceAtNewPos is not None :
                    if pieceAtNewPos.side != side :
                        yield Move(self, newPos, pieceToCapture = pieceAtNewPos)
                    return
    
    def copy(self) :
        cpy = self.__class__(self.board, self.side, self.position,  movesMade = self.movesMade)
        return cpy
    
    

