# How to Create and Write to a File in Python
#file builder - open up a file
file_builder = open("logger.txt", "w+") # open = fn built into py core lang => open up a NEW file if it cant find a saved file; w+ = write to file

file_builder.write("Hey I'm in a file!") # writes to the file dynamically

file_builder.close() # close file  so nothing else is added