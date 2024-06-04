def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def display_question(question_block):
    for line in question_block:
        print(line.strip())

def get_user_answer():
    return input("Your answer: ").strip().lower()

def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer.strip().lower()

def display_correct_answers(answers):
    print("\nCorrect Answers:")
    for answer in answers:
        print(answer.strip())

def main():
    questions_file_path = 'Question.txt'
    answers_file_path = 'Answer.txt'
    
    # Read questions and answers from files
    questions = read_file(questions_file_path)
    answers = read_file(answers_file_path)
    
    # Display each question block (question + options)
    question_block = []
    answer_index = 0
    for line in questions:
        if line.strip() == "":
            if question_block:
                display_question(question_block)
                user_answer = get_user_answer()
                correct_answer = answers[answer_index].split('.')[1].strip()
                if check_answer(user_answer, correct_answer):
                    print("Correct!")
                else:
                    print(f"Incorrect. The correct answer is {correct_answer}.")
                question_block = []
                answer_index += 1
        else:
            question_block.append(line)
    
    # Display the last question block if any
    if question_block:
        display_question(question_block)
        user_answer = get_user_answer()
        correct_answer = answers[answer_index].split('.')[1].strip()
        if check_answer(user_answer, correct_answer):
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

if __name__ == "__main__":
    main()
