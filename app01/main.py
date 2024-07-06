# asks for how many todos user wants to input
# stores and displays them

prompt = "How many todo: "
user_text = round(float(input(prompt)))
print("You want to add", user_text, "tasks.")
todos = []

def addtodo():
    prompt = "Enter a todo: "
    user_text = input(prompt)
    todos.append(user_text)

for i in range(user_text):
    addtodo()

print(todos)