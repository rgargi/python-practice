import json

with open("app01/extra/questions.json", "r") as f:
    questions = f.read()

# as the above code returns a string we need 
# the json module to get the data as a list

list_of_questions = json.loads(questions)
score = 0

for q in list_of_questions:
    print(q['question_text'])
    for i,a in enumerate(q['alternatives']):
        print(f"{i+1}. {a}")
    chosen_ans = input("Enter answer: ")
    try:
        q['chosen_ans'] = int(chosen_ans)
    except ValueError as err:
        print("ERROR! The number should be between 1 and", len(q['alternatives']))
        q['chosen_ans'] = chosen_ans

print("\nRESULTS")

for i,q in enumerate(list_of_questions):
    if q['chosen_ans'] == q['correct_ans']:
        score += 1
        print(f"Question {i} - Correct! - Your Answer: {q['chosen_ans']}, Correct Answer: {q['correct_ans']}")
    else:
        print(f"Question {i} - Wrong! - Your Answer: {q['chosen_ans']}, Correct Answer: {q['correct_ans']}")

print(f"You answered {score} out of {len(list_of_questions)} questions correctly.")