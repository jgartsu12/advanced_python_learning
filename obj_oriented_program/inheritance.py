# Introduction to Inheritance in Python
# inheritance =>  create specialized versions of classes

class User: # abstract user with 3 attributes
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def greeting(self): # make globally avaible to all users
        return f'Hi {self.first_name} {self.last_name}'
# child class has same beh as parent class with specialized beh only for that child class that parent class wont have
class AdminUser(User): # AdminUser inherits from users (what admin user can only do:)
    def active_users(self):
        return '500'

# instances
tiff = AdminUser('tiffany@devcamp.com', 'Tiff', 'Hudgens')

kristine = User('k@devcamp.com', 'Kristine', 'Hudgens')

print(tiff.active_users()) # => 500
# print(kristine.active_users())  # => AttributeError: 'User' object has no attribute 'active_users'
print(tiff.greeting()) # => Hi Tiff Hudgens prints because AdminUser inherited from User