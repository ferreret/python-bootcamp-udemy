'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''


def find_and_replace(file_name, word, replacement):
    with open(file_name, "r+") as file_handler:
        text = file_handler.read()
        text = text.replace(word, replacement)
        file_handler.seek(0)
        file_handler.write(text)
        file_handler.truncate()
