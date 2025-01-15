class foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        self._x += value
    
    #@ x.deleter quando nao quer tirar da memoria 

foo = foo(10)
print(foo.x)