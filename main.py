questions = [
    {
        "question": "Which language is mainly used for data science?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. SQL"],
        "answer": "B"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["A. Stack", "B. Queue", "C. Tree", "D. Graph"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "Which of the following is used to store key-value pairs in Python?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "question": "Which technology is used to package an application with its dependencies?",
        "options": ["A. Docker", "B. Figma", "C. Git", "D. Excel"],
        "answer": "A"
    }
]

score = 0

print("===== Python Technical Assessment =====")

for i, item in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {item['question']}")

    for option in item["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == item["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n===== Assessment Result =====")
print("Score:", score, "/", total_questions)
print("Percentage:", round(percentage, 2), "%")

if percentage >= 60:
    print("Result: Passed")
else:
    print("Result: Failed")