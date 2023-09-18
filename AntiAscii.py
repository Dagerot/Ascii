import sys
import os
import copy


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
            #lines_str = lines_str.strip()
            #if 0 == len(lines_str):  # Empty str?
            #    continue
            _list.append(lines_str)
    return _list


# Check arguments and execute action
# ----------------------------------------
def get_arg_list():
    in_file_path_str = ''
    out_file_path_str = ''
    # Any argument for output name?
    if (1 < len(sys.argv)):
        in_file_path_str = sys.argv[1].strip()
    if (2 < len(sys.argv)):
        out_file_path_str = sys.argv[2].strip()
    return [in_file_path_str, out_file_path_str]


UP_STR              = "Up"
DOWN_STR            = "Down"
LEFT_STR            = "left"
RIGHT_STR           = "right"

TOKEN_SPACE         = " "
TOKEN_LINE_HORZ     = "-"
TOKEN_BOLD_HORZ     = "="
TOKEN_LINE_VERT     = "|"
TOKEN_BOLD_VERT     = "#"
TOKEN_CROSS         = "+"
TOKEN_SMALLER       = "<"
TOKEN_LARGER        = ">"
TOKEN_UP            = "^"
TOKEN_DOWN          = "v"
TOKEN_SOLID         = "¤"
TOKEN_GND           = "£"

ASCII_SPACE                 = " "

ASCII_LINE_HORI             = "─"
ASCII_LINE_VERT             = "│"
ASCII_CROSS                 = "┼"
ASCII_CORN_UP_LEFT          = "┌"
ASCII_CORN_UP_RIGHT         = "┐"
ASCII_CORN_DOWN_LEFT        = "└"
ASCII_CORN_DOWN_RIGHT       = "┘"
ASCII_LINE_HORI_T_DOWN      = "┬"
ASCII_LINE_HORI_T_UPP       = "┴"
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
ASCII_b_LINE_HORI_bT_UPP    = "╩"
ASCII_b_LINE_VERT_bT_LEFT   = "╣"
ASCII_b_LINE_VERT_bT_RIGHT  = "╠"

ASCII_CROSS_HORI_b_VERT     = "╫"
ASCII_CROSS_b_HORI_VERT     = "╪"

ASCII_LINE_HORI_bT_DOWN     = "╥"
ASCII_LINE_HORI_bT_UPP      = "╨"
ASCII_LINE_VERT_bT_LEFT     = "╢"
ASCII_LINE_VERT_bT_RIGHT    = "╟"

ASCII_b_LINE_HORI_T_DOWN     = "╤"
ASCII_b_LINE_HORI_T_UPP      = "╧"
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

block_list = (ASCII_BLOCK_HORIZONTAL_MID, ASCII_BLOCK_VERTICAL)
cross_list = ("┼", "┌", "┐", "└", "┘", "┬", "┴", "┤", "├", "╬", "╔", "╗", "╚", "╝", "╦", "╩", "╣", "╠", "╫", "╪", "╥", "╨", "╢", "╟", "╤", "╧", "╡", "╞", "╒", "╕", "╘", "╛", "╓", "╖", "╙", "╜")

# ----------------------------------------
def anti_ascii_get_pixel(pixel):
    token = pixel
    if pixel in cross_list: token = TOKEN_CROSS
    elif ASCII_ARROW_LEFT == pixel: token = TOKEN_SMALLER
    elif ASCII_ARROW_RIGHT == pixel: token = TOKEN_LARGER
    elif ASCII_ARROW_UP == pixel: token = TOKEN_UP
    elif ASCII_ARROW_DOWN == pixel: token = TOKEN_DOWN
    elif ASCII_LINE_HORI == pixel: token = TOKEN_LINE_HORZ
    elif ASCII_LINE_VERT == pixel: token = TOKEN_LINE_VERT
    elif ASCII_b_LINE_HORI == pixel: token = TOKEN_BOLD_HORZ
    elif ASCII_b_LINE_VERT == pixel: token = TOKEN_BOLD_VERT
    elif pixel in block_list: token = TOKEN_SOLID
    return token


# ----------------------------------------
def pixel_update_get_list(in_list):
    out_list = list()
    row_size = len(in_list)
    # for all rows
    for row_cnt in range(0, row_size):
        in_str = in_list[row_cnt]
        col_size = len(in_str)
        _str = ""
        # for all chars
        for col_cnt in range(0, col_size):
            pixel_old = in_list[row_cnt][col_cnt]
            pixel_new = anti_ascii_get_pixel(pixel_old)
            _str = _str + pixel_new
        out_list.append(_str)
    return out_list


# Read file, clean up, return list
# ----------------------------------------
def clean_up_get_list(file_list):
    '''
    Read in ascii image to matrix (list of rows)
    '''
    _list = list()
    for row in file_list:
        _list.append(row.replace("\n",""))  # Remove [NewLine] token
    return _list


# ----------------------------------------
def convert_get_list(file_path_str):
    _list = parse_file_get_list(file_path_str)
    _list = clean_up_get_list(_list)
    _list = pixel_update_get_list(_list)
    return _list


# ----------------------------------------
def main():
    in_file_str, out_file_str = get_arg_list()
    _list = convert_get_list(in_file_str)

    if 0 == len(out_file_str):
        pos = in_file_str.find(".")
        name_str = in_file_str[:pos]
        ext_str = in_file_str[pos:]
        out_file_str = name_str + "_Ascii" + ext_str

    with open(out_file_str, "w", encoding="'utf-8") as out_file:  # Open output file
        for _str in _list:
            out_file.write(_str + "\n")


# ----------------------------------------
if __name__ == "__main__":
    main()
