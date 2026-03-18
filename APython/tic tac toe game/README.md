# Tic Tac Toe 🎮

A simple two-player Tic Tac Toe game for the terminal, written in Python.

## How to Play

Run the game with:

```bash
python tic_tac_toe.py
```

Two players take turns — **X** always goes first. On each turn, the board is displayed alongside a numbered position guide:

```
- | - | -     1 | 2 | 3
- | - | -     4 | 5 | 6
- | - | -     7 | 8 | 9
```

Enter a number from **1–9** to place your mark in the corresponding cell. The game ends when a player gets three in a row (horizontally, vertically, or diagonally), or when all nine cells are filled and it's a tie.

## Requirements

- Python 3.x
- No external dependencies

## Project Structure

```
tic_tac_toe.py
│
├── play_game()          # Main game loop
├── display_board()      # Renders the board
├── handle_turn()        # Handles player input and move validation
├── check_if_game_over() # Checks for a win or tie after each move
│   ├── check_rows()
│   ├── check_columns()
│   └── check_diagonals()
├── check_for_tie()      # Detects a full board with no winner
└── flip_player()        # Alternates the active player
```

## Rules

- Players alternate turns; X goes first.
- A player wins by filling an entire row, column, or diagonal with their mark.
- If all 9 cells are filled with no winner, the game is a draw.
- Choosing an already-occupied cell will prompt you to pick again.
