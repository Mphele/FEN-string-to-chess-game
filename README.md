# Chess Move Validator and Engine

## Overview

This is a **Python terminal-based chess application** that lets you play chess directly from **any valid FEN string**.
It enforces all standard movement rules and includes **king safety checks** to prevent illegal moves.

* Renders a visual board in the terminal using Unicode chess pieces.
* Move pieces using **algebraic notation** (e.g., `e2 to e4`).
* Highlights the **from-square** (red) and **to-square** (green) on each move.
* Validates moves for legality and prevents moves that would leave your king in check.
* Displays clear messages for illegal moves and captures.

## Features

* **FEN parsing**: Convert any valid FEN string into a playable board.
* **Move validation for all pieces**:

  * **Pawns**: single/double moves, diagonal captures, blocked path detection, promotion.
  * **Rooks**: straight-line movement with path obstruction detection.
  * **Knights**: L-shaped jumps with capture rules.
  * **Bishops**: diagonal movement with path obstruction detection.
  * **Queens**: combined rook and bishop movement with path checking.
  * **Kings**: one-square moves, check detection, and king safety enforcement.
* **User-friendly messages**: Includes capture notifications and suppressed messages during internal checks.

## Recent Updates

* Added **`is_in_check`** to detect if a king is under attack.
* Implemented **`is_move_safe`** to prevent moves that leave the king in check.
* Integrated check validation into move processing.
* Added **pawn promotion** when a pawn reaches the 8th rank.
* Cleaned up capture messages for clarity.

## How to Run

1. Clone the repository:

   ```
   git clone https://github.com/Mphele/FEN-string-to-chess-game
   ```
2. Run the Python script:

   ```
   python chess.py
   ```
3. Paste any valid FEN string when prompted:

   ```
   rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
   ```
4. Make moves by entering the squares:

   ```
   From: e2 To: e4
   ```
5. Type `"end"` as the From or To input to quit.

## Future Features

* **En passant**
* **Castling**
* **Full check and checkmate detection**
* **Move history tracking**
* **GUI interface** (Tkinter, Pygame, or web-based)

## Author

* Mphele Moswane

