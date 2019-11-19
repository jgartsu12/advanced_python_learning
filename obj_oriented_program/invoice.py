# class Invoice:

#     def greeting():
#         return 'Hi there'


# inv_one = Invoice()     # instantiate class Invoice
# print(inv_one)

# inv_two = Invoice()     # instantiate class Invoice again
# print(inv_two)

class Invoice:

    def greeting(self):
        return 'Hi there'


inv_one= Invoice()     # instantiate class Invoice again w/ greeting() fn
print(inv_one.greeting())

inv_two = Invoice()     # instantiate class Invoice again w/ greeting() fn
print(inv_two.greeting())

# = >
# Hi there
# Hi there
