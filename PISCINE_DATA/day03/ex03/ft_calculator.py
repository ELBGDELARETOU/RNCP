class calculator:

    def __init__(self, vector):
        self.vector = vector

    def __add__(self, object)-> None:
        self.vector = [obj + object for obj in self.vector]
        print(self.vector)
        return [obj for obj in self.vector]
    
    def __mul__(self, object)-> None:
        self.vector = [obj * object for obj in self.vector]
        print(self.vector)
        return [obj for obj in self.vector]
    
    def __sub__(self, object)-> None:
        self.vector = [obj - object for obj in self.vector]
        print(self.vector)
        return[obj for obj in self.vector]
    
    def __truediv__(self, object)-> None:
        try:
            self.vector = [obj / object for obj in self.vector]
            print(self.vector)
            return [obj for obj in self.vector]
        except:
            print("'x / 0' is an undefined case")