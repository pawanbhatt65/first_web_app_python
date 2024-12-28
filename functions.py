FILEPATH='todos.txt'

def get_todos(filename=FILEPATH):
    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos,mode, filename='todos.txt'):
    with open(filename, mode) as file_local:
        file_local.writelines(local_todos)


print(__name__)
print(type(__name__))
if __name__ == '__main__':
    print("Hello from functions!")