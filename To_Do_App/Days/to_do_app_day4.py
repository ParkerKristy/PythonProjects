#Day4 - add 'edit' feature
#list indexing

todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip() #to remove white spaces

    match user_action: #match case statement
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            for item in todos:  #for loop
                print(item)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            existing_todo = todos[number]
            print(existing_todo)
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break #break the while loop


print("Bye!")

# todos = ['clean', 'meet', 'throw']
# todos[0]
# 'clean'
# todos[1]
# 'meet'
# todos[2]
# 'throw'

#replacing an item from the list todos[number] = new_todo name''"