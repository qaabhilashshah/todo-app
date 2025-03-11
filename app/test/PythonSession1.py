todos = []

while True:
    user_action = input('Type add, show or exit: ')

    if user_action == 'add':
        todo = input('Enter a todo: ')
        todos.append(todo)
    elif user_action == 'show':
        print(todos)
    else:
        break
print("Bye!!!")
        
            
    
            
