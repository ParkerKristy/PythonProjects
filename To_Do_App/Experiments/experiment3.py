#1 Match case

#if input would be something else then match cases fe(asdfghj)
# none of the match cases would be executed
#loop goes back to the first line of the while loop
#
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
        case _: #whatever input that does not match
            print("Hey, you entered unknown command!")


print("Bye!")




# #2 Bitwise OR operator
while True:
    user_action = input("Type 'add','show' or exit: ")
    user_action = user_action.strip()

    match user_action: #match case statement
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show' | 'display': #Bitwise OR operator - if one of the str is match = True
            for item in todos:  #for loop
                print(item)
        case 'exit':
            break #break the while loop


print("Bye!")

#3 For loop
while True:
    user_action = input("Type 'add','show' or exit: ")
    user_action = user_action.strip()

    match user_action: #match case statement
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo.capitalize())
        case 'show':
            for item in todos:  #for loop - you can add more lines under
                item = item.title()
                print(item)
        case 'exit':
            break #break the while loop


print("Bye!")