class one:
    def func1(self):
        print("This is function one")

class two(one):
    def func2(self):
        print("This is function two")

class three(one):
    def func(self):
        print("This is function three")

class four(one):
    def func4(self):
        print("This is function four")

ob = four()
ob.func1()
