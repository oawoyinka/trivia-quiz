import json
import os
import random


def load_questions(file_path: str):
    if not os.path.exists(file_path):
        exit(f"File not found: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            questions = json.load(file)
        return questions
    except json.JSONDecodeError:
        exit(f"Error decoding JSON from file: {file_path}")


def load_high_score(high_score_file):
    if not os.path.exists(high_score_file):
        return 0

    try:
        with open(high_score_file, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("high_score", 0)
    except json.JSONDecodeError:
        return 0


def save_high_score(high_score_file, high_score):
    with open(high_score_file, "w", encoding="utf-8") as file:
        json.dump({"high_score": high_score}, file, indent=4)


def run_quiz(questions):
    score = 0
    shuffled_questions = questions.copy()
    random.shuffle(shuffled_questions)

    for question in shuffled_questions:
        question_text = question["question"]
        options = question["options"]

        print(question_text)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        try:
            user_choice = int(input("Pick an option: "))
            selected_option = options[user_choice - 1]
        except (ValueError, IndexError):
            print("Invalid selection — marked as wrong.")
            print()
            continue

        if selected_option == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

        print()

    print(f"Your final score is: {score}/{len(questions)}")
    return score


def main():
    questions_file = "questions.json"
    high_score_file = "high_score.json"

    questions = load_questions(questions_file)
    high_score = load_high_score(high_score_file)

    while True:
        score = run_quiz(questions)

        if score > high_score:
            high_score = score
            save_high_score(high_score_file, high_score)
            print(f"New high score! You beat the previous record with {score}.")
        else:
            print(f"High score remains: {high_score}")

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing, goodbye!")
            break


if __name__ == "__main__":
    main()