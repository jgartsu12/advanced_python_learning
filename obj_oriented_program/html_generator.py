# Using Polymorphism to Build an HTML Generator in Python
# inheritance is often coupled with polymorphism
# polymorphism
# tool that can render html on the page with multiple subpages that can render subpages
class Html:
    def __init__(self, content):
        self.content = content

    def render(self): # abstract class - sole purpose = holding and storing shared beh only child classes call this class
        raise NotImplementedError('Subclass must implement render method')  # never call html class - common conv when using very complex sys - pattern vreate class that u dont want end user to connect with but create abstract class 

class Heading(Html):
    def render(self):
        return f'<h1>{self.content}</h1>'

class Div(Html):
    def render(self):
        return f'<div>{self.content}</div>'


tags = [
        Div('some content'),
        Heading('Some big heading'),
        Div('another div')
]

for tag in tags:
    print(str(tag) + ': ' + tag.render()) # debugger use
    # => 
        # <__main__.Div object at 0x00000226E2F47508>: <div>some content</div>
        # <__main__.Heading object at 0x00000226E2F47588>: <h1>Some big heading</h1>
        # <__main__.Div object at 0x00000226E2F47608>: <div>another div</div>