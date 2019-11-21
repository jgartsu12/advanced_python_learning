def get_file_contents(filename):  # function that takes file path that is open u[]
    queried_file = open(filename, 'r') # read

    if queried_file.mode == 'r':
        return queried_file.read() # check to see if in read mode


content = get_file_contents('./text_content.txt') # store fn in content variable

print(content) # => Lorem ....

print("Number of words", len(content.split())) # split words in list elements to call it and get length
# => Number of words 1502