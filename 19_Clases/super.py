class rectangulo:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width

class square(rectangulo):
    def __init__(self,lenght,width):
        super().__init__(lenght,width)
        
class cube(rectangulo):
    def __init__(self,lenght,width,height):
        super().__init__(lenght,width)
        self.height = height

        