#infinite while-loop
while True:
    print('Hello')

# Inside vs Outside the Loop

todos = []

while True:  #Inside loop
    user_prompt = "Enter a To-Do: " #- it is not necessary to have it inside a loop - program will be heavier
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)

#capitalize() vs title()
#Clean the room vs Clean The Room

user_prompt = "Enter a To-Do: "

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())  #title - every word has capitalized letter - Clean The Room
    todos.append(todo)


#no print -> no output  (todo.title())
#no parenthesis -> no output  print(todo.title)






































