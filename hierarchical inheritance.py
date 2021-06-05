class first:
    def func1(self):
        print("This is First Page")

class second(first):
    def func2(self):
        print("This is Second Page")

class third(first):
    def func3(self):
        print("This is Third Page")

ob = second()
ob1 = third()
ob.func1()
ob.func2()
