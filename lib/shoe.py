class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if type(size) is not int:
            print("size must be an integer")
        self.size = size
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"