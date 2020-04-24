
class Living():
    def rightFootForward(self):
        print('right foot forward')
    def leftFootForward(self):
        print('left foot forward')
    def walk(self):
        for i in range(10):
            self.rightFootForward()
            self.leftFootForward()
        
class Magic(Living):
    def fly(self):
        print('flying')
    def castSpells(self):
        print('casting a spell')

class Muggle(Living):
    pass

class Werewolf(Magic):
    def changeToWolf(self):
        print('Ahhh the moon... turning into a werewolf!')
    def howl(self):
        print('awhooooooooooooooooooooooo')

class Animagus(Magic):
    def __init__(self, name, animal, eyeColor):
        self.name = name
        self.animal = animal
        self.eyeColor = eyeColor
    def transform(self):
        print(self.name + ' is transforming into a ' + self.animal)



jp = Animagus('JP','dragon','brown')
jp.transform()
jp.walk()

erin = Animagus('Erin','dog','green')
erin.transform()
