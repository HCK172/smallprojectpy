## how the data is stored -> store in a txt file
## function for showing the list of todos we have

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    with open('todo/todo.txt', 'r') as file: 
        todos = file.readlines()
   
    
    match user_action: 
        case 'add':
            todo = input('Enter a todos: ') + '\n'
            todos.append(todo)
            
            with open('todo/todo.txt', 'w') as file: 
                file.writelines(todos)

        case 'show' | 'display':

            ## new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item} " 
                print(row)

        case 'edit':
            file = open('todo/todo.txt', 'w')
            number = int(input('Number of the todo to edit:'))
            number = number - 1
            todos[number] = input('Enter the new todo: ') + '\n'

            with open('todo/todo.txt', 'w') as file: 
                file.writelines(todos)

        case 'complete': 
            file = open('todo/todo.txt', 'w')
            num = int(input('Enter the number you have completed: '))
            todos.pop(num - 1)
            with open('todo/todo.txt', 'w') as file: 
                file.writelines(todos)

            print('Yayy! you finished something today!')

        case 'exit':
            break