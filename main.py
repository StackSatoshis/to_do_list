# Ryan Carroll
while True:
    # Gets user input and strips white space
    user_action = input("Type add, show, edit, or exit:")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('todos.txt, 'r'') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1 } - {item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete"))
            todos.pop(number - 1)
        case 'exit':
            break

print("BYE!")