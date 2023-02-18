#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ddddddddddddddddddddddddddddddddddddddddddddddd"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, size):
        self.__width = size
        self.__height = size
