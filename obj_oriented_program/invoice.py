class Invoice: # created class

    def __init__(self, client, total): #constructor fn with instance to class via self arg
        self.client = client   # assign args to the obj # Add data directly to the class
        self.total = total      

    def formatter(self):      
        return f'{self.client} owes: ${self.total}' # access so self values above


google = Invoice('Google', 100)
snapchat = Invoice('Snapchat', 200)

print(google.formatter()) # => Google owes: $100
print(snapchat.formatter()) # => Snapchat owes: $200


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
