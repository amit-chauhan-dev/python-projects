import random
import time

# question with options and answers
quiz = [
    {
        "question": "Capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Kolkata", "D. Chennai"],
        "answer": "A"
    },
    {
        "question": "2 + 2 = ?",
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    {
        "question": "Color of sky?",
        "options": ["A. Green", "B. Blue", "C. Red", "D. Yellow"],
        "answer": "B"
    },
    {
        "question": "Capital of Gujarat?",
        "options": ["A. Surat", "B. Vadodara", "C. Gandhinagar", "D. Rajkot"],
        "answer": "C"
    }
]

# Welcome + username (Level 1)
print("Welcome to Quiz game")
name = input("Enter your name: ")
print(f"Hello {name}, let's start the quiz!\n")

score = 0

# Randomize questions (Level 2)
random.shuffle(quiz)

# Timer setup (Level 2)
time_limit = 10  # seconde per question 

# quiz loop
for q in quiz:
    print("\n" + q["question"])

    for options in q["options"]:
        print(options)
    
    start_time = time.time()
    answer = input("Your answer (A/B/C/D): ").upper()
    end_time = time.time()

    # Check time
    if end_time - start_time > time_limit:
        print("Time's up!")
    
    # check answer
    if answer == q["answer"]:
        print("Correct ")
        score += 1
    else:
        print("Wrong ")
        print("Correct answer is", q["answer"])

# Final Score 
print(f"\n {name}, Your Score: {score}/{len(quiz)}")

# High Score Save (Level 3)
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except:
    high_score = 0

if score > high_score:
    print("New High Score!")
    with open("highscore.txt", "w") as file:
        file.write(str(score))
else:
    print("High Score:", high_score)

print("Thanks for playing ")