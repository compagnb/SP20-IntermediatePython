
class Things():
    pass

class Living(Things):
    def rightFootForward(self):
        print('right foot forward')
    def leftFootForward(self):
        print('left foot forward')
    def walk(self):
        for i in range(10):
            self.rightFootForward()
            self.leftFootForward()

class NonLiving(Things):
    pass
        
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
    def transform(self):
        print('I am transforming')



