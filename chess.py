def main():
    def fen_to_list(string):
        new_string = string.split()[0]
        # extract positions only
        new_string = new_string.split("/")
        # row separated list
        nested = []
        # final nested list
        row = []
        # row seperator

        # make initial list
        for i in new_string:
            for j in i:
                if j.isdigit():
                    row.extend("." * int(j))
                else:
                    row.append(j)
            nested.append(row)
            row = []
        return nested

    # function that prints the board, takes in the 2d list and highlighted square
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
            if piece == ".":
                return print("Cannot move an empty square")

            #move validation block

            if piece == "p":
                if not is_valid_black_pawn(board, from_row, from_col, to_row, to_col):
                    return
            if piece =="P":
                if not is_valid_white_pawn(board, from_row, from_col, to_row, to_col):
                    return

            if piece == "r":
                if not is_valid_black_rook(board, from_row, from_col, to_row, to_col):
                    return

            if piece == "R":
                if not is_valid_white_rook(board, from_row, from_col, to_row, to_col):
                    return

            #move validation block
            board[from_row][from_col] = "."
            board[to_row][to_col] = piece
            highlight_squares = {
                from_square: "\033[41m",  # Red for from
                to_square: "\033[42m"  # Green for to
            }
            list_to_board(board, highlight_squares=highlight_squares)

    fen = input("Enter a FEN string: ")
    board = fen_to_list(fen)
    while True:
        print()
        list_to_board(board)
        print()
        fr = input("From: ").lower()
        to = input("to: ").lower()
        if fr == "end":
            break
        move_piece(board, fr, to)


def is_valid_black_pawn(board, from_row, from_col, to_row, to_col):
        if to_row < from_row:
            print("Pawn cannot move backwards")
            return False

        if abs(to_col - from_col) == 1 and to_row == from_row + 1:
            target = board[to_row][to_col]
            if target == ".":
                print("Pawn cannot capture empty square")
                return False
            if target.islower():
                print("Pawn cannot capture same color")
                return False
            print("Black pawn capture!")
            return True  # valid diagonal capture

        if to_col == from_col:
            # Forward move
            if board[to_row][to_col] != ".":
                print("Pawn cannot move forward into an occupied square")
                return False

            if from_row == 1 and to_row == 3 and board[2][to_col] == ".":
                return True  # double step
            elif to_row == from_row + 1:
                return True  # normal 1 step forward

        print("Invalid pawn move")
        return False

def is_valid_white_pawn(board, from_row, from_col, to_row, to_col):
    if to_row > from_row:
        print("Pawn cannot move backwards")
        return False

    # Diagonal capture
    if abs(to_col - from_col) == 1 and to_row == from_row - 1:
        target = board[to_row][to_col]
        if target == ".":
            print("Pawn cannot capture empty square")
            return False
        if target.isupper():
            print("Pawn cannot capture same color")
            return False
        print("White pawn capture!")
        return True

    # Forward move
    if to_col == from_col:
        if board[to_row][to_col] != ".":
            print("Pawn cannot move forward into an occupied square")
            return False

        if from_row == 6 and to_row == 4 and board[5][to_col] == ".":
            return True  # double move from starting position
        elif to_row == from_row - 1:
            return True  # single forward step

    print("Invalid pawn move")
    return False

def is_valid_black_rook(board, from_row, from_col, to_row, to_col):
    # 1. Rook can only move in straight lines
    if from_row != to_row and from_col != to_col:
        print("Rook must move in a straight line")
        return False

    # 2. Determine direction and check path for obstructions
    step_row = 0
    step_col = 0

    if from_row == to_row:  # Horizontal move
        step_col = 1 if to_col > from_col else -1
    else:  # Vertical move
        step_row = 1 if to_row > from_row else -1

    curr_row = from_row + step_row
    curr_col = from_col + step_col

    while curr_row != to_row or curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            print("Rook's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col

    # 3. Handle capture
    target = board[to_row][to_col]
    if target != "." and target.islower():
        print("Rook cannot capture same color")
        return False
    if target != "." and target.isupper():
        print("Rook captured white piece")

    return True


def is_valid_white_rook(board, from_row, from_col, to_row, to_col):
    # 1. Rook can only move in straight lines
    if from_row != to_row and from_col != to_col:
        print("Rook must move in a straight line")
        return False

    # 2. Determine direction and check path for obstructions
    step_row = 0
    step_col = 0

    if from_row == to_row:  # Horizontal move
        step_col = 1 if to_col > from_col else -1
    else:  # Vertical move
        step_row = 1 if to_row > from_row else -1

    curr_row = from_row + step_row
    curr_col = from_col + step_col

    while curr_row != to_row or curr_col != to_col:
        if board[curr_row][curr_col] != ".":
            print("Rook's path is blocked")
            return False
        curr_row += step_row
        curr_col += step_col

    # 3. Handle capture
    target = board[to_row][to_col]
    if target != "." and target.isupper():
        print("Rook cannot capture same color")
        return False
    if target != "." and target.islower():
        print("Rook captured black piece")

    return True



if __name__ == "__main__":
    main()
