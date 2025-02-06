## how the data is stored -> store in a txt file
## function for showing the list of todos we have

while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    user_action = user_action.strip()

    with open('todo/todo.txt', 'r') as file: 
        todos = file.readlines()
    with open('todo/done.txt','r') as file:
        done = file.readlines()

    if user_action == 'add' or user_action == 'edit' or user_action=='complete':
            print(f'{user_action} what?')
    
    elif 'add' in user_action: 

        todo = user_action[3:] 
        todos.append(todo)
        print('Successfully added!')

        with open('todo/todo.txt', 'w') as file: 
            file.writelines(todos)

    elif 'show' in user_action or 'display' in user_action:

        ## new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1} - {item} " 
                print(row)

    elif 'edit' in user_action: 
        
        number = int(user_action[4:])
        #number = int(input('Number of the todo to edit:'))
        number = number - 1
        todos[number] = input('Enter the new todo: ') + '\n'

        with open('todo/todo.txt', 'w') as file: 
            file.writelines(todos)

    elif 'complete' in user_action or 'done' in user_action: 
        
        num = int(user_action[8:])
        done.append(todos[num-1])
        with open('todo/done.txt', 'w') as file: 
                file.writelines(done)

        todos.pop(num-1) 
        with open('todo/todo.txt', 'w') as file: 
                file.writelines(todos)

        print('Yayy! you finished something today!')

    elif 'exit' in user_action: 

        break

    else: 
         print("Command doesn't exist!")