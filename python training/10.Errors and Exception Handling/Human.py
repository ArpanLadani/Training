from Animal import Animal

class Human(Animal):#@UndefinedVariable
    def __init__(self):
        pass
    def Hit(self):
        print('hit')

instance = Human()
instance.Bark()