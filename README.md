# Terminal Tic-Tac-Toe

A simple 2-player Tic-Tac-Toe game written in beginner-friendly Python.
It runs in the terminal, uses no external libraries, and no classes — just
functions, lists, loops, and `input()`.

## Requirements

- Python 3 (any recent version)

## How to Run

```bash
python tic_tac_toe.py
```

On some systems you may need:

```bash
python3 tic_tac_toe.py
```

## How to Play

- Player 1 plays as **X**, Player 2 plays as **O**.
- The board shows positions 1–9:

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

- Players take turns typing a number from 1 to 9.
- If a position is already taken, you are asked to pick another one.
- The first player to get three in a row (across, down, or diagonally) wins.
- If all nine positions fill up with no winner, the game is a draw.
- After each game you are asked whether you want to play again.

## Example

```
 X | O | 3
---+---+---
 4 | X | 6
---+---+---
 7 | O | X

Player X wins! Congratulations!
Do you want to play again? (y/n):
```

## Project Structure

```
terminal-tic-tac-toe/
├── tic_tac_toe.py    # the whole game
└── README.md         # this file
```

## License

MIT — free to use and modify.
