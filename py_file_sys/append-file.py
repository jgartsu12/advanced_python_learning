import datetime
from time import sleep

for i in range(5):
    file_builder = open("logger_one.txt", "a+") #  a+ = append
    file_builder.write(f'{datetime.datetime.now()}\n') # brings in current data as timestamp
    file_builder.close()

    print("file created")

    sleep(1) # want diff datetime stamp for ea element