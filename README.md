# Quiz / Trivia Game

A terminal-based multiple-choice quiz game built in Python. Questions are loaded from a JSON file, presented in random order, and the player's high score is tracked and saved between runs.

## Features

- **Multiple-choice quiz** — each question shows numbered options; the player answers by typing a number
- **Scoring** — tracks how many questions the player got right, out of the total
- **Randomized questions** — question order is shuffled every time you play, so it's different each round
- **High score tracking** — the best score ever achieved is saved to a file and compared against on every playthrough; the player is notified when they beat it
- **Replay** — after finishing all questions, the player is asked whether they'd like to play again
- **Input validation** — typing a letter or an out-of-range number doesn't crash the game; it's counted as wrong and the quiz continues

## Requirements

- Python 3

No external dependencies — this project only uses Python's standard library (`json`, `os`, `random`).

## Files

- `quiz_game.py` — the main program
- `questions.json` — the question bank (must exist before running; the program will not create it for you)
- `high_score.json` — created automatically the first time you play, to store the high score

## Question Format

Questions are stored as a list of objects in `questions.json`:

```json
[
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    }
]
```

- `question` — the question text
- `options` — the list of choices shown to the player, numbered automatically
- `answer` — the correct choice, written out exactly as it appears in `options`

## Usage

Run the script from the terminal:

```bash
python quiz_game.py
```

For each question:
1. The question text is displayed
2. The available options are shown, numbered starting from 1
3. Type the **number** of your chosen option and press Enter

After all questions have been answered, your score is shown (e.g. `Your final score is: 8/15`), compared against the saved high score, and you'll be asked if you want to play again.

## Notes

- If `questions.json` is missing or contains invalid JSON, the program will stop with an error message — a question bank is required to run the quiz.
- If `high_score.json` is missing or corrupted, the high score simply starts at `0` rather than stopping the program, since that's a normal first-run state.
- Built as a learning project — a good next step would be adding question categories, a timer per question, or difficulty levels.