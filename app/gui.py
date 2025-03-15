import functions
import FreeSimpleGUI as fsg
import time
import os

if not os.path.exists("app/todos.txt"):
    with open("app/todos.txt", "w") as file:
        pass

fsg.theme('Black')
clock = fsg.Text('', key = 'clock', font=('Helvetica', 20))
label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo", key = "todo")
add_button = fsg.Button(size = 10, image_source="app/add.png", key="Add", 
                        mouseover_colors="LightBlue2", tooltip="Add todo")
list_box = fsg.Listbox(values=functions.get_todos(), 
                       key="todos", enable_events= True, size=[50, 10])

edit_button = fsg.Button("Edit")
complete_button = fsg.Button(size = 10, image_source="app/complete.png", key="Complete", 
                        mouseover_colors="LightBlue2", tooltip="Complete todo")
exit_button = fsg.Button("Exit")

window = fsg.Window(title="Todo App",
                    layout= [[clock],
                             [label],
                             [input_box,add_button], 
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup("Please select a todo to edit", font=('Helvetica', 20))

        case "Complete":
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                fsg.popup("Please select a todo to complete", font=('Helvetica', 20))
        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case fsg.WIN_CLOSED:
            break

window.close()
