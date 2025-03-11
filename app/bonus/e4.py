import webbrowser

user_term = input("Enter a term to search: ")
webbrowser.open('https://www.google.com/search?q=' + user_term)