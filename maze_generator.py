from random import randint

class Maze_Generator:
    # Used for displaying the maze...unicode isn't pretty, but it is easy.
    DISPLAY_CHARS = ' ╵╷│╴┘┐┤╶└┌├─┴┬┼'
    DEFAULT_CELL = [1, 1, 1, 1] # Each item represents a connection (right, left, bottom top).

    def __init__(self, size: tuple, start_point: tuple = (0, 0)) -> None:
        self.MAZE_SIZE = size
        # Used for generating.
        self.current_path = [start_point]

        # Initializes the grid as a 2D list of default cells.
        # Each list of cells in the grid actually is a column in the maze, not a row.
        # It's a bit hard to visualize, but the grid is effectively sideways. It's
        # not important right now, but it makes indexing the grid significantly
        # more intuitive down the line.
        self.grid = [
            [self.DEFAULT_CELL for i in range(size[0])]\
            for i in range(size[1])
        ]

    def __repr__(self) -> list:
        return self.decode_grid()
    
    # Takes a maze cell and returns the correct display character
    # based on its connections. This definitely isn't the most intuitive
    # method, so maybe I shouldn't be doing it this way, but I think
    # it's cool and this is a personal project,
    # so I'm sticking with it for now.
    def decode_cell(self, cell: list) -> str:
        # All this does is interpret the four elements in the cell
        # as digits in a binary number, and then converts that binary number
        # to a decimal number between 0 and 15. The string containing all
        # the display characters is written out such that the decimal
        # number is the index of the correct character.
        char_index = int(cell[3]) * 8 + int(cell[2]) * 4 + int(cell[1]) * 2 + int(cell[0])
        return self.DISPLAY_CHARS[char_index]

    # Takes an entire row of cells, decodes each cell into a display character,
    # concatenates them together, and returns the display string
    # for the entire row.
    def decode_row(self, row: list[list]) -> str:
        display_string = ""

        for cell in row:
            display_string += self.decode_cell(cell)

        return display_string

    # Returns display strings for the entire maze grid.
    # The strings still need to be processed some more before
    # actually being displayed, but it's easier to do that in main.
    def decode_grid(self) -> list:
        display_strings = []
        for row in self.grid:
            display_strings.append(self.decode_row(row))
        return display_strings