class Invoice:

    def __init__(self, client, total):
        self.client = client
        self.total = total

    def __str__(self):
        return f'Invoice from {self.client} for {self.total}'
        # dump out values visible from an obj

inv = Invoice('Google', 500) # instantiate
print(str(inv))  # => Invoice from Google for 500