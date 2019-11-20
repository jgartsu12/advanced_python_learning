# Using Polymorphism to Build an HTML Generator in Python
# inheritance is often coupled with polymorphism
# polymorphism: poly = many .. morph = to change ==> one item can have many forms ... overrides beh 
# tool that can render html on the page with multiple subpages that can render subpages
class Html:
    def __init__(self, content):
        self.content = content

    def render(self): # abstract class - sole purpose = holding and storing shared beh only child classes call this class
        raise NotImplementedError('Subclass must implement render method')  # never call html class - common conv when using very complex sys - pattern vreate class that u dont want end user to connect with but create abstract class 
                # riase used cuz dont want anyone to call html class
                # protects against any other subclasses / child classes
                # react component class -> if dont call render fn u get an error
                # this ensures render beh on child classes with changed beh 
class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>' # polymorphish diff beh within child classes

class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>' 


tags = [
        Div('some content'),
        Heading('Some big heading'),
        Div('another div')
]

for tag in tags:
    print(tag.render()) 
#  # => <div>some content</div>
# <h1>Some big heading</h1>
# <div>another div</div>