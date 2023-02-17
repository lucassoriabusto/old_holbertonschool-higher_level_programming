#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """Super():
        Da acceso a los atributos de una clase padre o hermana
        para no tener que volver a escribirlos"""
        super().__init__(id)

        """Private instance attributes, each with
        its own public getter and setter"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle
        instance with the character #"""
        """self.x/y contiene las coordenadas donde se va a imprimir"""
        for n in range(self.__y):
            print()
        for n in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Update the class Rectangle
        Con self.variable accedes al valor de la
        variable para poder retornarlo"""
        return f"[Rectangle] ({self.id}) \
{self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) > 0:
            new_list = ["id", "width", "height", "x", "y"]
            """for a in args:
            for b in new_list:"""
            for a, b in zip(new_list, args):
                """print('{}/{}'.format(a, b))"""
                setattr(self, a, b)
        else:
            """.items():
            Return the dictionary's key-value pairs"""
            for a, b in kwargs.items():
                setattr(self, a, b)
