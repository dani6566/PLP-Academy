import random


# Define your quiz questions
quiz_questions = [
    {
        "question": "What does 'IDE' stand for in programming?",
        "options": ["Integrated Development Environment", "Interactive Design Element", "Internal Data Exchange", "Independent Debugging Editor"],
        "answer": "Integrated Development Environment"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["List", "Tuple", "Dictionary", "Array"],
        "answer": "Array" # Python has lists, which are similar, but 'Array' itself is not a built-in type name like List or Tuple
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who directed the movie 'Inception'?",
        "options": ["Steven Spielberg", "Christopher Nolan", "Quentin Tarantino", "James Cameron"],
        "answer": "Christopher Nolan"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Mars", "Earth", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    }
]

def run_quiz(questions):
    score = 0
    # Shuffle questions to make each game a bit different
    random.shuffle(questions)

    print("\n--- Welcome to the Quiz! ---")
    print("Answer the questions by typing the letter of your choice (A, B, C, D).\n")

    for i, question_data in enumerate(questions):
        print(f"Question {i + 1}: {question_data['question']}")
        for j, option in enumerate(question_data['options']):
            print(f"  {chr(65 + j)}. {option}") # chr(65) is 'A'

        while True:
            user_answer = input("Your answer: ").strip().upper()
            if user_answer in [chr(65 + k) for k in range(len(question_data['options']))]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")

        correct_option_index = question_data['options'].index(question_data['answer'])
        if user_answer == chr(65 + correct_option_index):
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {chr(65 + correct_option_index)}. {question_data['answer']} 😞")
        print("-" * 30) # Separator

    print("\n--- Quiz Finished! ---")
    print(f"You scored {score} out of {len(questions)} questions. {get_feedback(score, len(questions))}")
    print("--------------------")

def get_feedback(score, total_questions):
    """Provides a fun feedback message based on the score."""
    percentage = (score / total_questions) * 100
    if percentage == 100:
        return "Amazing! A perfect score!"
    elif percentage >= 75:
        return "Excellent job!"
    elif percentage >= 50:
        return "Good effort, keep practicing!"
    else:
        return "Keep learning, you'll get there!"



# Main game loop
while True:
    run_quiz(quiz_questions)

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye! 👋")
        break
