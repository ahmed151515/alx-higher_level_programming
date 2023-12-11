#!/usr/bin/python3
"""_summary_"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.width

    @size.setter
    def size(self, value):
        """_summary_

        Args:
            value (_type_): _description_
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """_summary_"""
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except:
            pass
        try:
            for key, value in kwargs.items():
                setattr(self, key, value)
        except:
            pass

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """_summary_"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y
        }
