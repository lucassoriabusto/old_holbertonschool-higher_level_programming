#!/usr/bin/python3
"""d"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """d"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        """self.width = size
        self.height = size"""
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
