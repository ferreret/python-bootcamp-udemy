'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''


def copy(path_file, new_path_file):
    with open(path_file) as original:
        text_file = original.read()
    with open(new_path_file, "w") as new_file:
        new_file.write(text_file)


copy('story.txt', 'story_copy.txt')  # None
