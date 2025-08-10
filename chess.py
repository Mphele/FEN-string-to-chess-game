import copy

PIECE_NAMES = {
    "P": "Pawn", "R": "Rook", "N": "Knight",
    "B": "Bishop", "Q": "Queen", "K": "King",
    "p": "Pawn", "r": "Rook", "n": "Knight",
    "b": "Bishop", "q": "Queen", "k": "King"
}

def main():
    fen = input("Enter a FEN string: ")
    board = fen_to_list(fen)
    while True:
        print()
        list_to_board(board)
        print()
        fr = input("From: ").lower()
        to = input("to: ").lower()
        if fr == "end" or to == "end":
            break
        move_piece(board, fr, to)



def fen_to_list(string):
        new_string = string.split()[0]

        new_string = new_string.split("/")

        nested = []

        row = []

        for i in new_string:
            for j in i:
                if j.isdigit():
                    row.extend("." * int(j))
                else:
                    row.append(j)
            nested.append(row)
            row = []
        return nested


def list_to_board(board, highlight_squares=None):
        piece_symbols = {
            'r': '♜',  # Black rook
            'n': '♞',  # Black knight
            'b': '♝',  # Black bishop
            'q': '♛',  # Black queen
            'k': '♚',  # Black king
            'p': '♟',  # Black pawn
            'R': '♖',  # White rook
            'N': '♘',  # White knight
            'B': '♗',  # White bishop
            'Q': '♕',  # White queen
            'K': '♔',  # White king
            'P': '♙',  # White pawn
            '.': '.'  # Empty square
        }
        if highlight_squares is None:
            highlight_squares = {}
        print("  a  b c d e f g h")
        # loop through each mini list (row)
        for row_index, row in enumerate(board):

            # this list will store each item and be reset after a row this is done so we can add a highlighted square when the time comes
            display_row = []

            # loop through each row and get each character. enumerate gets both index and character we unpack index to col_index and the character to char
            for col_index, char in enumerate(row):
                # this checks each character if it matches the co-ordinate given.
                # + is middle, left = letter through ASCII right =
                square = chr(ord('a') + col_index) + str(8 - row_index)
                symbol = piece_symbols[char]
                if square in highlight_squares:
                    color = highlight_squares[square]
                    symbol = f"{color}{symbol}\033[0m"
                display_row.append(symbol)
            print(f"{8 - row_index} " + " ".join(display_row))

def move_piece(board, from_square, to_square):
        valid_co = "abcdefgh"
        print(f"Move: {from_square} to {to_square}")
        if len(from_square) != 2 or len(to_square) != 2:
            return print("Invalid co-ordinate length")
        elif from_square[0] not in valid_co or int(from_square[1]) > 8:
            return print("Invalid from_square co-ordinate")
        elif to_square[0] not in valid_co or int(to_square[1]) > 8:
            return print("Invalid to square co-ordinate")
        elif from_square == to_square:
            return print("Co-ordinates cannot be the same ")
        else:
            from_square = from_square.lower().replace(" ", "")
            to_square = to_square.lower().replace(" ", "")

            from_col = "abcdefgh".index(from_square[0])  # gets column index using the letter of from_square
            from_row = 8 - int(from_square[1])  # gets row index using number in the from_square co-ordinate
            to_col = "abcdefgh".index(to_square[0])  # gets column index using the letter of to_square
            to_row = 8 - int(to_square[1])  # gets row index using number in the to_square co-ordinate

            piece = board[from_row][from_col]

            color = "white" if piece.isupper() else "black"

            if not is_move_safe(board, from_row, from_col, to_row, to_col, color):
                print("Move not allowed — it would leave your king in check.")
                return

            if piece == ".":
                return print("Cannot move an empty square")

            #move validation block

            if piece == "p":
                if not is_valid_black_pawn(board, from_row, from_col, to_row, to_col, suppress_output=False):
                    return
            if piece == "P":
                if not is_valid_white_pawn(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            if piece == "r":
                if not is_valid_black_rook(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return
            if piece == "R":
                if not is_valid_white_rook(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            if piece == "b":
                if not is_valid_black_bishop(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return
            if piece == "B":
                if not is_valid_white_bishop(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            if piece == "n":
                if not is_valid_black_knight(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return
            if piece == "N":
                if not is_valid_white_knight(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            if piece == "q":
                if not is_valid_black_queen(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return
            if piece == "Q":
                if not is_valid_white_queen(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            if piece == "k":
                if not is_valid_black_king(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return
            if piece == "K":
                if not is_valid_white_king(board, from_row, from_col, to_row, to_col, suppress_output=True):
                    return

            #move validation block


            board[from_row][from_col] = "."
            board[to_row][to_col] = piece
            highlight_squares = {
                from_square: "\033[41m",  # Red for from
                to_square: "\033[42m"  # Green for to
            }
            list_to_board(board, highlight_squares=highlight_squares)

def find_king(board, color):
    if color.lower() =="white":
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col =="K":
                    return row_index, col_index

    elif color.lower()=="black":
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col =="k":
                    return row_index, col_index
    return None


def is_in_check(board, color):
    king_row, king_col = find_king(board, color)

    for row_index, row in enumerate(board):
        for col_index, piece in enumerate(row):

            if color.lower() == "white" and piece.islower():
                if piece == 'p' and is_valid_black_pawn(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'r' and is_valid_black_rook(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'n' and is_valid_black_knight(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'b' and is_valid_black_bishop(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'q' and is_valid_black_queen(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'k' and is_valid_black_king(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True

            elif color.lower() == "black" and piece.isupper():
                if piece == 'P' and is_valid_white_pawn(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'R' and is_valid_white_rook(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'N' and is_valid_white_knight(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'B' and is_valid_white_bishop(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'Q' and is_valid_white_queen(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True
                if piece == 'K' and is_valid_white_king(board, row_index, col_index, king_row, king_col, suppress_output=True):
                    return True

    return False

def is_move_safe(board, from_row, from_col, to_row, to_col, color):

    test_board = copy.deepcopy(board)

    piece = test_board[from_row][from_col]
    test_board[to_row][to_col] = piece
    test_board[from_row][from_col] = '.'

    return not is_in_check(test_board, color)


def is_valid_black_pawn(board, from_row, from_col, to_row, to_col, suppress_output=False):
    if to_row < from_row:
        if not suppress_output:
            print("Pawn cannot move backwards")
        return False

    if abs(to_col - from_col) == 1 and to_row == from_row + 1:
        target = board[to_row][to_col]
        if target == ".":
            if not suppress_output:
                print("Pawn cannot capture empty square")
            return False
        if target.islower():
            if not suppress_output:
                print("Pawn cannot capture same color")
            return False
        if target.isupper():
            if not suppress_output:
                print(f"Black Pawn captured White {PIECE_NAMES[target]}")
        return True

    if to_col == from_col:

        if board[to_row][to_col] != ".":
            if not suppress_output:
                print("Pawn cannot move forward into an occupied square")
            return False

        if from_row == 1 and to_row == 3 and board[2][to_col] == ".":
            return True
        elif to_row == from_row + 1:
            return True

    if not suppress_output:
        print("Invalid pawn move")
    return False

def is_valid_white_pawn(board, from_row, from_col, to_row, to_col, suppress_output=False):
    if to_row > from_row:
        if not suppress_output:
            print("Pawn cannot move backwards")
        return False


    if abs(to_col - from_col) == 1 and to_row == from_row - 1:
        target = board[to_row][to_col]
        if target == ".":
            if not suppress_output:
                print("Pawn cannot capture empty square")
            return False
        if target.isupper():
            if not suppress_output:
                print("Pawn cannot capture same color")
            return False
        if target.islower():
            if not suppress_output:
                print(f"White Pawn captured Black {PIECE_NAMES[target]}")
        return True


    if to_col == from_col:
        if board[to_row][to_col] != ".":
            if not suppress_output:
                print("Pawn cannot move forward into an occupied square")
            return False

        if from_row == 6 and to_row == 4 and board[5][to_col] == ".":
            return True
        elif to_row == from_row - 1:
            return True

    if not suppress_output:
        print("Invalid pawn move")
    return False

def is_valid_black_rook(board, from_row, from_col, to_row, to_col, suppress_output=False):

    if from_row != to_row and from_col != to_col:
        if not suppress_output:
            print("Rook must move in a straight line")
        return False


    step_row = 0
    step_col = 0

    if from_row == to_row:
        step_col = 1 if to_col > from_col else -1
    else:
        step_row = 1 if to_row > from_row else -1

    curr_row = from_row + step_row
    curr_col = from_col + step_col

    while curr_row != to_row or curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            if not suppress_output:
                print("Rook's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col


    target = board[to_row][to_col]
    if target != "." and target.islower():
        if not suppress_output:
            print("Rook cannot capture same color")
        return False
    if target.isupper():
        if not suppress_output:
            print(f"Black Rook captured White {PIECE_NAMES[target]}")

    return True

def is_valid_white_rook(board, from_row, from_col, to_row, to_col, suppress_output=False):

    if from_row != to_row and from_col != to_col:
        if not suppress_output:
            print("Rook must move in a straight line")
        return False


    step_row = 0
    step_col = 0

    if from_row == to_row:
        step_col = 1 if to_col > from_col else -1
    else:
        step_row = 1 if to_row > from_row else -1

    curr_row = from_row + step_row
    curr_col = from_col + step_col

    while curr_row != to_row or curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            if not suppress_output:
                print("Rook's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col


    target = board[to_row][to_col]
    if target != "." and target.isupper():
        if not suppress_output:
            print("Rook cannot capture same color")
        return False
    if target.islower():
        if not suppress_output:
            print(f"White Rook captured Black {PIECE_NAMES[target]}")


    return True

def is_valid_black_bishop(board, from_row, from_col, to_row, to_col, suppress_output=False):

    if abs(to_row - from_row) != abs(to_col - from_col):
        if not suppress_output:
            print("Bishop must move diagonally")
        return False


    step_row = 1 if to_row > from_row else -1
    step_col = 1 if to_col > from_col else -1


    curr_row = from_row + step_row
    curr_col = from_col + step_col
    while curr_row != to_row and curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            if not suppress_output:
                print("Bishop's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col


    target = board[to_row][to_col]
    if target != "." and target.islower():
        if not suppress_output:
            print("Bishop cannot capture same color")
        return False
    if target.isupper():
        if not suppress_output:
            print(f"Black Bishop captured White {PIECE_NAMES[target]}")

    return True

def is_valid_white_bishop(board, from_row, from_col, to_row, to_col, suppress_output=False):

    if abs(to_row - from_row) != abs(to_col - from_col):
        if not suppress_output:
            print("Bishop must move diagonally")
        return False


    step_row = 1 if to_row > from_row else -1
    step_col = 1 if to_col > from_col else -1


    curr_row = from_row + step_row
    curr_col = from_col + step_col
    while curr_row != to_row and curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            if not suppress_output:
                print("Bishop's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col


    target = board[to_row][to_col]
    if target != "." and target.isupper():
        if not suppress_output:
            print("Bishop cannot capture same color")
        return False
    if target.islower():
        if not suppress_output:
            print(f"White Bishop captured Black {PIECE_NAMES[target]}")

    return True

def is_valid_black_knight(board, from_row, from_col, to_row, to_col, suppress_output=False):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
        if not suppress_output:
            print("Knight must move in an L-shape")
        return False


    target = board[to_row][to_col]
    if target != "." and target.islower():
        if not suppress_output:
            print("Knight cannot capture same color")
        return False
    if target.isupper():
        if not suppress_output:
            print(f"Black Knight captured White {PIECE_NAMES[target]}")

    return True

def is_valid_white_knight(board, from_row, from_col, to_row, to_col, suppress_output=False):

    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
        if not suppress_output:
            print("Knight must move in an L-shape")
        return False


    target = board[to_row][to_col]
    if target != "." and target.isupper():
        if not suppress_output:
            print("Knight cannot capture same color")
        return False
    if target.islower():
        if not suppress_output:
            print(f"White Knight captured Black {PIECE_NAMES[target]}")

    return True

def is_valid_black_queen(board, from_row, from_col, to_row, to_col, suppress_output=False):
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff == col_diff:
        step_row = 1 if to_row > from_row else -1
        step_col = 1 if to_col > from_col else -1
        curr_row, curr_col = from_row + step_row, from_col + step_col
        while curr_row != to_row and curr_col != to_col:
            if board[curr_row][curr_col] != ".":
                if not suppress_output:
                    print("Queen's diagonal path is blocked")
                return False
            curr_row += step_row
            curr_col += step_col

    elif from_row == to_row or from_col == to_col:
        step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)
        curr_row, curr_col = from_row + step_row, from_col + step_col
        while curr_row != to_row or curr_col != to_col:
            if board[curr_row][curr_col] != ".":
                if not suppress_output:
                    print("Queen's straight path is blocked")
                return False
            curr_row += step_row
            curr_col += step_col
    else:
        if not suppress_output:
            print("Queen must move in a straight line or diagonally")
        return False

    target = board[to_row][to_col]
    if target != "." and target.islower():
        if not suppress_output:
            print("Queen cannot capture same color")
        return False
    if target.isupper():
        if not suppress_output:
            print(f"Black Queen captured White {PIECE_NAMES[target]}")

    return True

def is_valid_white_queen(board, from_row, from_col, to_row, to_col, suppress_output=False):
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff == col_diff:
        step_row = 1 if to_row > from_row else -1
        step_col = 1 if to_col > from_col else -1
        curr_row, curr_col = from_row + step_row, from_col + step_col
        while curr_row != to_row and curr_col != to_col:
            if board[curr_row][curr_col] != ".":
                if not suppress_output:
                    print("Queen's diagonal path is blocked")
                return False
            curr_row += step_row
            curr_col += step_col

    elif from_row == to_row or from_col == to_col:
        step_row = 0 if from_row == to_row else (1 if to_row > from_row else -1)
        step_col = 0 if from_col == to_col else (1 if to_col > from_col else -1)
        curr_row, curr_col = from_row + step_row, from_col + step_col
        while curr_row != to_row or curr_col != to_col:
            if board[curr_row][curr_col] != ".":
                if not suppress_output:
                    print("Queen's straight path is blocked")
                return False
            curr_row += step_row
            curr_col += step_col
    else:
        if not suppress_output:
            print("Queen must move in a straight line or diagonally")
        return False

    target = board[to_row][to_col]
    if target != "." and target.isupper():
        if not suppress_output:
            print("Queen cannot capture same color")
        return False
    if target.islower():
        if not suppress_output:
            print(f"White Queen captured Black {PIECE_NAMES[target]}")

    return True

def is_valid_black_king(board, from_row, from_col, to_row, to_col, suppress_output=False):
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff > 1 or col_diff > 1:
        if not suppress_output:
            print("King can only move one square in any direction")
        return False

    target = board[to_row][to_col]
    if target != "." and target.islower():
        if not suppress_output:
            print("King cannot capture same color")
        return False
    if target.isupper():
        if not suppress_output:
            print(f"Black King captured White {PIECE_NAMES[target]}")

    return True

def is_valid_white_king(board, from_row, from_col, to_row, to_col, suppress_output=False):
    row_diff = abs(to_row - from_row)
    col_diff = abs(to_col - from_col)

    if row_diff > 1 or col_diff > 1:
        if not suppress_output:
            print("King can only move one square in any direction")
        return False

    target = board[to_row][to_col]
    if target != "." and target.isupper():
        if not suppress_output:
            print("King cannot capture same color")
        return False
    if target.islower():
        if not suppress_output:
            print(f"White King captured Black {PIECE_NAMES[target]}")

    return True


if __name__ == "__main__":
    main()
