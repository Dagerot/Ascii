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
    Input                                                           Output
    -----------------------------------------------------------     -----------------------------------------------------------
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘

    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘


    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘

    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘

    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘

    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ┌┐ ┌─┐ ┌──┐    ┌┬┐ ┌─┬─┐ ┌──┬──┐    ┌┬┬┐ ┌─┬─┬─┐ ┌──┬──┬──┐
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     ├┤ ├─┤ ├──┤    ├┼┤ ├─┼─┤ ├──┼──┤    ├┼┼┤ ├─┼─┼─┤ ├──┼──┼──┤
    || | | |  |    ||| | | | |  |  |    |||| | | | | |  |  |  |     ││ │ │ │  │    │││ │ │ │ │  │  │    ││││ │ │ │ │ │  │  │  │
    ++ +-+ +--+    +++ +-+-+ +--+--+    ++++ +-+-+-+ +--+--+--+     └┘ └─┘ └──┘    └┴┘ └─┴─┘ └──┴──┘    └┴┴┘ └─┴─┴─┘ └──┴──┴──┘


    +--+--+  +==+==+  +==+==+  +--+--+  +==+==+  +--+--+            ┌──┬──┐  ╔══╦══╗  ╒══╤══╕  ╓──╥──╖  ╔══╤══╗  ┌──╥──┐
    |  |  |  #  #  #  |  |  |  #  #  #  #  |  #  |  #  |            │  │  │  ║  ║  ║  │  │  │  ║  ║  ║  ║  │  ║  │  ║  │
    +--+--+  +==+==+  +--+--+  +--+--+  +--+--+  +==+==+            ├──┼──┤  ╠══╬══╣  ╞══╪══╡  ╟──╫──╢  ╟──┼──╢  ╞══╬══╡
    |  |  |  #  #  #  |  |  |  #  #  #  #  |  #  |  #  |            │  │  │  ║  ║  ║  │  │  │  ║  ║  ║  ║  │  ║  │  ║  │
    +--+--+  +==+==+  +==+==+  +--+--+  +==+==+  +--+--+            └──┴──┘  ╚══╩══╝  ╘══╧══╛  ╙──╨──╜  ╚══╧══╝  └──╨──┘

    +-----+  +-----+  +=====+  +=====+  +-----+  +=====+            ┌─────┐  ┌─────┐  ╔═════╗  ╔═════╗  ┌─────┐  ╔═════╗
    |     |  |     |  #     #  #     #  |     |  #     #            │     │  │     │  ║     ║  ║     ║  │     │  ║     ║
    +--+--+  |--+--|  +--+--+  #--+--#  |     |  #     #            ├──┬──┤  │──┬──│  ╟──┬──╢  ║──┬──║  │     │  ║     ║
    |  |  |  |  |  |  #  |  #  #  |  #  |     |  #     #            │  │  │  │  │  │  ║  │  ║  ║  │  ║  │     │  ║     ║
    +--+--+  +--+--+  +==+==+  +==+==+  +-----+  +=====+            └──┴──┘  └──┴──┘  ╚══╧══╝  ╚══╧══╝  └─────┘  ╚═════╝


Condition arrows

    |               │
    |(True)         ▼(True)

    |               │
    | (False)       │ (False)

    |(True)         ▼(True)

    | (False)       | (False)

    +---+           ┌───┐
    +-+-+           └─┬─┘
      |(True)         ▼(True)
    +-+-+           ┌─┴─┐
    +---+           └───┘

    +---+           ┌───┐
    +-+-+           └─┬─┘
      | (False)       │ (False)
    +-+-+           ┌─┴─┐
    +---+           └───┘


Arrows
    ─>              ─►

    <─              ◄─

    |               │
    v               ▼

    ^               ▲
    |               │

    +------------+  ┌────────────┐
    +-+-----+----+  └─┬─────┬────┘
      |  |  ^  ^      │  │  ▲  ▲
      v  v  |  |      ▼  ▼  │  │
    +-+-----+----+  ┌─┴─────┴────┐
    +------------+  └────────────┘

    +------------+  ┌────────────┐
    +-+-----+----+  └─┬─────┬────┘
      v  v  ^  ^      ▼  v  ▲  ^
    +-+-----+----+  ┌─┴─────┴────┐
    +------------+  └────────────┘

    +-+  +-+        ┌─┐  ┌─┐
    | +->+ |        │ ├─►┤ │
    | |  | |        │ │  │ │
    | |->| |        │ │─►│ │
    | |  | |        │ │  │ │
    | +<-+ |        │ ├◄─┤ │
    | |  | |        │ │  │ │
    | |<-| |        │ │◄─│ │
    +-+  +-+        └─┘  └─┘

    +-+ +-+         ┌─┐ ┌─┐
    | +>+ |         │ ├►┤ │
    | | | |         │ │ │ │
    | |>| |         │ │>│ │
    | | | |         │ │ │ │
    | +<+ |         │ ├◄┤ │
    | | | |         │ │ │ │
    | |<| |         │ │<│ │
    +-+ +-+         └─┘ └─┘

Bit ---+↓+-+-+-+-+-+-+-+-+P+-+
    ---+-+-+-+-+-+-+-+-+-+-+↑+-----
        ^ 0 1 2 3 4 5 6 7 ^ ^
 Start -+ |             | | +- Stop
          +----[Data]---+ +- Parity, Even

Bit ───┐↓┌─┬─┬─┬─┬─┬─┬─┬─┐P┌─┐
    ───┴─┴─┴─┴─┴─┴─┴─┴─┴─┴─┘↑└─────
        ▲ 0 1 2 3 4 5 6 7 ▲ ▲
 Start ─┘ │             │ │ └─ Stop
          └────[Data]───┘ └─ Parity, Even

Bars
    ¤       █

    ¤¤      ■■

    ¤       █
    ¤       █

Lines
    -       -
    --      ──

    |       |

    |       │
    |       │

    ¨       -
    ¨¨      --
    :       ¦

    :       ¦
    :       ¦

Special case
    £       ┴

    |       │
   +++     ┌┴┐
   | |     │ │
   +++     └┬┘
    £       ┴

    +-      ┌─
    £       ┴

    ¤       █
    £       ┴

    ££      ┤├

Example
    +=[Main]=========================================================================================================================================+
    # [PcMaster    ] [Pink  ] +-[Unit]-----------------------------------------+ +-[Hw]-----------+ +-[CAN]-------------+ +-[Ethernet]-------------+ #
    # [Swdl        ] [Green ] | +--------------------------------------------+ | | (o) COM        | | Type +----------+ | | +--------------------+ | #
    # [CustVar     ] [Blue  ] | |                                            | | | ( ) CAN-Kvaser | |      | Standard | | | |                    | | #
    # [Log         ] [Yellow] | |                                            | | | ( ) Ethernet   | |      +----------+ | | |                    | | #
    # [SwStatus    ] [Gray  ] | |                                            | | +----------------+ |      | Extended | | | |                    | | #
    # [Oscilloscope]          | |                                            | |                    |      +----------+ | | |                    | | #
    # [HwTest      ]          | |                                            | | +-[Settings]-----+ | ID Tx   [_______] | | |                    | | #
    # [Graph       ]          | |                                            | | | [Port] [_____] | | ID Rx   [_______] | | |                    | | #
    # [Settings    ]          | |                                            | | | Speed  [_____] | | Rx mask [_______] | | |                    | | #
    # [Com log     ]          | |                                            | | |                | |                   | | |                    | | #
    #                         | +--------------------------------------------+ | | Panel lock [ ] | |                   | | +--------------------+ | #
    #                         | [Scan for units] [x] Default timing [_____] ms | | Activate   [x] | |                   | | [Scan for IP]          | #
    # [Exec external]         |                  [x] Dec                       | |                | |                   | | [__.__.__.__] [Add IP] | #
    #                         +------------------------------------------------+ +----------------+ +-------------------+ +------------------------+ #
    # ¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤ # <-- ¤¤¤ = ProgressBar
    # [____________________________________________________________________________________________________________________________________________] # <-- Status text
    +================================================================================================================================================+

    ╔═[Main]═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
    ║ [PcMaster    ] [Pink  ] ┌─[Unit]─────────────────────────────────────────┐ ┌─[Hw]───────────┐ ┌─[CAN]─────────────┐ ┌─[Ethernet]─────────────┐ ║
    ║ [Swdl        ] [Green ] │ ┌────────────────────────────────────────────┐ │ │ (o) COM        │ │ Type ┌──────────┐ │ │ ┌────────────────────┐ │ ║
    ║ [CustVar     ] [Blue  ] │ │                                            │ │ │ ( ) CAN-Kvaser │ │      │ Standard │ │ │ │                    │ │ ║
    ║ [Log         ] [Yellow] │ │                                            │ │ │ ( ) Ethernet   │ │      ├──────────┤ │ │ │                    │ │ ║
    ║ [SwStatus    ] [Gray  ] │ │                                            │ │ └────────────────┘ │      │ Extended │ │ │ │                    │ │ ║
    ║ [Oscilloscope]          │ │                                            │ │                    │      └──────────┘ │ │ │                    │ │ ║
    ║ [HwTest      ]          │ │                                            │ │ ┌─[Settings]─────┐ │ ID Tx   [_______] │ │ │                    │ │ ║
    ║ [Graph       ]          │ │                                            │ │ │ [Port] [_____] │ │ ID Rx   [_______] │ │ │                    │ │ ║
    ║ [Settings    ]          │ │                                            │ │ │ Speed  [_____] │ │ Rx mask [_______] │ │ │                    │ │ ║
    ║ [Com log     ]          │ │                                            │ │ │                │ │                   │ │ │                    │ │ ║
    ║                         │ └────────────────────────────────────────────┘ │ │ Panel lock [ ] │ │                   │ │ └────────────────────┘ │ ║
    ║                         │ [Scan for units] [x] Default timing [_____] ms │ │ Activate   [x] │ │                   │ │ [Scan for IP]          │ ║
    ║ [Exec external]         │                  [x] Dec                       │ │                │ │                   │ │ [__.__.__.__] [Add IP] │ ║
    ║                         └────────────────────────────────────────────────┘ └────────────────┘ └───────────────────┘ └────────────────────────┘ ║
    ║ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ ║ <-- ■■■ = ProgressBar
    ║ [____________________________________________________________________________________________________________________________________________] ║ <-- Status text
    ╚════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
'''


import sys
import os
import copy


# Open file for read and get handle
# ----------------------------------------
#def load_file_get_handle(file_path_str):
#    try:
#        handle = open(file_path_str, "r", encoding='utf-8')
#    except File_UnableToOpenFile:
#        print("File not found:" + file_path_str)
#        handle = None
#        quit()
#    return handle


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


# Open file for write and get handle
# ----------------------------------------
#def save_file_get_handle(file_path_str):
#    try:
#        handle = open(file_path_str, "w", encoding='utf-8')
#    except File_UnableToOpenCreateFile:
#        print("Unable to open/create file:" + file_path_str)
#        handle = None
#        quit()
#    return handle


# -----------------------------
#def extract_arg_get_list():
#    '''list of input files from inline arguments'''
#    _list = list()
#    if (1 < len(sys.argv)):
#        # For all arguments (except program call)
#        for cnt in range(1, len(sys.argv)):
#            s = sys.argv[cnt].strip()
#            _list.append(s)
#    return _list


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


UP_STR            = "Up"
DOWN_STR          = "Down"
LEFT_STR          = "left"
RIGHT_STR         = "right"

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

ASCII_d_LINE_HORI           = "-"
ASCII_d_LINE_VERT           = "¦"
ASCII_d_CROSS               = "+"
ASCII_d_CORN_UP_LEFT        = "."
ASCII_d_CORN_UP_RIGHT       = "."
ASCII_d_CORN_DOWN_LEFT      = "'"
ASCII_d_CORN_DOWN_RIGHT     = "'"
ASCII_d_LINE_HORI_dT_DOWN    = "."
ASCII_d_LINE_HORI_dT_UP      = "'"
ASCII_d_LINE_VERT_dT_LEFT    = "¦"
ASCII_d_LINE_VERT_dT_RIGHT   = "¦"

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


# Is this pixel a horizontal token?
# ----------------------------------------
def is_token_horizontal(pixel):
    token_bool = False
    if (TOKEN_HORI_LINE == pixel) or (TOKEN_HORI_BOLD == pixel):
        token_bool = True
    return token_bool


# Is this pixel a vertical token?
# ----------------------------------------
def is_token_vertical(pixel):
    token_bool = False
    if (TOKEN_VERT_LINE == pixel) or (TOKEN_VERT_BOLD == pixel):
        token_bool = True
    return token_bool


# Is this pixel a cross token?
# ----------------------------------------
def is_token_cross(pixel):
    token_bool = False
    if (TOKEN_CROSS == pixel):
        token_bool = True
    return token_bool


# Is this pixel a line token?
# ----------------------------------------
def is_token(pixel):
    token_bool = False
    if (TOKEN_HORI_LINE == pixel) or (TOKEN_VERT_LINE == pixel):
        token_bool = True
    if (TOKEN_HORI_BOLD == pixel) or (TOKEN_VERT_BOLD == pixel):
        token_bool = True
    if (TOKEN_CROSS == pixel):
        token_bool = True
    return token_bool


# Is this pixel a horisontal arrow?
# ----------------------------------------
def is_token_horisontal_arrow(pixel):
    token_bool = False
    if (TOKEN_LEFT == pixel) or (TOKEN_RIGHT == pixel):
        token_bool = True
    return token_bool


# Is this pixel a vertical arrow?
def is_token_vertical_arrow(pixel):
    token_bool = False
    if (TOKEN_UP == pixel) or (TOKEN_DOWN == pixel):
        token_bool = True
    return token_bool


# Get pixel
# ----------------------------------------
def pixel_get(_list, row, col):
    '''
    In case of pixel out of matrix: Return TOKEN_SPACE
    '''
    row_size = len(_list)
    # within matrix height?
    if (0 <= row ) and (row < row_size):
        col_size = len(str(_list[row]).replace("\n",""))
        # within matrix width?
        if (0 <= col) and (col < col_size):
            pixel = _list[row][col]
        else:
            pixel = TOKEN_SPACE
    else:
        pixel = TOKEN_SPACE
    return pixel



# Get pixel over actual
# ----------------------------------------
def pixel_get_over(_list, row, col):
    '''
    ┼──────────┼
    │ over[0]  │
    ┼──────────┼
    │    X     │
    ┼──────────┼
    '''
    return pixel_get(_list, row - 1, col)


# Get pixel under actual
# ----------------------------------------
def pixel_get_under(_list, row, col):
    '''
    ┼──────────┼
    │    X     │
    ┼──────────┼
    │ under[0] │
    ┼──────────┼
    In case of pixel out of matrix: Return TOKEN_SPACE
    '''
    return pixel_get(_list, row + 1, col)


# Get pixel left of actual
# ----------------------------------------
def pixel_get_left(_list, row, col):
    '''
    ┼─────────┼──────────┼
    │ left[0] │    X     │
    ┼─────────┼──────────┼

    In case of pixel out of matrix: Return TOKEN_SPACE
    '''
    return pixel_get(_list, row, col - 1)


# Get pixel right of actual
# ----------------------------------------
def pixel_get_right(_list, row, col):
    '''
    ┼──────────┼──────────
    │    X     │ right[0]
    ┼──────────┼──────────

    In case of pixel out of matrix: Return TOKEN_SPACE
    '''
    return pixel_get(_list, row, col + 1)


# Get surrounding pixels
# ----------------------------------------
def pixel_surrounding_get_list(_list, row, col, nof):
    '''
            │         │ over[1]  │          │
    ────────┼─────────┼──────────┼──────────┼─────────
            │         │ over[0]  │          │
    ────────┼─────────┼──────────┼──────────┼─────────
    left[1] │ left[0] │    X     │ right[0] │ right[1]
    ────────┼─────────┼──────────┼──────────┼─────────
            │         │ under[0] │          │
    ────────┼─────────┼──────────┼──────────┼─────────
            │         │ under[1] │          │

    In case of pixel out of matrix: Return TOKEN_SPACE
    '''
    over_list = list()
    under_list = list()
    left_list = list()
    right_list = list()

    for cnt in range(0, nof):
        over_list.append(pixel_get_over(  _list, row - cnt, col      ))  # Get pixels over actual
        under_list.append(pixel_get_under(_list, row + cnt, col      ))  # Get pixels under actual
        left_list.append(pixel_get_left(  _list, row      , col - cnt))  # Get pixels left of actual
        right_list.append(pixel_get_right(_list, row      , col + cnt))  # Get pixels right of actual
    return (over_list, under_list, left_list, right_list)


# ----------------------------------------
def connect_horisontal_line(pixel):   return (TOKEN_HORI_LINE   == pixel) or (TOKEN_CROSS == pixel) or (TOKEN_LEFT == pixel) or (TOKEN_RIGHT == pixel) or (TOKEN_SOLID == pixel)
def connect_horisontal_bold(pixel):   return (TOKEN_HORI_BOLD   == pixel) or (TOKEN_CROSS == pixel)
def connect_horisontal_dotted(pixel): return (TOKEN_HORI_DOTTED == pixel) or (TOKEN_CROSS == pixel)
def connect_vertical_line(pixel):     return (TOKEN_VERT_LINE   == pixel) or (TOKEN_CROSS == pixel) or (TOKEN_UP   == pixel) or (TOKEN_DOWN  == pixel) or (TOKEN_SOLID == pixel) or (TOKEN_GND == pixel)
def connect_vertical_bold(pixel):     return (TOKEN_VERT_BOLD   == pixel) or (TOKEN_CROSS == pixel)
def connect_vertical_dotted(pixel):   return (TOKEN_VERT_DOTTED == pixel) or (TOKEN_CROSS == pixel)


# ----------------------------------------
def update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list):
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
    if TOKEN_HORI_BOLD == pixel:
        if   connect_horisontal_bold(right_list[0]): pixel = ASCII_b_LINE_HORI
        elif connect_horisontal_bold(left_list[0]):  pixel = ASCII_b_LINE_HORI

    elif TOKEN_HORI_LINE == pixel:
        if   connect_horisontal_line(right_list[0]): pixel = ASCII_LINE_HORI
        elif connect_horisontal_line(left_list[0]):  pixel = ASCII_LINE_HORI

    elif TOKEN_VERT_BOLD == pixel:
        if   connect_vertical_bold(over_list[0]):  pixel = ASCII_b_LINE_VERT
        elif connect_vertical_bold(under_list[0]): pixel = ASCII_b_LINE_VERT

    elif TOKEN_VERT_LINE == pixel:
        if   connect_vertical_line(over_list[0]):  pixel = ASCII_LINE_VERT
        elif connect_vertical_line(under_list[0]): pixel = ASCII_LINE_VERT

    elif TOKEN_HORI_DOTTED == pixel:
        if   connect_horisontal_dotted(right_list[0]): pixel = ASCII_d_LINE_HORI
        elif connect_horisontal_dotted(left_list[0]):  pixel = ASCII_d_LINE_HORI

    elif TOKEN_VERT_DOTTED == pixel:
        if   connect_vertical_dotted(over_list[0]):  pixel = ASCII_d_LINE_VERT
        elif connect_vertical_dotted(under_list[0]): pixel = ASCII_d_LINE_VERT

    # else: Nothing
    return pixel


# ----------------------------------------
def connect_horisontal(pixel):  return (TOKEN_HORI_LINE == pixel) or (TOKEN_HORI_BOLD == pixel) or (TOKEN_HORI_DOTTED == pixel) or (TOKEN_CROSS == pixel) or (TOKEN_LEFT == pixel) or (TOKEN_RIGHT == pixel) or (TOKEN_SOLID == pixel)
def connect_vertical(pixel):    return (TOKEN_VERT_LINE == pixel) or (TOKEN_VERT_BOLD == pixel) or (TOKEN_VERT_DOTTED == pixel) or (TOKEN_CROSS == pixel) or (TOKEN_UP   == pixel) or (TOKEN_DOWN  == pixel) or (TOKEN_SOLID == pixel) or (TOKEN_GND == pixel)


# ----------------------------------------
def update_cross_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list):
    '''
    from    to
    -----   -----
    +       ┌┬┐ ╔╦╗ ╒╤╕ ╓╥╖ .-.-.
            ├┼┤ ╠╬╣ ╞╪╡ ╟╫╢ ¦-+-¦
            └┴┘ ╚╩╝ ╘╧╛ ╙╨╜ '-'-'
    '''

    if connect_vertical(over_list[0]):
        if   TOKEN_VERT_LINE   == over_list[0]: over = 1  # Line
        elif TOKEN_VERT_BOLD   == over_list[0]: over = 2  # Bold
        elif TOKEN_VERT_DOTTED == over_list[0]: over = 3  # Dotted
        elif TOKEN_UP          == over_list[0]: over = 1  # Line
        elif TOKEN_SOLID       == over_list[0]: over = 1  # Line
        else:                                   over = 1  # Line
    else: over = 0

    if connect_vertical(under_list[0]):
        if   TOKEN_VERT_LINE   == under_list[0]: under = 1  # Line
        elif TOKEN_VERT_BOLD   == under_list[0]: under = 2  # Bold
        elif TOKEN_VERT_DOTTED == under_list[0]: under = 3  # Dotted
        elif TOKEN_DOWN        == under_list[0]: under = 1  # Line
        elif TOKEN_GND         == under_list[0]: under = 1  # Line
        elif TOKEN_SOLID       == under_list[0]: under = 1  # Line
        else:                                    under = 1  # Line
    else: under = 0

    if connect_horisontal(left_list[0]):
        if   TOKEN_HORI_LINE   == left_list[0]: left = 1  # Line
        elif TOKEN_HORI_BOLD   == left_list[0]: left = 2  # Bold
        elif TOKEN_HORI_DOTTED == left_list[0]: left = 3  # Dotted
        elif TOKEN_LEFT        == left_list[0]: left = 1  # Line
        elif TOKEN_SOLID       == left_list[0]: left = 1  # Line
        else:                                   left = 1  # Line
    else: left = 0

    if connect_horisontal(right_list[0]):
        if   TOKEN_HORI_LINE   == right_list[0]: right = 1  # Line
        elif TOKEN_HORI_BOLD   == right_list[0]: right = 2  # Bold
        elif TOKEN_HORI_DOTTED == right_list[0]: right = 3  # Dotted
        elif TOKEN_RIGHT       == right_list[0]: right = 1  # Line
        elif TOKEN_SOLID       == right_list[0]: right = 1  # Line
        else:                                    right = 1  # Line
    else: right = 0

    if   (1 == left) and (1 == right) and (1 == over) and (1 == under): pixel = ASCII_CROSS                # ┼
    elif (1 == left) and (1 == right) and (1 == over)                 : pixel = ASCII_LINE_HORI_T_UP       # ┴
    elif (1 == left) and (1 == right)                 and (1 == under): pixel = ASCII_LINE_HORI_T_DOWN     # ┬
    elif (1 == left)                  and (1 == over) and (1 == under): pixel = ASCII_LINE_VERT_T_LEFT     # ┤
    elif                 (1 == right) and (1 == over) and (1 == under): pixel = ASCII_LINE_VERT_T_RIGHT    # ├
    elif (0 == left) and (1 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_LEFT         # ┌
    elif (1 == left) and (0 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_RIGHT        # ┐
    elif (0 == left) and (1 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_LEFT       # └
    elif (1 == left) and (0 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_RIGHT      # ┘


    elif (3 == left) and (1 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_LEFT         # ┌
    elif (1 == left) and (3 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_RIGHT        # ┐
    elif (3 == left) and (1 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_LEFT       # └
    elif (1 == left) and (3 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_RIGHT      # ┘

    elif (0 == left) and (1 == right) and (3 == over) and (1 == under): pixel = ASCII_CORN_UP_LEFT         # ┌
    elif (1 == left) and (0 == right) and (3 == over) and (1 == under): pixel = ASCII_CORN_UP_RIGHT        # ┐
    elif (0 == left) and (1 == right) and (1 == over) and (3 == under): pixel = ASCII_CORN_DOWN_LEFT       # └
    elif (1 == left) and (0 == right) and (1 == over) and (3 == under): pixel = ASCII_CORN_DOWN_RIGHT      # ┘

    elif (3 == left) and (1 == right) and (3 == over) and (1 == under): pixel = ASCII_CORN_UP_LEFT         # ┌
    elif (1 == left) and (3 == right) and (3 == over) and (1 == under): pixel = ASCII_CORN_UP_RIGHT        # ┐
    elif (3 == left) and (1 == right) and (1 == over) and (3 == under): pixel = ASCII_CORN_DOWN_LEFT       # └
    elif (1 == left) and (3 == right) and (1 == over) and (3 == under): pixel = ASCII_CORN_DOWN_RIGHT      # ┘


    elif (2 == left) and (2 == right) and (2 == over) and (2 == under): pixel = ASCII_b_CROSS              # ╬
    elif (2 == left) and (2 == right) and (2 == over)                 : pixel = ASCII_b_LINE_HORI_bT_UP    # ╩
    elif (2 == left) and (2 == right)                 and (2 == under): pixel = ASCII_b_LINE_HORI_bT_DOWN  # ╦
    elif (2 == left)                  and (2 == over) and (2 == under): pixel = ASCII_b_LINE_VERT_bT_LEFT  # ╣
    elif                 (2 == right) and (2 == over) and (2 == under): pixel = ASCII_b_LINE_VERT_bT_RIGHT # ╠
    elif (0 == left) and (2 == right) and (0 == over) and (2 == under): pixel = ASCII_b_CORN_UP_LEFT       # ╔
    elif (2 == left) and (0 == right) and (0 == over) and (2 == under): pixel = ASCII_b_CORN_UP_RIGHT      # ╗
    elif (0 == left) and (2 == right) and (2 == over) and (0 == under): pixel = ASCII_b_CORN_DOWN_LEFT     # ╚
    elif (2 == left) and (0 == right) and (2 == over) and (0 == under): pixel = ASCII_b_CORN_DOWN_RIGHT    # ╝

    elif (3 == left) and (3 == right) and (3 == over) and (3 == under): pixel = ASCII_d_CROSS              # +
    elif (3 == left) and (3 == right) and (3 == over)                 : pixel = ASCII_d_LINE_HORI_dT_UP    # '  (┴)
    elif (3 == left) and (3 == right)                 and (3 == under): pixel = ASCII_d_LINE_HORI_dT_DOWN  # .  (┬)
    elif (3 == left)                  and (3 == over) and (3 == under): pixel = ASCII_d_LINE_VERT_dT_LEFT  # ¦  (┤)
    elif                 (3 == right) and (3 == over) and (3 == under): pixel = ASCII_d_LINE_VERT_dT_RIGHT # ¦  (├)
    elif (0 == left) and (3 == right) and (0 == over) and (3 == under): pixel = ASCII_d_CORN_UP_LEFT       # .  (┌)
    elif (3 == left) and (0 == right) and (0 == over) and (3 == under): pixel = ASCII_d_CORN_UP_RIGHT      # .  (┐)
    elif (0 == left) and (3 == right) and (3 == over) and (0 == under): pixel = ASCII_d_CORN_DOWN_LEFT     # '  (└)
    elif (3 == left) and (0 == right) and (3 == over) and (0 == under): pixel = ASCII_d_CORN_DOWN_RIGHT    # '  (┘)

    elif (1 == left) and (1 == right) and (2 == over) and (2 == under): pixel = ASCII_CROSS_HORI_b_VERT    # ╫
    elif (2 == left) and (2 == right) and (1 == over) and (1 == under): pixel = ASCII_CROSS_b_HORI_VERT    # ╪

    elif (1 == left) and (1 == right) and (0 == over) and (2 == under): pixel = ASCII_LINE_HORI_bT_DOWN    # ╥
    elif (1 == left) and (1 == right) and (2 == over) and (0 == under): pixel = ASCII_LINE_HORI_bT_UP      # ╨
    elif (1 == left) and (0 == right) and (2 == over) and (2 == under): pixel = ASCII_LINE_VERT_bT_LEFT    # ╢
    elif (0 == left) and (1 == right) and (2 == over) and (2 == under): pixel = ASCII_LINE_VERT_bT_RIGHT   # ╟

    elif (2 == left) and (2 == right) and (0 == over) and (1 == under): pixel = ASCII_b_LINE_HORI_T_DOWN   # ╤
    elif (2 == left) and (2 == right) and (1 == over) and (0 == under): pixel = ASCII_b_LINE_HORI_T_UP     # ╧
    elif (2 == left) and (0 == right) and (1 == over) and (1 == under): pixel = ASCII_b_LINE_VERT_T_LEFT   # ╡
    elif (0 == left) and (2 == right) and (1 == over) and (1 == under): pixel = ASCII_b_LINE_VERT_T_RIGHT  # ╞

    elif (0 == left) and (2 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_b_LEFT       # ╒
    elif (2 == left) and (0 == right) and (0 == over) and (1 == under): pixel = ASCII_CORN_UP_b_RIGHT      # ╕
    elif (0 == left) and (2 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_b_LEFT     # ╘
    elif (2 == left) and (0 == right) and (1 == over) and (0 == under): pixel = ASCII_CORN_DOWN_b_RIGHT    # ╛

    elif (0 == left) and (1 == right) and (0 == over) and (2 == under): pixel = ASCII_CORN_b_UP_LEFT       # ╓
    elif (1 == left) and (0 == right) and (0 == over) and (2 == under): pixel = ASCII_CORN_b_UP_RIGHT      # ╖
    elif (0 == left) and (1 == right) and (2 == over) and (0 == under): pixel = ASCII_CORN_b_DOWN_LEFT     # ╙
    elif (1 == left) and (0 == right) and (2 == over) and (0 == under): pixel = ASCII_CORN_b_DOWN_RIGHT    # ╜

    # special case - Y-axix
    #elif (1 == left) and (1 == right) and (0 == over) and (0 == under): pixel = ASCII_CROSS                # ┼
    #elif (0 == left) and (0 == right) and (1 == over) and (1 == under): pixel = ASCII_CROSS                # ┼
    elif                                  (1 == over) and (1 == under): pixel = ASCII_CROSS                # ┼

    # special case - Bold corners mixed with lines
    elif                 (2 == right)                 and (2 == under): pixel = ASCII_b_CORN_UP_LEFT       # ╔
    elif (2 == left)                                  and (2 == under): pixel = ASCII_b_CORN_UP_RIGHT      # ╗
    elif                 (2 == right) and (2 == over)                 : pixel = ASCII_b_CORN_DOWN_LEFT     # ╚
    elif (2 == left)                  and (2 == over)                 : pixel = ASCII_b_CORN_DOWN_RIGHT    # ╝

    # else: Nothing
    return pixel


# ----------------------------------------
def line_token_to_ascii_get_pixel(pixel, over_list, under_list, right_list, left_list):
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
    if   TOKEN_HORI_LINE   == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # "-"
    elif TOKEN_HORI_BOLD   == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # "="
    elif TOKEN_VERT_LINE   == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # "|"
    elif TOKEN_VERT_BOLD   == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # "#"
    elif TOKEN_HORI_DOTTED == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # ¨
    elif TOKEN_VERT_DOTTED == pixel: pixel = update_line_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list)  # :
    elif TOKEN_CROSS       == pixel: pixel = update_cross_to_neighbour_get_pixel(pixel, over_list, under_list, right_list, left_list) # "+"
    # else: Nothing
    return pixel


# ----------------------------------------
def condition_token_to_ascii_get_pixel(pixel, over_list, under_list, right_list, left_list):
    '''
    from        to
    -----       -----
    |(text)     ▼(text)
    (text)|     (text)▼
    '''
    line_vert_list = (TOKEN_VERT_LINE, ASCII_LINE_VERT)

    if   (ASCII_CONDITION_RIGHT == right_list[0]) and (pixel in line_vert_list): pixel = ASCII_ARROW_DOWN  # ▼(
    elif (ASCII_CONDITION_LEFT  == left_list[0])  and (pixel in line_vert_list): pixel = ASCII_ARROW_DOWN  # )▼

    # else: Nothing
    return pixel


# ----------------------------------------
def arrow_token_to_ascii_get_pixel(pixel, over_list, under_list, right_list, left_list):
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
    left_cnxn_list  = (TOKEN_HORI_LINE, TOKEN_CROSS, ASCII_LINE_HORI, ASCII_CROSS, ASCII_CORN_UP_LEFT, ASCII_CORN_DOWN_LEFT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_HORI_b_VERT,
                       ASCII_LINE_HORI_bT_DOWN, ASCII_LINE_HORI_bT_UP, ASCII_LINE_VERT_bT_RIGHT, ASCII_CORN_b_UP_LEFT, ASCII_CORN_b_DOWN_LEFT)
    right_cnxn_list = (TOKEN_HORI_LINE, TOKEN_CROSS, ASCII_LINE_HORI, ASCII_CROSS, ASCII_CORN_UP_RIGHT, ASCII_CORN_DOWN_RIGHT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_LEFT, ASCII_CROSS_HORI_b_VERT,
                       ASCII_LINE_HORI_bT_DOWN, ASCII_LINE_HORI_bT_UP, ASCII_LINE_VERT_bT_LEFT, ASCII_CORN_b_UP_LEFT, ASCII_CORN_b_DOWN_LEFT)
    over_cnxn_list  = (TOKEN_VERT_LINE, TOKEN_CROSS, ASCII_LINE_VERT, ASCII_CROSS, ASCII_CORN_UP_LEFT, ASCII_CORN_UP_RIGHT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_VERT_T_LEFT, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_b_HORI_VERT,
                       ASCII_b_LINE_HORI_T_DOWN, ASCII_b_LINE_VERT_T_LEFT, ASCII_b_LINE_VERT_T_RIGHT, ASCII_CORN_UP_b_LEFT, ASCII_CORN_UP_b_RIGHT)
    under_cnxn_list = (TOKEN_VERT_LINE, TOKEN_CROSS, ASCII_LINE_VERT, ASCII_CROSS, ASCII_CORN_DOWN_LEFT, ASCII_CORN_DOWN_RIGHT,
                       ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_LEFT, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_b_HORI_VERT,
                       ASCII_b_LINE_HORI_T_UP, ASCII_b_LINE_VERT_T_LEFT, ASCII_b_LINE_VERT_T_RIGHT, ASCII_CORN_DOWN_b_LEFT, ASCII_CORN_DOWN_b_RIGHT)

    if   (TOKEN_RIGHT == pixel) and (left_list[0]  in left_cnxn_list): pixel = ASCII_ARROW_RIGHT # ─►
    elif (TOKEN_LEFT  == pixel) and (right_list[0] in right_cnxn_list): pixel = ASCII_ARROW_LEFT # ◄─
                                                                                                 # │
    elif (TOKEN_DOWN  == pixel) and (over_list[0]  in over_cnxn_list): pixel = ASCII_ARROW_DOWN  # ▼
    elif (TOKEN_UP    == pixel) and (under_list[0] in under_cnxn_list): pixel = ASCII_ARROW_UP   # ▲
                                                                                                 # │
    # else: Nothing
    return pixel


# ----------------------------------------
def block_token_to_ascii_get_pixel(pixel, over_list, under_list, right_list, left_list):
    '''
    from    to
    -----   -----
    #       █

    ##      ■■

    #       █
    #       █
    '''

    solid_hori_list = (TOKEN_SOLID, ASCII_BLOCK_HORIZONTAL_MID)

    if   (TOKEN_SOLID == pixel) and (left_list[0]  in solid_hori_list): pixel = ASCII_BLOCK_HORIZONTAL_MID # ■
    elif (TOKEN_SOLID == pixel) and (right_list[0] in solid_hori_list): pixel = ASCII_BLOCK_HORIZONTAL_MID # ■

    # special case
    # single ¤ used for knob
    elif (TOKEN_SOLID == pixel): pixel = ASCII_BLOCK_VERTICAL       # █

    # else: Nothing
    return pixel


# ----------------------------------------
def misc_token_to_ascii_get_pixel(pixel, over_list, under_list, right_list, left_list):
    '''
    from    to
    -----   -----
    £       ┴   (Ground symbol, vertical capacitor)
    ££      ┤├  (Horizontal capacitor)

    '''
    # special case
    #if (TOKEN_GND == pixel):  pixel = ASCII_LINE_HORI_T_UP # ┴

    left_cnxn_list  = (TOKEN_HORI_LINE, TOKEN_CROSS, TOKEN_SOLID, ASCII_BLOCK_HORIZONTAL_MID, ASCII_LINE_HORI, ASCII_CROSS, ASCII_CORN_UP_LEFT, ASCII_CORN_DOWN_LEFT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_HORI_b_VERT,
                       ASCII_LINE_HORI_bT_DOWN, ASCII_LINE_HORI_bT_UP, ASCII_LINE_VERT_bT_RIGHT, ASCII_CORN_b_UP_LEFT, ASCII_CORN_b_DOWN_LEFT)
    right_cnxn_list = (TOKEN_HORI_LINE, TOKEN_CROSS, TOKEN_SOLID, ASCII_BLOCK_HORIZONTAL_MID, ASCII_LINE_HORI, ASCII_CROSS, ASCII_CORN_UP_RIGHT, ASCII_CORN_DOWN_RIGHT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_LEFT, ASCII_CROSS_HORI_b_VERT,
                       ASCII_LINE_HORI_bT_DOWN, ASCII_LINE_HORI_bT_UP, ASCII_LINE_VERT_bT_LEFT, ASCII_CORN_b_UP_LEFT, ASCII_CORN_b_DOWN_LEFT)
    over_cnxn_list  = (TOKEN_VERT_LINE, TOKEN_CROSS, TOKEN_SOLID, ASCII_BLOCK_VERTICAL, ASCII_LINE_VERT, ASCII_CROSS, ASCII_CORN_UP_LEFT, ASCII_CORN_UP_RIGHT,
                       ASCII_LINE_HORI_T_DOWN, ASCII_LINE_VERT_T_LEFT, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_b_HORI_VERT,
                       ASCII_b_LINE_HORI_T_DOWN, ASCII_b_LINE_VERT_T_LEFT, ASCII_b_LINE_VERT_T_RIGHT, ASCII_CORN_UP_b_LEFT, ASCII_CORN_UP_b_RIGHT)
    under_cnxn_list = (TOKEN_VERT_LINE, TOKEN_CROSS, TOKEN_SOLID, ASCII_BLOCK_VERTICAL, ASCII_LINE_VERT, ASCII_CROSS, ASCII_CORN_DOWN_LEFT, ASCII_CORN_DOWN_RIGHT,
                       ASCII_LINE_HORI_T_UP, ASCII_LINE_VERT_T_LEFT, ASCII_LINE_VERT_T_RIGHT, ASCII_CROSS_b_HORI_VERT,
                       ASCII_b_LINE_HORI_T_UP, ASCII_b_LINE_VERT_T_LEFT, ASCII_b_LINE_VERT_T_RIGHT, ASCII_CORN_DOWN_b_LEFT, ASCII_CORN_DOWN_b_RIGHT)

    if   (TOKEN_GND == pixel) and (left_list[0]  in left_cnxn_list): pixel = ASCII_LINE_VERT_T_LEFT   # ┤
    elif (TOKEN_GND == pixel) and (right_list[0] in right_cnxn_list): pixel = ASCII_LINE_VERT_T_RIGHT # ├
    elif (TOKEN_GND == pixel) and (over_list[0]  in over_cnxn_list): pixel = ASCII_LINE_HORI_T_UP     # ┴
    elif (TOKEN_GND == pixel) and (under_list[0] in under_cnxn_list): pixel = ASCII_LINE_HORI_T_DOWN  # ┬

    # else: Nothing
    return pixel


# ----------------------------------------
def pixel_update_get_list(in_list, func):
    out_list = list()
    row_size = len(in_list)
    # for all rows
    for row_cnt in range(0, row_size):
        in_str = in_list[row_cnt]
        col_size = len(in_str)
        _str = ""
        # for all chars
        for col_cnt in range(0, col_size):
            over_list, under_list, left_list, right_list = pixel_surrounding_get_list(in_list, row_cnt, col_cnt, 2)
            pixel_old = in_list[row_cnt][col_cnt]
            pixel_new = func(pixel_old, over_list, under_list, right_list, left_list)
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
    _list = pixel_update_get_list(_list, line_token_to_ascii_get_pixel)
    _list = pixel_update_get_list(_list, condition_token_to_ascii_get_pixel)
    _list = pixel_update_get_list(_list, arrow_token_to_ascii_get_pixel)
    _list = pixel_update_get_list(_list, block_token_to_ascii_get_pixel)
    _list = pixel_update_get_list(_list, misc_token_to_ascii_get_pixel)
    return _list


# ----------------------------------------
def print_to_screen(_list):
    for _str in _list:
       print(_str)


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
