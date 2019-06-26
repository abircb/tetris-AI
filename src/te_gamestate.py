""" GameState is the API to be used by an AutoPlayer """
from te_settings import MAXROW, MAXCOL


class GameState:
    """ GameState maintains the API to be used by an AutoPlayer to communicate with the game """

    def __init__(self, model):
        self.__model = model
        self.__is_a_clone = False

    def get_falling_block_position(self):
        """get_falling_block_position() returns an (x,y) tuple containing the
            position of the current falling block.  (0,0) is at the
            top left of the arena.
        """
        return self.__model.falling_block_position

    def get_falling_block_angle(self):
        """get_falling_block_angle() returns the rotation "angle" of the
            current falling block.  Angle is an integer from 0 to 3,
            increasing clockwise, then wrapping back to zero.
        """
        return self.__model.falling_block_angle

    def get_falling_block_tiles(self):
        """get_falling_block_tiles returns a copy of the current falling
           block's tiles.  This is either a 3x3 or 4x4 list of lists, where 0
           indicates no tile and anything else indicates a tile.

           Most search strategies do not need to know the actual block
           tiles - they only need to know the outcome when the block
           lands, but some more advanced strategies might need this,
           so I've added it based on a feature request.
        """
        tilescopy = self.__model.get_falling_block_tiles()
        return tilescopy

    def get_next_block_tiles(self):
        """get_next_block_tiles returns a copy of the next block's tiles.
           Format is the same as for get_falling_block_tiles().  Most
           search strategies should not need this imformation.
        """
        tilescopy = self.__model.get_next_block_tiles()
        return tilescopy

    def get_falling_block_type(self):
        """get_falling_block_type() returns a str denoting the current
        falling block type I, J, L, O, S, T, Z
        """
        return self.__model.falling_block_type

    def get_next_block_type(self):
        """get_next_block_type() returns a str denoting the current
        falling block type I, J, L, O, S, T, Z
        """
        return self.__model.next_block_type

    def print_block_tiles(self):
        tiles = self.get_falling_block_tiles()
        txt = ""
        size = len(tiles)
        for _y in range(0, size):  # row 0 is the top row
            for _x in range(0, size):  # column 0 is the left column
                if tiles[_y][_x] != 0:  # if there's no tile, the entry is zero
                    txt += "#"
                else:
                    txt += "."
            txt += "\n"
        print(txt)

    def get_tiles(self):
        """get_tiles() returns a copy of the tiles that have settled in the
            arena.  The falling block is not included in these
            tiles. See print_tiles() function for how to interpret the
            list of lists that get_tiles() returns.
        """
        tilescopy = self.__model.get_copy_of_tiles()
        return tilescopy

    def print_tiles(self):
        """print out the current landed tiles - useful for debugging."""
        tiles = self.get_tiles()
        txt = ""
        for _y in range(0, MAXROW):  # row 0 is the top row
            for _x in range(0, MAXCOL):  # column 0 is the left column
                if tiles[_y][_x] != 0:  # if there's no tile, the entry is zero
                    txt += "#"
                else:
                    txt += "."
            txt += "\n"
        print(txt)

    def get_score(self):
        """ get_score() returns the current score, as maintained by the model. """
        return self.__model.score

    def clone(self, is_dummy):
        """clone() will clone the entire game state.
           Any changes made to the cloned state will not affect
           the original model.
        """
        game = GameState(self.__model)
        game._set_model(self.__model.clone(is_dummy), True)
        return game

    def _set_model(self, model, is_a_clone):
        """helper function for clone()"""
        self.__model = model
        self.__is_a_clone = is_a_clone

    def move(self, direction):
        """move() moves the falling block left or right.  If you call move()
           on the original gamestate, the game will update.  If you
           call it on cloned gamestate, the cloned state will update
           but will not affect the actual running game
        """
        self.__model.move(direction)

    def rotate(self, direction):
        """rotate() rotates the falling block left (anticlockwise) or right
           clockwise).  If you call rotate() on the original
           gamestate, the game will update.  If you call it on cloned
           gamestate, the cloned state will update but will not affect
           the actual running game
        """
        self.__model.rotate(direction)

    def update(self):
        # update the game state
        if self.__model.is_dummy:
            (_, landed) = self.__model.update()
            return landed
        return False
