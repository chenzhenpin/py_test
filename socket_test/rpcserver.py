from xmlrpc.server import SimpleXMLRPCServer
class KeyServer:
    _rpc_method=['get','set','add']
    def __init__(self,address):
        self._data={}
        self._serv=SimpleXMLRPCServer(address,allow_none=True)
        for name in self._rpc_method:
            self._serv.register_function(getattr(self,name))
    def get(self,name):
        return self._data[name]
    def set (self,name,value):
        self._data[name]=value
    def add(self,a,b):
        return a+b
if __name__=='__main__':
    kserver=KeyServer(('',9999))
    kserver._serv.serve_forever()