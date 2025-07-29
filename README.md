# Chess Move Validator And Chess Engine

## This is a Python terminal-based chess application that:
- Renders a visual board from any valid FEN string.
- Lets you move pieces using algebraic notation (e.g., e2 to e4).
- Validates movement rules for all chess pieces.
- Highlights the from-square (red) and to-square (green) on each move.
- Detects and prevents illegal moves based on chess rules.

## Features:
- Fully functional FEN parser (fen_to_list)
- Visual terminal board rendering with Unicode chess pieces
- Move validation for:
  - Pawns (including double move, diagonal capture, and blocked paths)
  - Rooks (straight-line movement, path obstruction)
  - Knights (L-shape jump, capture)
  - Bishops (diagonal movement, path obstruction)
  - Queens (combination of rook + bishop movement)
  - Kings (1-square move in all directions, no castling yet)
    - Check detection and king safety enforcement
    - Suppresses irrelevant error messages during internal safety checks
    - Clear, user-friendly error messages for invalid moves
- Friendly error messages for invalid moves

## Recent Updates:
- Added is_in_check function to detect if a king is under attack.
- Implemented is_move_safe to prevent moves that leave your king in check.
- Integrated check validation into move processing.
- Added output suppression during internal move validation to avoid clutter.
- Cleaned up capture messages for clarity.

## HOW TO RUN: 
1. Clone the repository:
- git clone https://github.com/Mphele/FEN-string-to-chess-game

2. Run the python script:
- python chess.py

3. When prompted, paste any valid FEN string:
- e.g. rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

4. Make moves entering which square you want to move from to which square:
- e.g. From: e2 To: e4

5. Type "end" as the From: or To: input to quit the game.


## Future Features (Planned):
- En passant
- Castling
- Check and checkmate detection
- Move history tracking
- GUI interface (e.g., Tkinter or Pygame)

### Author:
- Mphele Moswane





