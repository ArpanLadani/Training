from Human import Human

class Animal(Human):#@UndefinedVariable
    def __init__(self):
        pass
    def Bark(self):
        print('bark')


instance = Animal()
instance.Hit()