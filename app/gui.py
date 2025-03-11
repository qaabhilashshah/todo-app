from functions import get_todos, write_todos
import FreeSimpleGUI as fsg

label = fsg.Text("Type in a to-do")
input_box = fsg.InputText(tooltip="Enter todo")
add_button = fsg.Button("Add")
show_button = fsg.Button("Show")
edit_button = fsg.Button("Edit")
complete_button = fsg.Button("Complete")
exit_button = fsg.Button("Exit")


window = fsg.Window(title="Todo App", layout=[[label, input_box, add_button, 
                                               show_button, edit_button, complete_button, exit_button]])
window.read()
window.close()
