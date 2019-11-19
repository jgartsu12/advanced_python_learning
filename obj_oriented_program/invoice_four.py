class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self): # nice to read 
        return f'Invoice from {self.client} for {self.total}'

    def __repr__(self): # raw data in a log example
        return f'Invoice <values: {self.client}, {self.total}>'

inv = Invoice('Google', 500) # instantiate
print(str(inv))  # => Invoice from Google for 500
print(repr(inv))  # => Invoice <values: Google, 500>