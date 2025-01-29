# Thayer Yang
# 29 JAN 2025
# Quiz with DICTIONARIES and LISTS

score = 0

questions = [
    {
        'question':'What is the most religious group?',
        'answer': 'christianity'
    },
    {
        'question':'What year did LMFAO\'s song "Party Rock Anthem" release?',
        'answer':'2011'
    },
    {
        'question':'In AppleTV\'s hit comedy series Ted Lasso, what is Jamie Tartt\'s jersey number?',
        'answer': '9'
    },
    {
        'question':'What was named "Friday"?',
        'answer':'horse'
    },
    {
        'question':'What is the word defined in the Oxford Dictionary?: "not anything; no single thing."?',
        'answer':'nothing'
    }
]

for question in questions:
    question_text = question.get('question')
    print(question_text)

    user_answer = input("Enter answer: ")
    correct_answer = question.get('answer')

    if user_answer == correct_answer:
        score += 1

print(f"Your score = {score}/{len(questions)}")