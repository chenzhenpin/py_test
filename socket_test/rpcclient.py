from xmlrpc.client import ServerProxy
s=ServerProxy('http://localhost:9999',allow_none=True)
s.set('foo','bar')
print(s.get('foo'))
print(s.add(1,2))