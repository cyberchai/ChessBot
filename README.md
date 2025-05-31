# Minimax Chess Bot

**Author:** Chaira Harder

This is a simple two-player chess game implemented in Python using the `python-chess` library. It includes a computer opponent powered by the **Minimax algorithm with alpha-beta pruning** to determine optimal moves. Players can choose to play as either White or Black, and the computer begins with one of several classic chess openings when it starts first.

## Features

* Command-line interface for playing chess against the computer
* Support for standard UCI move notation (e.g., `e2e4`)
* Randomly selected classical opening strategies (Sicilian, Ruy Lopez, Italian)
* Board evaluation based on piece values
* Minimax decision-making with configurable depth and alpha-beta pruning
* Real-time board display after each move

## Requirements

* Python 3
* [`python-chess`](https://pypi.org/project/python-chess/) library

Install the required library with:

```bash
pip install python-chess
```

## How to Run

```bash
python3 your_script_name.py
```

You will be prompted to choose to play as White or Black. Choose move using standard notation (e.g., `e2e4`), and the bot will respond on its turn.

## Notes

* The current version supports basic gameplay logic; features like check detection and advanced move heuristics may be improved in future versions.
