import json
import os


def load_questions(file_path: str):
    if not os.path.exists(file_path):
        exit(f"File not found: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            questions = json.load(file)
        return questions
    except json.JSONDecodeError:
        exit(f"Error decoding JSON from file: {file_path}")


def run_quiz(questions):
    score = 0

    for question in questions:
        question_text = question["question"]
        options = question["options"]

        print(question_text)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        user_choice = input("Pick an option: ")
        user_choice = int(user_choice)
        selected_option = options[user_choice - 1]

        if selected_option == question["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

        print()

    print(f"Your final score is: {score}/{len(questions)}")


def main():
    questions = load_questions("questions.json")
    run_quiz(questions)


if __name__ == "__main__":
    main()