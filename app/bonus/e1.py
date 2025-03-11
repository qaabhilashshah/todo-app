import glob

myfiles = glob.glob('app/files/*.txt')

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())
