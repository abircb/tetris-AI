from enum import Enum

#switch this to False to disable autoplaying by default
DEFAULT_AUTOPLAY = True
DISABLE_DISPLAY = False

#main settings
GRID_SIZE = 30
MAXROW = 20
MAXCOL = 10
CANVAS_WIDTH = GRID_SIZE * (7 + MAXCOL)
CANVAS_HEIGHT = GRID_SIZE * (4 + MAXROW)

class Direction(Enum):
    LEFT = -1
    RIGHT = 1
