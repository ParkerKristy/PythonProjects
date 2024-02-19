# DAY 3 - list view, exit program - make program more intelligent
#Match, FOR loop, strip()

todos = []

while True:
    user_action = input("Type 'add','show' or exit: ")

    match user_action: #match case statement
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            print(todos)
        case 'exit':
            break #break the while loop


print("Bye!")


# FOR LOOP

#strip() method - #to allow str like 'add ' - with space
# #The strip() method removes any leading, and trailing whitespaces.
# # Leading means at the beginning of the string, trailing means at the end.
# # You can specify which character(s) to remove, if not, any whitespaces will be removed.


todos = []

while True:
    user_action = input("Type 'add','show' or exit: ")
    user_action = user_action.strip()

    match user_action: #match case statement
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            for item in todos:  #for loop
                print(item)
        case 'exit':
            break #break the while loop


print("Bye!")