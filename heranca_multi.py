class animal:
    pass



class ave(animal):
    pass

class mamifero(animal):
    def __init__(self, patas) -> None:
        self.patas = patas
        super(). __init__(patas)
        
class Gato(mamifero):
    pass
class vaca(mamifero):
    pass
class leao(mamifero):
    pass

class ornitorrinco(mamifero, ave):
    pass

gato = Gato(4)
print(gato)