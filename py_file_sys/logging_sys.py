# How to Create and Write to a File in Python

file_builder = open("logger.txt", "w+")

for i in range(10):
    file_builder.write(f"I'm on line {i + 1}\n") # i+1 = incrementss so it starts on 1 

file_builder.close()

# in logger.txt on each line it said what line of code it is on
# overrode what was previous written in file - temporary logger
# THIS SYNTAX WILL OVERRIDE CONTENT IN THE FILE via write