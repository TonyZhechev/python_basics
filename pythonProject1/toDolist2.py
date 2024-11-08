from ToDoListApp import user_action

todos=[]


while True:
    user_action = input("Type add, show,or exit")
    user_action = user_action.strip
    match user_action:
        case 'Type add':
            todo = input('Enter a todo')
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'or exit':
            break
print('Bye')