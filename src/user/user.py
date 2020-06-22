from enum import Enum, auto

class ClothingSize(Enum):
    XXS = auto()
    XS = auto()
    S = auto()
    M = auto()
    L = auto()
    XL = auto()
    XXL = auto()
    XXXL = auto()

class User:
    
    def __init__(self, shoe_size=10, shirt_size=ClothingSize.L, pant_size=ClothingSize.L):
        self.data = {}
        self.shoe_size = shoe_size
        self.shirt_size = shirt_size
        self.pant_size = pant_size
    
    def set_all_data(self, data_set):
        self.data = dict(data_set)

    def set_data(self, data, value):
        self.data[value] = data

    def get_data(self, data):
        return self.data[data]

    def shoe_size(self):
        return self.shoe_size

    def shirt_size(self):
        return self.shirt_size

    def pant_size(self):
        return self.pant_size
    


    

