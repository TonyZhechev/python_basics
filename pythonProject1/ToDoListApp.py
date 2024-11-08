todos = []

while True:
    user_action =input("Type add,show,or exit:")
    match user_action:
        case 'add':
            todo =input("Enter a todo:")
            todos.append(todo)
        case 'show'| 'display':
            for item in todos:
                item = item.upper()
                print(item)
        case "edit":
            number =int(input("Edit a number"))
            number = number - 1
            new_todo = input("Enter a todo")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
         print("This is incorrect")
print('Bye!')




