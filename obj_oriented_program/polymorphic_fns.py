# Building Polymorphic Functions in Pythoad
# if shared beh use inheritance with polymorphism like html_generator.py
# only want select classes to use render fn use polymorphic fns
class Heading:
    def __init__(self, content):
        self.content = content

    def render(self): 
        return f'<h1>{self.content}</h1>'

class Div:
    def __init__(self, content):
        self.content = content

    def render(self):
        return f'<div>{self.content}</div>' 


div_one = Div('some content')
heading = Heading('Some big heading') # comma after these makes tuples error
div_two = Div('another div')

     #polymorphism
def html_render(tag_object): # tag_object = any thing that takes render
    print(tag_object.render())


html_render(div_one) # => <div>some content</div>
html_render(div_two) # => <div>another div</div>
html_render(heading) # => <h1>Some big heading</h1>

