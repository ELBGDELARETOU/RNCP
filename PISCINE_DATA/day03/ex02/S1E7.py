from S1E9 import Character

class Baratheon(Character):
    """Baratheon family"""
    
    def __init__(self, name, is_alive=True ):
        """Init function for "name" and "is_alive" parameter"""
        super().__init__(name, is_alive)
        self.family_name = "Baratheon"
        self.eye_color = "brown"
        self.hair_color = "dark"
    
    def die(self):
        """Function 'die' kills the character"""
        self.is_alive = False
    def __repr__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"
    def __str__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"

class Lannister(Character):
    """Lannister family"""

    def __init__(self, name, is_alive=True):
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eye_color = "blue"
        self.hair_color = "light"
        
    def create_lannister(name, is_alive=True):
        new = Lannister(name, is_alive=True)
        new.first_name = name;
        new.is_alive = is_alive
        return new
    def __repr__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"
    def __str__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"

def main():
    pass

if __name__ == "__main__":
    main()