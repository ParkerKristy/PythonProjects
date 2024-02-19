user_prompt = 'Enter a To-Do :'
todo1 = input(user_prompt)
todo2 = input(user_prompt)
todo3 = input(user_prompt)

todos = [todo1, todo2, todo3, 'Hello']
print(todos)

print(type(user_prompt))
print(type(todos))


# removal of second " - SyntaxError: unterminated string literal (detected at line 1)
# "", '' it does not matter but be aware of words like don't - in that case use ""
# removal of second ) - SyntaxError: '(' was never closed
# space around = does not matter, but it is more readable
# expression needs to be in separated lines - SyntaxError: invalid syntax