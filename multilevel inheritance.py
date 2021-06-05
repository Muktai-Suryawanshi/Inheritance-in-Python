class name:
    def myname(self):
        print("my name")

class student(name):
    def game(self):
        print("game")

class marry(student):
    def sahi(self):
        print("same")

m = marry()
m.myname()
m.game()
m.sahi()