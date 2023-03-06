# Ryan Carroll
while True:
    # Gets user input and strips white space
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()

    if 'add' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1 } - {item}"
            print(row)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("enter new todo: ")
        todos[number] = new_todo + "\n"

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        to_be_removed = todos[index].strip('\n')
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"{to_be_removed} was removed from the list."
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print("Command not valid, please try again. ")

print("BYE!")