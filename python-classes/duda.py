if type(self.__position) != tuple or type(value) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @position.setter
    def position(self, value):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int or len(value) != 2
        or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
