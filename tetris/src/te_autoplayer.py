''' Implemented an AI to play tetris '''

from random import Random as rand
from te_settings import Direction

class AutoPlayer():
    def __init__(self, controller):
        self.controller = controller
        self.rand = rand()

        #weights
        self.holesWeight = -8.5
        self.totalHeightWeight = -3
        self.smoothnessWeight = -2.5
        self.completedLinesWeight = 100
        self.rangeWeight = -5.5
        self.maxYWeight = 0
        self.minYWeight = 0
        self.holesNumWeight = -7
        self.rowMovementWeight = -5.5
        self.columnMovementWeight = -6.5
        self.blockHeightWeight = 0

        self.bestPosition = 0
        self.bestAngle = 0
        self.prevY = -1

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        x, y = gamestate.get_falling_block_position()

        if y < self.prevY:
            self.bestPosition, self.bestAngle = self.findbestMoveandRotation(gamestate)
        self.prevY = y

        self.make_move(gamestate, self.bestPosition, self.bestAngle)

    def findbestMoveandRotation(self, gamestate):
        bestPosition = 0
        bestAngle = 0
        bestScore = -10000000000

        for angle in range(0, 4):
            for position in range(-3, 13):
                clone = gamestate.clone(True)

                oldScore = clone.get_score()
                oldTiles = clone.get_tiles()
                while(clone.update() == False):
                    x, y = clone.get_falling_block_position()
                    blockAngle = clone.get_falling_block_angle()

                    if position > x:
                        clone.move(Direction.RIGHT)
                    if position < x:
                        clone.move(Direction.LEFT)

                    if angle == 3 and blockAngle == 0:
                        clone.rotate(Direction.LEFT)
                    elif angle > blockAngle:
                        clone.rotate(Direction.RIGHT)

                #check total height
                heights = self.calculateTotalHeight(clone)
                totalHeight = sum(heights)

                #smoothness
                smoothness = self.calculateSmoothness(heights)

                #holes
                holes = self.calculateHoles(clone)

                #completed Lines
                completedLines = self.calculateCompletedLines(oldScore, clone)

                #Max and Min Y Canvas
                maxYCanvas = max(heights)
                minYCanvas = min(heights)

                #Range
                rangeCanvas = maxYCanvas - minYCanvas

                #num of holes
                holeNum = self.findNumHoles(clone)

                #Row movement
                rowMovement, columnMovement = self.calculateRowAndColumnMovement(clone)

                #block coor
                blockCoor = self.findBlockCoor(clone, oldTiles, completedLines)
                blockHeightMax = max(blockCoor[1])
                blockHeightMin = min(blockCoor[1])
                blockHeightDelta = (blockHeightMax - blockHeightMin)/2
                blockHeight = blockHeightMin + blockHeightDelta

                #Calculating score
                smoothnessScore = (smoothness * self.smoothnessWeight)
                totalHeightScore = (totalHeight * self.totalHeightWeight)
                completedLinesScore = (completedLines * self.completedLinesWeight)
                rangeScore = (self.rangeWeight * rangeCanvas)
                maxY_Score = (self.maxYWeight * maxYCanvas)
                minY_Score = (self.minYWeight * minYCanvas)
                holesNumScore = (self.holesNumWeight * holeNum)
                rowMovementScore = (self.rowMovementWeight * rowMovement)
                columnMovementScore = (self.columnMovementWeight * columnMovement)
                blockHeightScore = (self.blockHeightWeight * blockHeight)

                #excuse the long line
                score = smoothnessScore + totalHeightScore + completedLinesScore + rangeScore + maxY_Score + minY_Score + holesNumScore + rowMovementScore + columnMovementScore + blockHeightScore

                if score > bestScore:
                    bestScore = score
                    bestPosition = position
                    bestAngle = angle

        return (bestPosition, bestAngle)

    def calculateTotalHeight(self, Clone):
        """ Computes the aggregate height; takes the sum of the height of each column
        (the distance from the highest tile in each column to the bottom of the grid)"""
        tiles = Clone.get_tiles()
        columnHeights = []

        for column in range(0, 10):
            for row in range(0, 20):
                if (tiles[row][column] != 0):
                    columnHeights.append(20 - row)
                    break
                elif row == 19:
                    columnHeights.append(0)

        return columnHeights

    def calculateSmoothness(self, heights):
        """ The smoothness of a grid tells us the variation of its column heights. """
        smoothness = 0
        for x in range(len(heights) - 1):
            smoothness += abs(heights[x] - heights[x + 1])
        return smoothness

    def findNumHoles(self, clone):
        tiles = clone.get_tiles()
        numHoles = 0
        for column in range(0, 10):
            counter = 0
            gap = False
            for row in range(0, 20):
                '''if row == 19 and tiles[row][column] == 0 and tiles[row - 1][column] != 0:
                    counter += 1'''
                if gap == True:
                    counter += 1
                if row < 19 and tiles[row][column] != 0 and tiles[row + 1][column] == 0:
                    gap = True
                if row < 19 and tiles[row][column] == 0 and tiles[row + 1][column] != 0:
                    gap = False


            numHoles += counter

        return numHoles

    def calculateRowAndColumnMovement(self, clone):
        tiles = clone.get_tiles()
        rowMovement = 0
        columnMovement = 0

        for column in range(0, 10):
            for row in range(0, 20):
                if (row < 19 and (tiles[row][column] != tiles[row + 1][column]) and (tiles[row][column] == 0 or tiles[row + 1][column] == 0)):
                    columnMovement += 1

        for row in range(0, 20):
            for column in range(0, 10):
                if (column < 9 and (tiles[row][column] != tiles[row][column + 1]) and (tiles[row][column] == 0 or tiles[row][column + 1] == 0)):
                    rowMovement += 1

        return (rowMovement, columnMovement)

    def findMaxYCanvas(self, clone):
        tiles = clone.get_tiles()
        canvasYCoorMax = 0
        blockCoor = []

        for column in range(0, 20):
            for row in range(0, 10):
                if (tiles[row][column] != 0 and y ):
                    canvasYCoorMax = y
                    break
        return canvasYCoorMax

    def findBlockCoor(self, clone, oldTiles, completedLines):
        newTiles = clone.get_tiles()
        blockCoor = []

        for y in range(0, 20):
            for x in range(0, 10):
                if (oldTiles[y][x] != newTiles[y][x]):
                    blockCoor.append((x, y))
        return blockCoor

    def calculateHoles(self, clone):
        """computes the number of 'holes' in the grid. A hole is defined as an empty space such that
        there is at least one tile in the same column above it."""
        tiles = clone.get_tiles()
        holes = 0

        for row in range(0, 20):
            for column in range(0, 10):
                if row < 19 and tiles[row][column] != 0 and tiles[row + 1][column] == 0:
                    holes += 1
        return holes

    def calculateCompletedLines(self, oldscore, clone):
        """ This is probably the most intuitive heuristic among the four. It is simply the
         number of complete lines in a grid. """
        newScore = clone.get_score()
        diff = newScore - oldscore

        if (100 < diff < 130):
            return 1
        elif (400 < diff < 450):
            return 2
        elif (800 < diff < 850):
            return 3
        elif (1600 < diff < 1650):
            return 4
        else:
            return 0

    def make_move(self, gamestate, targetPosition, targetAngle):
        x, y = gamestate.get_falling_block_position()
        angle = gamestate.get_falling_block_angle()

        if targetPosition > x:
            gamestate.move(Direction.RIGHT)
        if targetPosition < x:
            gamestate.move(Direction.LEFT)

        if targetAngle == 3 and angle == 0:
            gamestate.rotate(Direction.LEFT)
        elif targetAngle > angle:
            gamestate.rotate(Direction.RIGHT)
