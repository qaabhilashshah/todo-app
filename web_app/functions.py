FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos,filepath=FILEPATH):
     with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == '__main__':
    print("This is a module with functions for working with todos.")
    print("You can import it and use the functions.")
    print("You can't run it directly.")
    print("You can use the following functions:")
    print("- get_todos()")
    print("- write_todos(todos)")
    print("Good luck!")