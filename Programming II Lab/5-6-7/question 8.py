correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

with open('student_answers.txt', 'r') as file:
    student_answers = file.read().strip().split(',')

if len(student_answers) != len(correct_answers):
    print("Error: The number of answers does not match the number of questions.")
else:
    num_correct = 0
    num_incorrect = 0
    incorrect_questions = []
    for i in range(len(correct_answers)):
        if student_answers[i] == correct_answers[i]:
            num_correct += 1
        else:
            num_incorrect += 1
            incorrect_questions.append(i + 1)

    if num_correct >= 15:
        result = "passed"
    else:
        result = "failed"

    print("The student", result, "the exam.")
    print("Number of correctly answered questions:", num_correct)
    print("Number of incorrectly answered questions:", num_incorrect)
    print("Question numbers of incorrectly answered questions:", incorrect_questions)
