class User:
    
    def __init__(self, shoe_size=10, shirt_size="L", pant_size="L"):
        self.data = {}
        self._shoe_size = shoe_size
        self._shirt_size = shirt_size
        self._pant_size = pant_size
    
    def set_all_data(self, data_set):
        self.data = dict(data_set)

    def set_data(self, data, value):
        self.data[value] = data

    def get_data(self, data):
        return self.data[data]

    def shoe_size(self):
        return self._shoe_size

    def shirt_size(self):
        return self._shirt_size

    def pant_size(self):
        return self._pant_size
    


    

