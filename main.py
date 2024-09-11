user_prompt="enter a to-do"

todos = []

while True:
    user_action = input("Type add,show,edit,complete or exit :")
    user_action =  user_action.strip()

    if "add" in user_action:
        todo = user_action[4:]

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)


    elif 'show' in user_action:
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        #new_todos= [item.strip('\n') for item in todos]
        ##

        for index,items in enumerate(todos):
            items = items.strip("\n")
            row= f"{index +1}-{items}"
            print(row)

    elif 'edit' in user_action:
        number = int(input("number of todo to edit :"))
        number= number-1

        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()
        #print("Here is how it will be",todos)


        new_todo = input("enter a new to-do")
        todos[number]=new_todo

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)


        print("Got it!")
    elif 'complete' in user_action:
        number = int(input("Number of todo to complete: "))

        with open("todos.txt","r") as file:
            todos = file.readlines()
        index=number-1
        todo_to_remove = todos[index]
        todos.pop(index)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")


print("bye")




