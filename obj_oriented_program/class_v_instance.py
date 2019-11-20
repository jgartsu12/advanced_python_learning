# Class vs Instance Attributes in Python
# ~~~~~~~~~~~~ instance attribute
# class Website:
#     def __init__(self, title): # instance
#         self.title = title # title that gets passed in

# # ws = Website('My Website Title')
# # print(ws.title) # => My Website Title

# ws = Website('My Title')
# print(ws.__dict__) # converts to dictionary ... prints attributes and their values
# # => {'title': 'My Title'} = instance attribute - an attribute that belongs to this instance

# ws_two = Website('Second Title') # another instance
# print(ws_two.__dict__) # => {'title': 'Second Title'}

#~~~~~~~~~~ class attributes
class DifferentWebsite:
    title = 'My Class Title'

# dw = DifferentWebsite() # another instance
# print(dw.__dict__) # = > {} --- no attributes pinted

dw = DifferentWebsite()
print(dw.title) # => My Class Title
# have access to the values but not treated same way as instance attributes since it belongs to the class

dw_two = DifferentWebsite()
print(dw_two.title)  # => My Class Title

# ~~ diff btwn class and instance attributes
# class att - belongs to class definition
# instance att - beloings to the instance - need to pass value directly into the instance
# __dict__ helps u to decipher which attribute is which 
