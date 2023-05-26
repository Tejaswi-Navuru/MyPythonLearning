class Myclass:
    classvar = "Hello"

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printHello(self):
        print(Myclass.classvar + ' ' + self.firstname + ' ' + self.lastname)

print(Myclass.classvar)

class01 = Myclass("Tejaswi", "Navuru")
class01.printHello()
class02 = Myclass("Test", "User")
class02.printHello()