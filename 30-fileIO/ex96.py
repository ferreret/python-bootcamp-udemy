'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''


def copy_and_reverse(path_file, new_path_file):
    with open(path_file) as original:
        text_file = original.read()
    with open(new_path_file, "w") as new_file:
        new_file.write(text_file[::-1])
