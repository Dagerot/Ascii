'''
confluence - Make better graphics
    +-[Html macro]------------------+
    | <pre class="diagram">         |
    |                               |
    | Ascii image                   |
    |                               |
    | </pre>                        |
    +-------------------------------+

    +-[Html macro]-----------------------------------------------------------+
    | <script>window.markdeepOptions = {mode: 'html'};</script>              |
    | <script src="/download/attachments/26018195/markdeep.min.js"></script> |
    +------------------------------------------------------------------------+

Possible connections
        │[a]│     ◄── Row = y-1
    ────┼───┼────
    [d] │[x]│ [b] ◄── Row = y
    ────┼───┼────
        │[c]│     ◄── Row = y-1
     ▲    ▲    ▲
     │    │    └─ Col = x+1
     │    └─ Col = x
     └─ Col = x-1

Directions
         │ over  │
    ─────┼───────┼─────
    left │   X   │ right
    ─────┼───────┼─────
         │ under │

Connection in each direction can be of type:
    0 = No connection
    1 = Line connection ('-', '|')
    2 = Bold line connection ('=', '#')

    From            To
    -----------     -----------
       │   │           │   │
    ───┼───┼───     ───┼───┼───
       │[|]│           │[|]│
    ───┼───┼───     ───┼───┼───
       │   │           │   │

    From            To                  From            To                  From            To
    -----------     -----------         -----------     -----------         -----------     -----------
       │ - │           │ - │               │ | │           │ | │               │ | │           │ | │
    ───┼───┼───     ───┼───┼───         ───┼───┼───     ───┼───┼───         ───┼───┼───     ───┼───┼───
       │[|]│           │[|]│               │[|]│           │[│]│               │[|]│ -         │[│]│ -
    ───┼───┼───     ───┼───┼───         ───┼───┼───     ───┼───┼───         ───┼───┼───     ───┼───┼───
       │   │           │   │               │   │           │   │               │   │           │   │

    From            To                  From            To                  From            To
    -----------     -----------         -----------     -----------         -----------     -----------
       │ | │           │ | │              │ | │            │ | │              │ | │            │ | │
    ───┼───┼───     ───┼───┼───        ───┼───┼───      ───┼───┼───        ───┼───┼───      ───┼───┼───
       │[+]│ -         │[└]│ -            │[+]│ -   =>     │[├]│ -          - │[+]│ -   =>   - │[┼]│ -
    ───┼───┼───     ───┼───┼───        ───┼───┼───      ───┼───┼───        ───┼───┼───      ───┼───┼───
       │   │           │   │              │ | │            │ | │              │ | │            │ | │

Frames
    Input       Output
    -------     ------
    +-+-+-+     ┌─┬─┬─┐
    +-+-+-+     ├─┼─┼─┤
    +-+-+-+     ├─┼─┼─┤
    +-+-+-+     └─┴─┴─┘

    +--+--+--+  ┌──┬──┬──┐
    |  |  |  |  │  │  │  │
    +--+--+--+  ├──┼──┼──┤
    |  |  |  |  │  │  │  │
    +--+--+--+  ├──┼──┼──┤
    |  |  |  |  │  │  │  │
    +--+--+--+  └──┴──┴──┘

    +==+==+     ╔══╦══╗
    #  #  #     ║  ║  ║
    +==+==+     ╠══╬══╣
    #  #  #     ║  ║  ║
    +==+==+     ╚══╩══╝

    +==+==+     ╔══╤══╗
    #  |  #     ║  │  ║
    +--+--+     ╟──┼──╢
    #  |  #     ║  │  ║
    +==+==+     ╚══╧══╝
'''


# -----------------------------
import sys
import os
import copy
import argparse
import textwrap


# -----------------------------
INDENT_STR = '    '


# ----------------------------------------
class RawFormatter(argparse.HelpFormatter):
    def _fill_text(self, text, width, indent):
        return "\n".join([textwrap.fill(line, width) for line in textwrap.indent(textwrap.dedent(text), indent).splitlines()])


# ----------------------------------------
def file_remove(file_name_str):
    if os.path.isfile(file_name_str):
        try:
            os.remove(file_name_str)
        except:
            print(INDENT_STR + 'Error - Unable to remove file:', file_name_str)
            exit()


# -----------------------------
def open_file_get_lines(filename):
    '''Get lines from a file'''
    encodings = ["utf-8", "iso-8859-1", "ascii"]
    for encoding in encodings:
        with open(filename, encoding=encoding, mode="r") as file:
            try:
                return file.readlines()
            except UnicodeDecodeError:
                # failed to decode, try some other decoding
                pass
    return []


# -----------------------------
def parse_file_get_list(file_path_str):
    _list = list()
    if os.path.isfile(file_path_str):
        for lines_str in open_file_get_lines(file_path_str):  # With all lines in file
            _list.append(lines_str)
    return _list


UP          = 'up'
DOWN        = 'down'
LEFT        = 'left'
RIGHT       = 'right'
UP_LEFT     = 'up_left'
UP_RIGHT    = 'up_right'
DOWN_LEFT   = 'down_left'
DOWN_RIGHT  = 'down_right'


# -----------------------------
class Ascii(object):
    TOKEN_SPACE       = " "
    TOKEN_HORI_LINE   = "-"
    TOKEN_HORI_BOLD   = "="
    TOKEN_HORI_DOTTED = "¨"
    TOKEN_VERT_LINE   = "|"
    TOKEN_VERT_BOLD   = "#"
    TOKEN_VERT_DOTTED = ":"
    TOKEN_CROSS       = "+"
    TOKEN_LEFT        = "<"
    TOKEN_RIGHT       = ">"
    TOKEN_UP          = "^"
    TOKEN_DOWN        = "v"
    TOKEN_SOLID       = "¤"
    TOKEN_GND         = "£"
    TOKEN_GRAPH_UP    = "/"
    TOKEN_GRAPH_DOWN  = "\\"

    ASCII_SPACE                 = " "

    ASCII_LINE_HORI             = "─"
    ASCII_LINE_VERT             = "│"
    ASCII_CROSS                 = "┼"
    ASCII_CORN_UP_LEFT          = "┌"
    ASCII_CORN_UP_RIGHT         = "┐"
    ASCII_CORN_DOWN_LEFT        = "└"
    ASCII_CORN_DOWN_RIGHT       = "┘"
    ASCII_LINE_HORI_T_DOWN      = "┬"
    ASCII_LINE_HORI_T_UP        = "┴"
    ASCII_LINE_VERT_T_LEFT      = "┤"
    ASCII_LINE_VERT_T_RIGHT     = "├"

    ASCII_b_LINE_HORI           = "═"
    ASCII_b_LINE_VERT           = "║"
    ASCII_b_CROSS               = "╬"
    ASCII_b_CORN_UP_LEFT        = "╔"
    ASCII_b_CORN_UP_RIGHT       = "╗"
    ASCII_b_CORN_DOWN_LEFT      = "╚"
    ASCII_b_CORN_DOWN_RIGHT     = "╝"
    ASCII_b_LINE_HORI_bT_DOWN   = "╦"
    ASCII_b_LINE_HORI_bT_UP     = "╩"
    ASCII_b_LINE_VERT_bT_LEFT   = "╣"
    ASCII_b_LINE_VERT_bT_RIGHT  = "╠"

    ASCII_d_LINE_HORI           = "­"  # 0xF0
    ASCII_d_LINE_VERT           = "¦"  # 0xDD
    ASCII_d_CROSS               = "+"
    ASCII_d_CORN_UP_LEFT        = "."
    ASCII_d_CORN_UP_RIGHT       = "."
    ASCII_d_CORN_DOWN_LEFT      = "'"
    ASCII_d_CORN_DOWN_RIGHT     = "'"
    ASCII_d_LINE_HORI_dT_DOWN    = "."
    ASCII_d_LINE_HORI_dT_UP      = "'"
    ASCII_d_LINE_VERT_dT_LEFT    = "¦"  # 0xDD
    ASCII_d_LINE_VERT_dT_RIGHT   = "¦"  # 0xDD

    ASCII_CROSS_HORI_b_VERT     = "╫"
    ASCII_CROSS_b_HORI_VERT     = "╪"

    ASCII_LINE_HORI_bT_DOWN     = "╥"
    ASCII_LINE_HORI_bT_UP       = "╨"
    ASCII_LINE_VERT_bT_LEFT     = "╢"
    ASCII_LINE_VERT_bT_RIGHT    = "╟"

    ASCII_b_LINE_HORI_T_DOWN     = "╤"
    ASCII_b_LINE_HORI_T_UP       = "╧"
    ASCII_b_LINE_VERT_T_LEFT     = "╡"
    ASCII_b_LINE_VERT_T_RIGHT    = "╞"

    ASCII_CORN_UP_b_LEFT         = "╒"
    ASCII_CORN_UP_b_RIGHT        = "╕"
    ASCII_CORN_DOWN_b_LEFT       = "╘"
    ASCII_CORN_DOWN_b_RIGHT      = "╛"
    ASCII_CORN_b_UP_LEFT         = "╓"
    ASCII_CORN_b_UP_RIGHT        = "╖"
    ASCII_CORN_b_DOWN_LEFT       = "╙"
    ASCII_CORN_b_DOWN_RIGHT      = "╜"

    ASCII_ARROW_UP              = "▲"
    ASCII_ARROW_DOWN            = "▼"
    ASCII_ARROW_LEFT            = "◄"
    ASCII_ARROW_RIGHT           = "►"
    ASCII_CONDITION_RIGHT       = "("
    ASCII_CONDITION_LEFT        = ")"
    ASCII_LABLE_RIGHT           = "["
    ASCII_LABLE_LEFT            = "]"
    ASCII_BLOCK_HORIZONTAL_MID  = "■"
    ASCII_BLOCK_VERTICAL        = "█"

    # -----------------------------
    def __init__(self):
        self.data_list = list()
        self.token_arrow_horisontal_list = (self.TOKEN_LEFT, self.TOKEN_RIGHT)
        self.token_arrow_verical_list = (self.TOKEN_UP, self.TOKEN_DOWN)
        self.token_line_horisontal_list = (self.TOKEN_HORI_LINE, self.TOKEN_HORI_BOLD, self.TOKEN_HORI_DOTTED, self.TOKEN_CROSS)
        self.token_line_vertical_list = (self.TOKEN_VERT_LINE, self.TOKEN_VERT_BOLD, self.TOKEN_VERT_DOTTED, self.TOKEN_CROSS)
        self.token_line_list = (self.TOKEN_HORI_LINE, self.TOKEN_VERT_LINE, self.TOKEN_HORI_BOLD, self.TOKEN_VERT_BOLD, self.TOKEN_HORI_DOTTED, self.TOKEN_VERT_DOTTED, self.TOKEN_CROSS)

        self.line_horisontal_cnxn_list   = (self.TOKEN_HORI_LINE  , self.TOKEN_CROSS, self.TOKEN_LEFT, self.TOKEN_RIGHT, self.TOKEN_SOLID)
        self.bold_horisontal_cnxn_list   = (self.TOKEN_HORI_BOLD  , self.TOKEN_CROSS)
        self.dotted_horisontal_cnxn_list = (self.TOKEN_HORI_DOTTED, self.TOKEN_CROSS)
        self.line_verical_cnxn_list      = (self.TOKEN_VERT_LINE  , self.TOKEN_CROSS, self.TOKEN_UP, self.TOKEN_DOWN, self.TOKEN_SOLID, self.TOKEN_GND)
        self.bold_verical_cnxn_list      = (self.TOKEN_VERT_BOLD  , self.TOKEN_CROSS)
        self.dotted_verical_cnxn_list    = (self.TOKEN_VERT_DOTTED, self.TOKEN_CROSS)

        self.cross_connect_vertical_list   = (self.TOKEN_VERT_LINE, self.TOKEN_VERT_BOLD, self.TOKEN_VERT_DOTTED, self.TOKEN_CROSS, self.TOKEN_UP, self.TOKEN_DOWN, self.TOKEN_SOLID, self.TOKEN_GND)
        self.cross_connect_horisontal_list = (self.TOKEN_HORI_LINE, self.TOKEN_HORI_BOLD, self.TOKEN_HORI_DOTTED, self.TOKEN_CROSS, self.TOKEN_LEFT, self.TOKEN_RIGHT, self.TOKEN_SOLID)

        self.ascii_block_list = (self.ASCII_BLOCK_HORIZONTAL_MID, self.ASCII_BLOCK_VERTICAL)
        self.ascii_cross_list = ("┼", "┌", "┐", "└", "┘", "┬", "┴", "┤", "├", "╬", "╔", "╗", "╚", "╝", "╦", "╩", "╣", "╠", "╫", "╪", "╥", "╨", "╢", "╟", "╤", "╧", "╡", "╞", "╒", "╕", "╘", "╛", "╓", "╖", "╙", "╜", "+")

        self.ascii_arrow_cnxn_left_list  = (
            self.TOKEN_HORI_LINE, self.TOKEN_CROSS,
            self.ASCII_LINE_HORI, self.ASCII_CROSS,
            self.ASCII_CORN_UP_LEFT, self.ASCII_CORN_DOWN_LEFT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_HORI_T_UP,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_HORI_b_VERT,
            self.ASCII_LINE_HORI_bT_DOWN, self.ASCII_LINE_HORI_bT_UP, self.ASCII_LINE_VERT_bT_RIGHT,
            self.ASCII_CORN_b_UP_LEFT, self.ASCII_CORN_b_DOWN_LEFT)
        self.ascii_arrow_cnxn_right_list = (
            self.TOKEN_HORI_LINE, self.TOKEN_CROSS,
            self.ASCII_LINE_HORI, self.ASCII_CROSS,
            self.ASCII_CORN_UP_RIGHT, self.ASCII_CORN_DOWN_RIGHT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_HORI_T_UP,
            self.ASCII_LINE_VERT_T_LEFT, self.ASCII_CROSS_HORI_b_VERT,
            self.ASCII_LINE_HORI_bT_DOWN, self.ASCII_LINE_HORI_bT_UP,
            self.ASCII_LINE_VERT_bT_LEFT, self.ASCII_CORN_b_UP_LEFT, self.ASCII_CORN_b_DOWN_LEFT)
        self.ascii_arrow_cnxn_over_list  = (
            self.TOKEN_VERT_LINE, self.TOKEN_CROSS,
            self.ASCII_LINE_VERT, self.ASCII_CROSS,
            self.ASCII_CORN_UP_LEFT, self.ASCII_CORN_UP_RIGHT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_VERT_T_LEFT,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_b_HORI_VERT,
            self.ASCII_b_LINE_HORI_T_DOWN, self.ASCII_b_LINE_VERT_T_LEFT,
            self.ASCII_b_LINE_VERT_T_RIGHT, self.ASCII_CORN_UP_b_LEFT, self.ASCII_CORN_UP_b_RIGHT)
        self.ascii_arrow_cnxn_under_list = (
            self.TOKEN_VERT_LINE, self.TOKEN_CROSS,
            self.ASCII_LINE_VERT, self.ASCII_CROSS,
            self.ASCII_CORN_DOWN_LEFT, self.ASCII_CORN_DOWN_RIGHT,
            self.ASCII_LINE_HORI_T_UP, self.ASCII_LINE_VERT_T_LEFT,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_b_HORI_VERT,
            self.ASCII_b_LINE_HORI_T_UP, self.ASCII_b_LINE_VERT_T_LEFT,
            self.ASCII_b_LINE_VERT_T_RIGHT, self.ASCII_CORN_DOWN_b_LEFT, self.ASCII_CORN_DOWN_b_RIGHT)

        self.ascii_solid_hori_list = (self.TOKEN_SOLID, self.ASCII_BLOCK_HORIZONTAL_MID)

        self.ascii_gnd_cnxn_left_list  = (
            self.TOKEN_HORI_LINE, self.TOKEN_CROSS, self.TOKEN_SOLID,
            self.ASCII_BLOCK_HORIZONTAL_MID, self.ASCII_LINE_HORI,
            self.ASCII_CROSS, self.ASCII_CORN_UP_LEFT, self.ASCII_CORN_DOWN_LEFT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_HORI_T_UP,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_HORI_b_VERT,
            self.ASCII_LINE_HORI_bT_DOWN, self.ASCII_LINE_HORI_bT_UP,
            self.ASCII_LINE_VERT_bT_RIGHT, self.ASCII_CORN_b_UP_LEFT, self.ASCII_CORN_b_DOWN_LEFT)
        self.ascii_gnd_cnxn_right_list = (
            self.TOKEN_HORI_LINE, self.TOKEN_CROSS, self.TOKEN_SOLID,
            self.ASCII_BLOCK_HORIZONTAL_MID, self.ASCII_LINE_HORI,
            self.ASCII_CROSS, self.ASCII_CORN_UP_RIGHT, self.ASCII_CORN_DOWN_RIGHT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_HORI_T_UP,
            self.ASCII_LINE_VERT_T_LEFT, self.ASCII_CROSS_HORI_b_VERT,
            self.ASCII_LINE_HORI_bT_DOWN, self.ASCII_LINE_HORI_bT_UP,
            self.ASCII_LINE_VERT_bT_LEFT, self.ASCII_CORN_b_UP_LEFT, self.ASCII_CORN_b_DOWN_LEFT)
        self.ascii_gnd_cnxn_over_list  = (
            self.TOKEN_VERT_LINE, self.TOKEN_CROSS, self.TOKEN_SOLID,
            self.ASCII_BLOCK_VERTICAL, self.ASCII_LINE_VERT,
            self.ASCII_CROSS, self.ASCII_CORN_UP_LEFT, self.ASCII_CORN_UP_RIGHT,
            self.ASCII_LINE_HORI_T_DOWN, self.ASCII_LINE_VERT_T_LEFT,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_b_HORI_VERT,
            self.ASCII_b_LINE_HORI_T_DOWN, self.ASCII_b_LINE_VERT_T_LEFT,
            self.ASCII_b_LINE_VERT_T_RIGHT, self.ASCII_CORN_UP_b_LEFT, self.ASCII_CORN_UP_b_RIGHT)
        self.ascii_gnd_cnxn_under_list = (
            self.TOKEN_VERT_LINE, self.TOKEN_CROSS, self.TOKEN_SOLID,
            self.ASCII_BLOCK_VERTICAL, self.ASCII_LINE_VERT, self.ASCII_CROSS,
            self.ASCII_CORN_DOWN_LEFT, self.ASCII_CORN_DOWN_RIGHT,
            self.ASCII_LINE_HORI_T_UP, self.ASCII_LINE_VERT_T_LEFT,
            self.ASCII_LINE_VERT_T_RIGHT, self.ASCII_CROSS_b_HORI_VERT,
            self.ASCII_b_LINE_HORI_T_UP, self.ASCII_b_LINE_VERT_T_LEFT,
            self.ASCII_b_LINE_VERT_T_RIGHT, self.ASCII_CORN_DOWN_b_LEFT, self.ASCII_CORN_DOWN_b_RIGHT)


    # -----------------------------
    def clear(self):
        self.data_list = list()

    ## ----------------------------------------
    #def is_token_horizontal(pixel):
    #    token_bool = False
    #    if pixel in self.token_line_horisontal_list:
    #        token_bool = True
    #    return token_bool
    #
    #
    ## ----------------------------------------
    #def is_token_vertical(pixel):
    #    token_bool = False
    #    if pixel in self.token_line_vertical_list
    #        token_bool = True
    #    return token_bool
    #
    #
    ## ----------------------------------------
    #def is_token_cross(pixel):
    #    token_bool = False
    #    if (TOKEN_CROSS == pixel):
    #        token_bool = True
    #    return token_bool
    #
    #
    ## ----------------------------------------
    #def is_token_line(pixel):
    #    token_bool = False
    #    if pixel in self.token_line_list):
    #        token_bool = True
    #    return token_bool
    #
    #
    ## ----------------------------------------
    #def is_token_horisontal_arrow(pixel):
    #    token_bool = False
    #    if pixel in self.token_arrow_horisontal:
    #        token_bool = True
    #    return token_bool
    #
    #
    ## ----------------------------------------
    #def is_token_vertical_arrow(pixel):
    #    token_bool = False
    #    if pixel in self.token_arrow_vertical:
    #        token_bool = True
    #    return token_bool


    # ----------------------------------------
    def pixel_get(self, row, col):
        '''
        In case of pixel out of matrix: Return TOKEN_SPACE
        '''
        row_size = len(self.data_list)
        # within matrix height?
        if (0 <= row ) and (row < row_size):
            col_size = len(str(self.data_list[row]).replace("\n",""))
            # within matrix width?
            if (0 <= col) and (col < col_size):
                pixel = self.data_list[row][col]
            else:
                pixel = self.TOKEN_SPACE
        else:
            pixel = self.TOKEN_SPACE
        return pixel


    # ----------------------------------------
    def pixel_get_over(self, row, col):        return self.pixel_get(row - 1, col)
    def pixel_get_under(self, row, col):       return self.pixel_get(row + 1, col)
    def pixel_get_left(self, row, col):        return self.pixel_get(row, col - 1)
    def pixel_get_right(self, row, col):       return self.pixel_get(row, col + 1)

    def pixel_get_over_left(self, row, col):   return self.pixel_get(row - 1, col - 1)
    def pixel_get_under_left(self, row, col):  return self.pixel_get(row + 1, col - 1)
    def pixel_get_over_right(self, row, col):  return self.pixel_get(row - 1, col + 1)
    def pixel_get_under_right(self, row, col): return self.pixel_get(row + 1, col + 1)


    # ----------------------------------------
    def pixel_surrounding_get_dict(self, row, col, nof):
        '''
                │              │ up[1]    │               │
        ────────┼──────────────┼──────────┼───────────────┼─────────
                │ up_left[0]   │ up[0]    │ up_right[0]   │
        ────────┼──────────────┼──────────┼───────────────┼─────────
        left[1] │ left[0]      │    X     │ right[0]      │ right[1]
        ────────┼──────────────┼──────────┼───────────────┼─────────
                │ down_left[0] │ down[0]  │ down_right[0] │
        ────────┼──────────────┼──────────┼───────────────┼─────────
                │              │ down[1]  │               │

        In case of pixel out of matrix: Return TOKEN_SPACE
        '''
        _dict = dict()
        _dict[UP] = list()
        _dict[DOWN] = list()
        _dict[LEFT] = list()
        _dict[RIGHT] = list()
        _dict[UP_LEFT] = list()
        _dict[UP_RIGHT] = list()
        _dict[DOWN_LEFT] = list()
        _dict[DOWN_RIGHT] = list()

        for cnt in range(0, nof):
            _dict[UP_LEFT].append(    self.pixel_get_over_left  (row - cnt, col - cnt))  # Get pixels up left of actual
            _dict[UP].append(         self.pixel_get_over       (row - cnt, col      ))  # Get pixels over actual
            _dict[UP_RIGHT].append(   self.pixel_get_over_right (row - cnt, col + cnt))  # Get pixels up right of actual
            _dict[LEFT].append(       self.pixel_get_left       (row      , col - cnt))  # Get pixels left of actual
            _dict[RIGHT].append(      self.pixel_get_right      (row      , col + cnt))  # Get pixels right of actual
            _dict[DOWN_LEFT].append(  self.pixel_get_under_left (row + cnt, col - cnt))  # Get pixels down left of actual
            _dict[DOWN].append(       self.pixel_get_under      (row + cnt, col      ))  # Get pixels under actual
            _dict[DOWN_RIGHT].append( self.pixel_get_under_right(row + cnt, col + cnt))  # Get pixels down right of actual
        return _dict


    # ----------------------------------------
    def update_line_to_neighbour_get_pixel(self, pixel, _dict):
        '''
        from    to
        -----   -----
        =       ═
        -       ─
        |       │
        #       ║
        ¨       -
        :       ¦
        '''
        if self.TOKEN_HORI_BOLD == pixel:
            if   _dict[RIGHT][0] in self.bold_horisontal_cnxn_list: pixel = self.ASCII_b_LINE_HORI
            elif _dict[LEFT][0]  in self.bold_horisontal_cnxn_list: pixel = self.ASCII_b_LINE_HORI

        elif self.TOKEN_HORI_LINE == pixel:
            if   _dict[RIGHT][0] in self.line_horisontal_cnxn_list: pixel = self.ASCII_LINE_HORI
            elif _dict[LEFT][0]  in self.line_horisontal_cnxn_list: pixel = self.ASCII_LINE_HORI

        elif self.TOKEN_VERT_BOLD == pixel:
            if   _dict[UP][0]   in self.bold_verical_cnxn_list: pixel = self.ASCII_b_LINE_VERT
            elif _dict[DOWN][0] in self.bold_verical_cnxn_list: pixel = self.ASCII_b_LINE_VERT

        elif self.TOKEN_VERT_LINE == pixel:
            if   _dict[UP][0]   in self.line_verical_cnxn_list: pixel = self.ASCII_LINE_VERT
            elif _dict[DOWN][0] in self.line_verical_cnxn_list: pixel = self.ASCII_LINE_VERT

        elif self.TOKEN_HORI_DOTTED == pixel:
            if   _dict[RIGHT][0] in self.dotted_horisontal_cnxn_list: pixel = self.ASCII_d_LINE_HORI
            elif _dict[LEFT][0]  in self.dotted_horisontal_cnxn_list: pixel = self.ASCII_d_LINE_HORI

        elif self.TOKEN_VERT_DOTTED == pixel:
            if   _dict[UP][0]   in self.dotted_verical_cnxn_list: pixel = self.ASCII_d_LINE_VERT
            elif _dict[DOWN][0] in self.dotted_verical_cnxn_list: pixel = self.ASCII_d_LINE_VERT

        # else: Nothing
        return pixel


    # ----------------------------------------
    def update_cross_to_neighbour_get_pixel(self, pixel, _dict):
        '''
        from    to
        -----   -----
        +       ┌┬┐ ╔╦╗ ╒╤╕ ╓╥╖ .-.-.
                ├┼┤ ╠╬╣ ╞╪╡ ╟╫╢ ¦-+-¦
                └┴┘ ╚╩╝ ╘╧╛ ╙╨╜ '-'-'
        '''

        NONE = 0
        LINE = 1
        BLIN = 2
        DOTS = 3
        CROS = 4

        # ----------------------------------------
        def cross_4_get_pixel(left, right, over, under):
            '''
            + =>
                ┼ ╬ ╪ ╫ +
            '''
            if   (LINE == left) and (LINE == right) and (LINE == over) and (LINE == under): pixel = self.ASCII_CROSS             # ┼
            elif (BLIN == left) and (BLIN == right) and (BLIN == over) and (BLIN == under): pixel = self.ASCII_b_CROSS           # ╬
            elif (DOTS == left) and (DOTS == right) and (DOTS == over) and (DOTS == under): pixel = self.ASCII_d_CROSS           # +
            elif (BLIN == left) and (BLIN == right) and (LINE == over) and (LINE == under): pixel = self.ASCII_CROSS_b_HORI_VERT # ╪
            elif (LINE == left) and (LINE == right) and (BLIN == over) and (BLIN == under): pixel = self.ASCII_CROSS_HORI_b_VERT # ╫
            else: pixel = 0
            return pixel

        # ----------------------------------------
        def cross_3_get_pixel(left, right, over, under):
            '''
             + =>
                Lines:  ┴ ┬ ┤ ├
        ¨       Bold:   ╩ ╦ ╣ ╠
                Dotted: ' . ¦ ¦
                Mixed1: ╨ ╥ ╢ ╟
                Mixed2: ╧ ╤ ╡ ╞
            '''
            if   (LINE == left) and (LINE == right) and (LINE == over)                    : pixel = self.ASCII_LINE_HORI_T_UP       # ┴
            elif (LINE == left) and (LINE == right) and (DOTS == over)                    : pixel = self.ASCII_LINE_HORI_T_UP       # ┴
            elif (LINE == left) and (LINE == right)                    and (DOTS == under): pixel = self.ASCII_LINE_HORI_T_DOWN     # ┬
            elif (LINE == left) and (LINE == right)                    and (LINE == under): pixel = self.ASCII_LINE_HORI_T_DOWN     # ┬
            elif (LINE == left)                     and (LINE == over) and (LINE == under): pixel = self.ASCII_LINE_VERT_T_LEFT     # ┤
            elif (DOTS == left)                     and (LINE == over) and (LINE == under): pixel = self.ASCII_LINE_VERT_T_LEFT     # ┤
            elif                    (LINE == right) and (LINE == over) and (LINE == under): pixel = self.ASCII_LINE_VERT_T_RIGHT    # ├
            elif                    (DOTS == right) and (LINE == over) and (LINE == under): pixel = self.ASCII_LINE_VERT_T_RIGHT    # ├

            elif (BLIN == left) and (BLIN == right) and (BLIN == over)                    : pixel = self.ASCII_b_LINE_HORI_bT_UP    # ╩
            elif (BLIN == left) and (BLIN == right)                    and (BLIN == under): pixel = self.ASCII_b_LINE_HORI_bT_DOWN  # ╦
            elif (BLIN == left)                     and (BLIN == over) and (BLIN == under): pixel = self.ASCII_b_LINE_VERT_bT_LEFT  # ╣
            elif                    (BLIN == right) and (BLIN == over) and (BLIN == under): pixel = self.ASCII_b_LINE_VERT_bT_RIGHT # ╠

            elif (DOTS == left) and (DOTS == right) and (DOTS == over)                    : pixel = self.ASCII_d_LINE_HORI_dT_UP    # '  (dotted ┴)
            elif (DOTS == left) and (DOTS == right) and (LINE == over)                    : pixel = self.ASCII_LINE_HORI_T_UP       # ┴
            elif (DOTS == left) and (DOTS == right) and (BLIN == over)                    : pixel = self.ASCII_LINE_HORI_bT_UP      # ╨
            elif (DOTS == left) and (DOTS == right)                    and (DOTS == under): pixel = self.ASCII_d_LINE_HORI_dT_DOWN  # .  (dotted ┬)
            elif (DOTS == left) and (DOTS == right)                    and (LINE == under): pixel = self.ASCII_LINE_HORI_T_DOWN     # ┬
            elif (DOTS == left) and (DOTS == right)                    and (BLIN == under): pixel = self.ASCII_LINE_HORI_bT_DOWN    # ╥
            elif (DOTS == left)                     and (DOTS == over) and (DOTS == under): pixel = self.ASCII_d_LINE_VERT_dT_LEFT  # ¦  (dotted ┤)
            elif (LINE == left)                     and (DOTS == over) and (DOTS == under): pixel = self.ASCII_LINE_VERT_T_LEFT     # ┤
            elif (BLIN == left)                     and (DOTS == over) and (DOTS == under): pixel = self.ASCII_b_LINE_VERT_T_LEFT   # ╡
            elif                    (DOTS == right) and (DOTS == over) and (DOTS == under): pixel = self.ASCII_d_LINE_VERT_dT_RIGHT # ¦  (dotted ├)
            elif                    (LINE == right) and (DOTS == over) and (DOTS == under): pixel = self.ASCII_LINE_VERT_T_RIGHT    # ├
            elif                    (BLIN == right) and (DOTS == over) and (DOTS == under): pixel = self.ASCII_b_LINE_VERT_T_RIGHT  # ╞

            elif (LINE == left) and (LINE == right) and (BLIN == over)                    : pixel = self.ASCII_LINE_HORI_bT_UP      # ╨
            elif (LINE == left) and (LINE == right) and                    (BLIN == under): pixel = self.ASCII_LINE_HORI_bT_DOWN    # ╥
            elif (LINE == left) and                     (BLIN == over) and (BLIN == under): pixel = self.ASCII_LINE_VERT_bT_LEFT    # ╢
            elif (DOTS == left) and                     (BLIN == over) and (BLIN == under): pixel = self.ASCII_LINE_VERT_bT_LEFT    # ╢
            elif                    (LINE == right) and (BLIN == over) and (BLIN == under): pixel = self.ASCII_LINE_VERT_bT_RIGHT   # ╟
            elif                    (DOTS == right) and (BLIN == over) and (BLIN == under): pixel = self.ASCII_LINE_VERT_bT_RIGHT   # ╟

            elif (BLIN == left) and (BLIN == right) and (LINE == over)                    : pixel = self.ASCII_b_LINE_HORI_T_UP     # ╧
            elif (BLIN == left) and (BLIN == right) and (DOTS == over)                    : pixel = self.ASCII_b_LINE_HORI_T_UP     # ╧
            elif (BLIN == left) and (BLIN == right)                    and (LINE == under): pixel = self.ASCII_b_LINE_HORI_T_DOWN   # ╤
            elif (BLIN == left) and (BLIN == right)                    and (DOTS == under): pixel = self.ASCII_b_LINE_HORI_T_DOWN   # ╤
            elif (BLIN == left)                     and (LINE == over) and (LINE == under): pixel = self.ASCII_b_LINE_VERT_T_LEFT   # ╡
            elif                    (BLIN == right) and (LINE == over) and (LINE == under): pixel = self.ASCII_b_LINE_VERT_T_RIGHT  # ╞

            else: pixel = 0
            return pixel

        # ----------------------------------------
        def cross_2_get_pixel(left, right, over, under):
            '''
             + =>
                Lines:  ┌ ┐ └ ┘
        ¨       Bold:   ╔ ╗ ╚ ╝
                Dotted: . . ' '
                Mixed1: ╓ ╖ ╙ ╜
                Mixed2: ╒ ╕ ╘ ╛
            '''
            if                      (LINE == right)                    and (LINE == under): pixel = self.ASCII_CORN_UP_LEFT         # ┌
            elif (LINE == left)                                        and (LINE == under): pixel = self.ASCII_CORN_UP_RIGHT        # ┐
            elif                    (LINE == right) and (LINE == over)                    : pixel = self.ASCII_CORN_DOWN_LEFT       # └
            elif (LINE == left)                     and (LINE == over)                    : pixel = self.ASCII_CORN_DOWN_RIGHT      # ┘

            elif                    (BLIN == right)                    and (BLIN == under): pixel = self.ASCII_b_CORN_UP_LEFT       # ╔
            elif (BLIN == left)                                        and (BLIN == under): pixel = self.ASCII_b_CORN_UP_RIGHT      # ╗
            elif                    (BLIN == right) and (BLIN == over)                    : pixel = self.ASCII_b_CORN_DOWN_LEFT     # ╚
            elif (BLIN == left)                     and (BLIN == over)                    : pixel = self.ASCII_b_CORN_DOWN_RIGHT    # ╝

            elif                    (DOTS == right)                    and (DOTS == under): pixel = self.ASCII_d_CORN_UP_LEFT       # . (dotted ┌)
            elif (DOTS == left)                                        and (DOTS == under): pixel = self.ASCII_d_CORN_UP_RIGHT      # . (dotted ┐)
            elif                    (DOTS == right) and (DOTS == over)                    : pixel = self.ASCII_d_CORN_DOWN_LEFT     # ' (dotted └)
            elif (DOTS == left)                     and (DOTS == over)                    : pixel = self.ASCII_d_CORN_DOWN_RIGHT    # ' (dotted ┘)

            elif                    (BLIN == right)                    and (LINE == under): pixel = self.ASCII_CORN_UP_b_LEFT       # ╒
            elif (BLIN == left)                                        and (LINE == under): pixel = self.ASCII_CORN_UP_b_RIGHT      # ╕
            elif                    (BLIN == right) and (LINE == over)                    : pixel = self.ASCII_CORN_DOWN_b_LEFT     # ╘
            elif (BLIN == left)                     and (LINE == over)                    : pixel = self.ASCII_CORN_DOWN_b_RIGHT    # ╛

            elif                    (LINE == right)                    and (BLIN == under): pixel = self.ASCII_CORN_b_UP_LEFT       # ╓
            elif (LINE == left)                                        and (BLIN == under): pixel = self.ASCII_CORN_b_UP_RIGHT      # ╖
            elif                    (LINE == right) and (BLIN == over)                    : pixel = self.ASCII_CORN_b_DOWN_LEFT     # ╙
            elif (LINE == left)                     and (BLIN == over)                    : pixel = self.ASCII_CORN_b_DOWN_RIGHT    # ╜

            else: pixel = 0
            return pixel

        if _dict[UP][0] in self.cross_connect_vertical_list:
            if   self.TOKEN_VERT_LINE   == _dict[UP][0]: over = LINE  # Line
            elif self.TOKEN_VERT_BOLD   == _dict[UP][0]: over = BLIN  # Bold
            elif self.TOKEN_VERT_DOTTED == _dict[UP][0]: over = DOTS  # Dotted
            elif self.TOKEN_CROSS       == _dict[UP][0]: over = LINE  # +
            elif self.TOKEN_UP          == _dict[UP][0]: over = LINE  # Line
            elif self.TOKEN_SOLID       == _dict[UP][0]: over = LINE  # Line
            else:                                   over = LINE  # Line
        else: over = 0

        if _dict[DOWN][0] in self.cross_connect_vertical_list:
            if   self.TOKEN_VERT_LINE   == _dict[DOWN][0]: under = LINE  # Line
            elif self.TOKEN_VERT_BOLD   == _dict[DOWN][0]: under = BLIN  # Bold
            elif self.TOKEN_VERT_DOTTED == _dict[DOWN][0]: under = DOTS  # Dotted
            elif self.TOKEN_CROSS       == _dict[DOWN][0]: under = LINE  # +
            elif self.TOKEN_DOWN        == _dict[DOWN][0]: under = LINE  # Line
            elif self.TOKEN_GND         == _dict[DOWN][0]: under = LINE  # Line
            elif self.TOKEN_SOLID       == _dict[DOWN][0]: under = LINE  # Line
            else:                                     under = LINE  # Line
        else: under = 0

        if _dict[LEFT][0] in self.cross_connect_horisontal_list:
            if   self.TOKEN_HORI_LINE   == _dict[LEFT][0]: left = LINE  # Line
            elif self.TOKEN_HORI_BOLD   == _dict[LEFT][0]: left = BLIN  # Bold
            elif self.TOKEN_HORI_DOTTED == _dict[LEFT][0]: left = DOTS  # Dotted
            elif self.TOKEN_CROSS       == _dict[LEFT][0]: left = LINE  # +
            elif self.TOKEN_LEFT        == _dict[LEFT][0]: left = LINE  # Line
            elif self.TOKEN_SOLID       == _dict[LEFT][0]: left = LINE  # Line
            else:                                     left = LINE  # Line
        else: left = 0

        if _dict[RIGHT][0] in self.cross_connect_horisontal_list:
            if   self.TOKEN_HORI_LINE   == _dict[RIGHT][0]: right = LINE  # Line
            elif self.TOKEN_HORI_BOLD   == _dict[RIGHT][0]: right = BLIN  # Bold
            elif self.TOKEN_HORI_DOTTED == _dict[RIGHT][0]: right = DOTS  # Dotted
            elif self.TOKEN_CROSS       == _dict[RIGHT][0]: right = LINE  # +
            elif self.TOKEN_RIGHT       == _dict[RIGHT][0]: right = LINE  # Line
            elif self.TOKEN_SOLID       == _dict[RIGHT][0]: right = LINE  # Line
            else:                                      right = LINE  # Line
        else: right = 0

        pixel_4 = cross_4_get_pixel(left, right, over, under)
        pixel_3 = cross_3_get_pixel(left, right, over, under)
        pixel_2 = cross_2_get_pixel(left, right, over, under)
        if   type(pixel_4) is str: pixel = pixel_4
        elif type(pixel_3) is str: pixel = pixel_3
        elif type(pixel_2) is str: pixel = pixel_2
        # else: Nothing to do
        return pixel


    # ----------------------------------------
    def line_token_to_ascii_get_pixel(self, pixel, _dict):
        '''
        Possible connections
                │[a]│     ◄── Row = y-1
            ────┼───┼────
            [d] │[x]│ [b] ◄── Row = y
            ────┼───┼────
                │[c]│     ◄── Row = y-1
             ▲    ▲    ▲
             │    │    └─ Col = x+1
             │    └─ Col = x
             └─ Col = x-1

        Directions
                 │ over  │
            ─────┼───────┼─────
            left │   X   │ right
            ─────┼───────┼─────
                 │ under │

        Connection in each direction can be of type:
            0 = No connection
            1 = Line connection ('-', '|')
            2 = Bold line connection ('=', '#')
        '''
        if   self.TOKEN_HORI_LINE   == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # "-"
        elif self.TOKEN_HORI_BOLD   == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # "="
        elif self.TOKEN_VERT_LINE   == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # "|"
        elif self.TOKEN_VERT_BOLD   == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # "#"
        elif self.TOKEN_HORI_DOTTED == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # ¨
        elif self.TOKEN_VERT_DOTTED == pixel: pixel = self.update_line_to_neighbour_get_pixel(pixel, _dict)  # :
        elif self.TOKEN_CROSS       == pixel: pixel = self.update_cross_to_neighbour_get_pixel(pixel, _dict) # "+"
        # else: Nothing
        return pixel


    # ----------------------------------------
    def condition_token_to_ascii_get_pixel(self, pixel, _dict):
        '''
        from        to
        -----       -----
        |(text)     ▼(text)
        (text)|     (text)▼
        '''
        line_vert_list = (self.TOKEN_VERT_LINE, self.ASCII_LINE_VERT)

        if   (self.ASCII_CONDITION_RIGHT == _dict[RIGHT][0]) and (pixel in line_vert_list): pixel = self.ASCII_ARROW_DOWN  # ▼(
        elif (self.ASCII_CONDITION_LEFT  == _dict[LEFT][0])  and (pixel in line_vert_list): pixel = self.ASCII_ARROW_DOWN  # )▼

        # else: Nothing
        return pixel


    # ----------------------------------------
    def arrow_token_to_ascii_get_pixel(self, pixel, _dict):
        '''
        from    to
        -----   -----
        ─>      ─►
        <─      ◄─
        |       │
        v       ▼
        ^       ▲
        |       │
        '''
        if   (self.TOKEN_RIGHT == pixel) and (_dict[LEFT][0]  in self.ascii_arrow_cnxn_left_list) : pixel = self.ASCII_ARROW_RIGHT # ─►
        elif (self.TOKEN_LEFT  == pixel) and (_dict[RIGHT][0] in self.ascii_arrow_cnxn_right_list): pixel = self.ASCII_ARROW_LEFT  # ◄─

        elif (self.TOKEN_LEFT  == pixel) and (_dict[LEFT][0]  in self.ascii_arrow_cnxn_left_list) : pixel = self.ASCII_ARROW_LEFT  # ─◄
        elif (self.TOKEN_RIGHT == pixel) and (_dict[RIGHT][0] in self.ascii_arrow_cnxn_right_list): pixel = self.ASCII_ARROW_RIGHT # ►─

        elif (self.TOKEN_LEFT  == pixel) and (self.TOKEN_RIGHT == _dict[RIGHT][0])                : pixel = self.ASCII_ARROW_LEFT  # ◄►
        elif (self.TOKEN_RIGHT == pixel) and (self.TOKEN_LEFT  == _dict[LEFT][0])                 : pixel = self.ASCII_ARROW_RIGHT # ◄►

        elif (self.TOKEN_DOWN  == pixel) and (_dict[UP][0]   in self.ascii_arrow_cnxn_over_list) : pixel = self.ASCII_ARROW_DOWN  # ↓
        elif (self.TOKEN_UP    == pixel) and (_dict[DOWN][0] in self.ascii_arrow_cnxn_under_list): pixel = self.ASCII_ARROW_UP    # ↑

        elif (self.TOKEN_UP    == pixel) and (_dict[UP][0]   in self.ascii_arrow_cnxn_over_list) : pixel = self.ASCII_ARROW_UP   # ↓
        elif (self.TOKEN_DOWN  == pixel) and (_dict[DOWN][0] in self.ascii_arrow_cnxn_under_list): pixel = self.ASCII_ARROW_DOWN  # ↑
        # else: Nothing
        return pixel


    # ----------------------------------------
    def block_token_to_ascii_get_pixel(self, pixel, _dict):
        '''
        from    to
        -----   -----
        #       █

        ##      ■■

        #       █
        #       █
        '''
        if   (self.TOKEN_SOLID == pixel) and (_dict[LEFT][0]  in self.ascii_solid_hori_list): pixel = self.ASCII_BLOCK_HORIZONTAL_MID # ■
        elif (self.TOKEN_SOLID == pixel) and (_dict[RIGHT][0] in self.ascii_solid_hori_list): pixel = self.ASCII_BLOCK_HORIZONTAL_MID # ■

        # special case
        # single ¤ used for knob
        elif (self.TOKEN_SOLID == pixel): pixel = self.ASCII_BLOCK_VERTICAL       # █

        # else: Nothing
        return pixel


    # ----------------------------------------
    def misc_token_to_ascii_get_pixel(self, pixel, _dict):
        '''
        from    to
        -----   -----
        £       ┴   (Ground symbol, vertical capacitor)
        ££      ┤├  (Horizontal capacitor)

        '''
        # special case
        #if (TOKEN_GND == pixel):  pixel = ASCII_LINE_HORI_T_UP # ┴

        if   (self.TOKEN_GND == pixel) and (_dict[LEFT][0]  in self.ascii_gnd_cnxn_left_list):  pixel = self.ASCII_LINE_VERT_T_LEFT  # ┤
        elif (self.TOKEN_GND == pixel) and (_dict[RIGHT][0] in self.ascii_gnd_cnxn_right_list): pixel = self.ASCII_LINE_VERT_T_RIGHT # ├
        elif (self.TOKEN_GND == pixel) and (_dict[UP][0]    in self.ascii_gnd_cnxn_over_list):  pixel = self.ASCII_LINE_HORI_T_UP    # ┴
        elif (self.TOKEN_GND == pixel) and (_dict[DOWN][0]  in self.ascii_gnd_cnxn_under_list): pixel = self.ASCII_LINE_HORI_T_DOWN  # ┬

        # else: Nothing
        return pixel


    # ----------------------------------------
    def pixel_update(self, func):
        out_list = list()
        row_size = len(self.data_list)
        # for all rows
        for row_cnt in range(0, row_size):
            in_str = self.data_list[row_cnt]
            col_size = len(in_str)
            _str = ""
            # for all chars
            for col_cnt in range(0, col_size):
                _dict = self.pixel_surrounding_get_dict(row_cnt, col_cnt, 2)
                pixel_old = self.data_list[row_cnt][col_cnt]
                pixel_new = func(pixel_old, _dict)
                _str = _str + pixel_new
            out_list.append(_str)
        self.data_list = out_list


    # ----------------------------------------
    def clean_up_get_list(self, file_list):
        '''
        Read in ascii image to matrix (list of rows)
        '''
        _list = list()
        for row in file_list:
            _list.append(row.replace("\n",""))  # Remove [NewLine] token
        return _list


    # ----------------------------------------
    def convert_get_list(self, file_path_str):
        _list = parse_file_get_list(file_path_str)
        self.data_list = self.clean_up_get_list(_list)
        self.pixel_update(self.line_token_to_ascii_get_pixel)
        self.pixel_update(self.condition_token_to_ascii_get_pixel)
        self.pixel_update(self.arrow_token_to_ascii_get_pixel)
        self.pixel_update(self.block_token_to_ascii_get_pixel)
        self.pixel_update(self.misc_token_to_ascii_get_pixel)
        return self.data_list


    # ----------------------------------------
    def anti_ascii_get_pixel(self, pixel):
        token = pixel
        if   pixel in self.ascii_cross_list  : token = self.TOKEN_CROSS
        elif self.ASCII_ARROW_LEFT == pixel  : token = self.TOKEN_LEFT
        elif self.ASCII_ARROW_RIGHT == pixel : token = self.TOKEN_RIGHT
        elif self.ASCII_ARROW_UP == pixel    : token = self.TOKEN_UP
        elif self.ASCII_ARROW_DOWN == pixel  : token = self.TOKEN_DOWN
        elif self.ASCII_LINE_HORI == pixel   : token = self.TOKEN_HORI_LINE
        elif self.ASCII_LINE_VERT == pixel   : token = self.TOKEN_VERT_LINE
        elif self.ASCII_b_LINE_HORI == pixel : token = self.TOKEN_HORI_BOLD
        elif self.ASCII_b_LINE_VERT == pixel : token = self.TOKEN_VERT_BOLD
        elif self.ASCII_d_LINE_HORI == pixel : token = self.TOKEN_HORI_DOTTED
        elif self.ASCII_d_LINE_VERT == pixel : token = self.TOKEN_VERT_DOTTED
        elif pixel in self.ascii_block_list  : token = self.TOKEN_SOLID
        return token


    # ----------------------------------------
    def anti_convert_get_list(self, file_path_str):
        _list = parse_file_get_list(file_path_str)
        _list = self.clean_up_get_list(_list)

        out_list = list()
        row_size = len(_list)
        # for all rows
        for row_cnt in range(0, row_size):
            in_str = _list[row_cnt]
            col_size = len(in_str)
            _str = ""
            # for all chars
            for col_cnt in range(0, col_size):
                pixel_old = _list[row_cnt][col_cnt]
                pixel_new = self.anti_ascii_get_pixel(pixel_old)
                _str = _str + pixel_new
            out_list.append(_str)
        return out_list


# ----------------------------------------
def print_to_screen(_list):
    for _str in _list:
       print(_str)


# -----------------------------
_name_ = os.path.basename(sys.argv[0])
_ver_ = '1.0'
_use_ = '%(prog)s -i <input file> -o <output file>'
_note_ = '''
    Genreate UTF-8 graphics from ASCII
'''


# ----------------------------------------
def main():
    obj = Ascii()

    # handle arguments
    parser = argparse.ArgumentParser(
        prog        = _name_,
        usage       = _use_,
        description = _note_, formatter_class = RawFormatter,
    )

    parser.add_argument('-i', '--in_file',    required = True,  type=str, help = 'input file: Usage: -i Xxx.txt')
    parser.add_argument('-o', '--out_file',   required = False, type=str, help = 'output file: Usage: -i Yyy.txt')
    parser.add_argument('-a', '--anti_ascii', required = False, action = 'store_true', help = 'undo ascii conversion')
    parser.add_argument('-v', '--version',                      action = 'version', version = _name_ + ' v' + _ver_)

    args = parser.parse_args()

    in_file_str = str(args.in_file)

    if args.out_file is not None:
        out_file_str = str(args.out_file)
    else:
        pos = in_file_str.find(".")
        name_str = in_file_str[:pos]
        ext_str = in_file_str[pos:]
        out_file_str = name_str + "_Ascii" + ext_str

    print(INDENT_STR + 'In_file:   ' + in_file_str)
    print(INDENT_STR + 'Out_tfile: ' + out_file_str)
    print('')

    print(INDENT_STR + 'Removing: ' + out_file_str)
    file_remove(out_file_str)

    if args.anti_ascii:
        _list = obj.anti_convert_get_list(in_file_str)
    else:
        _list = obj.convert_get_list(in_file_str)

    with open(out_file_str, "w", encoding="'utf-8") as out_file:  # Open output file
        for _str in _list:
            out_file.write(_str + "\n")


# ----------------------------------------
if __name__ == "__main__":
    main()
