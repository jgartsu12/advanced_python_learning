class Invoice: 

    def __init__(self, client, total): 
        self._client = client  # protect with _ so child class has access to this data (inheritance) --> data attributte should be protected 
        self._total = total     
       
    def formatter(self):      
        return f'{self._client} owes: ${self._total}' 

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client 

    
    @property
    def total(self):
        return self._total


google = Invoice('Google', 100) 

print(google.client) # => Google # gives direct acces to client

google.client = 'Yahoo' # overrides to yahoo

print(google.client)  # => Yahoo

print(google.total) # => 100