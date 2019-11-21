# Reading and Working with File Data in Python notes

# read in text data and work with it

def get_file_contents(filename): # filename = path to the file
    queried_file = open(filename, 'r') # 'r' -> reading

    if queried_file.mode == 'r': # make sure in read mode
        return queried_file.read() # read fn


content = get_file_contents("py_file_sys/text_content.txt") # (path to the file)

print(content)

