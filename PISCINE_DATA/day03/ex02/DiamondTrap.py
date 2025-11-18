from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def set_eyes(self, color):
        self.eye_color = color
    def set_hairs(self, color):
        self.hair_color = color
    def get_eyes(self):
        return self.eye_color
    def get_hairs(self):
        return self.hair_color