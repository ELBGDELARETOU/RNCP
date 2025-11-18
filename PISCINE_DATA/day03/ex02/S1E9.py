from abc import ABC, abstractmethod 

class Character(ABC):
    """Abstract class"""
    @abstractmethod
    def __init__(self, name, is_alive=True):
        """Init function for name and alive parameter in abstract class"""
        self.first_name = name
        self.is_alive = is_alive 
    def die(self):
        """kills"""
        self.is_alive = False
    def __repr__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"
    def __str__(self):
        return f"Vector: ({self.__class__.__name__}, {self.eye_color}, {self.hair_color})"

class Stark(Character):
    """I am stark"""
    def __init__(self, name, is_alive=True):
        """Init function for name and alive parameter"""
        super().__init__(name, is_alive)
    def die(self):
        """Function 'die' kills the character"""
        super().die()

# def main():   
    # stark = Stark("Martin", False)
    # print(stark.is_alive)

# if __name__ == "__main__":
    # main();