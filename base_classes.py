def F(): pass

class Event():
    def __init__(self):
        self.__F = []

    def invock(self, *args, **kvargs):
        for i in self.__F:
            i(*args, **kvargs)

    def __iadd__(self, other):
        if not(other in self.__F):
            self.__F.append(other)
        return self

    def __isub__(self, other):
        if other in self.__F:
            self.__F.remove(other)
        return self

    def check_presence(self, other):
        if other in self.__F:
            return True
        else:
            return False

    def clear(self):
        self.__F.clear()

    def get_content(self):
        print(self.__F)


class Singleton():
    def __new__(cls):
        if not hasattr(cls, 'instace'):
            cls.instace = super(Singleton, cls).__new__(cls)
        return cls.instace
