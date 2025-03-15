import FreeSimpleGUI as fsg

label1 = fsg.Text("Select files to compress:")
input_box1 = fsg.Input()
choose_button1 = fsg.FileBrowse("Choose files", key = 'files')


label2 = fsg.Text("Select desitnation folder:")
input_box2 = fsg.Input()
choose_button2 = fsg.FolderBrowse("Choose files", key = 'folder')
compress_button = fsg.Button("Compress")

window = fsg.Window("File Compressor", layout=[[label1, input_box1, choose_button1], 
                                               [label2, input_box2, choose_button2],
                                               [compress_button]])

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    for file in filepaths:
        print(f"Compressing {file} to {folder}")


window.close()