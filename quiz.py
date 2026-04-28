import sys
sys.stdout.reconfigure(encoding='utf-8')
import random

print("🎯 Welcome to the CS Quiz Game!")
print("------------------------------")
name = input("Enter your name: ")
print(f"\nHello {name}! Let's start the quiz!")
print("You will be asked 5 questions.")
print("Type the number of your answer.\n")

# 5 Questions
questions = [
    {
        "question": "What is the time complexity of Binary Search?",
        "options": ["1. O(n)",
                    "2. O(n²)",
                    "3. O(log n)",
                    "4. O(1)"],
        "answer": "3"
    },
    {
        "question": "Which data structure works on LIFO principle?",
        "options": ["1. Queue",
                    "2. Stack",
                    "3. Linked List",
                    "4. Tree"],
        "answer": "2"
    },
    {
        "question": "What is the output of: print(type(10/2)) in Python?",
        "options": ["1. <class 'int'>",
                    "2. <class 'float'>",
                    "3. <class 'str'>",
                    "4. <class 'double'>"],
        "answer": "2"
    },
    {
        "question": "What does Git command 'git commit' do?",
        "options": ["1. Uploads code to GitHub",
                    "2. Saves a snapshot of your changes locally",
                    "3. Downloads latest code changes",
                    "4. Creates a new branch"],
        "answer": "2"
    },
    {
        "question": "Which of these is an example of a compiled language?",
        "options": ["1. Python",
                    "2. JavaScript",
                    "3. Ruby",
                    "4. C++"],
        "answer": "4"
    }
]

# Shuffle questions
random.shuffle(questions)

# Ask questions and track score
score = 0
total = len(questions)

for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for option in q["options"]:
        print(option)

    user_answer = input("\nYour answer (1/2/3/4): ")

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        correct_option = q["options"][int(q["answer"]) - 1]
        print(f"❌ Wrong! Correct answer: {correct_option}\n")

# Final result
print("------------------------------")
print(f"Quiz Complete! Well done {name}!")
print(f"Your Score: {score}/{total}")

if score == total:
    print("🏆 Perfect Score! You're a CS genius!")
elif score >= 4:
    print("🎉 Excellent! Great knowledge!")
elif score >= 3:
    print("👍 Good job! Keep learning!")
elif score >= 2:
    print("📚 Fair effort! Review missed topics!")
else:
    print("💪 Don't give up! Study and try again!")

print("------------------------------")