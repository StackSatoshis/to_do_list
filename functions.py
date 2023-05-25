FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    '''
    Reads a text file and returns
    list of todo items
    '''
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    '''
    Writes the to-do items to a file
    :param todos_arg:
    :param filepath:
    :return:
    '''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())