class Invoice: # created class

    def __init__(self, client, total): #constructor fn with instance to class via self arg
        self.client = client   # assign args to the obj # Add data directly to the class
        self.total = total      
       
    def formatter(self):      
        return f'{self.client} owes: ${self.total}' # access so self values above


google = Invoice('Google', 100) # gets stored in google variable as an object if want access to we have access automcially

print(google.client) # => setter method
# setter process - go into obj and set the value
google.client = 'Yahoo'

print(google.client) # => Yahoo overide client value  via setter (setter in python are objs so can reach into and overide the vlaue)


#     def greeting():
#         return 'Hi there'


# inv_one = Invoice()     # instantiate class Invoice
# print(inv_one)

# inv_two = Invoice()     # instantiate class Invoice again
# print(inv_two)

# class Invoice:

#     def greeting(self):
#         return 'Hi there'


# inv_one= Invoice()     # instantiate class Invoice again w/ greeting() fn
# print(inv_one.greeting())

# inv_two = Invoice()     # instantiate class Invoice again w/ greeting() fn
# print(inv_two.greeting())

# = >
# Hi there
# Hi there
