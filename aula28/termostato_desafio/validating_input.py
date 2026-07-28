"""
Validating input is one of the most common use cases of property() and managed attributes. Data validation is a common requirement in code that takes input from users or other sources that you could consider untrusted. Python’s property() provides a quick and reliable tool for dealing with input validation.

For example, getting back to the Point class, you may require the values of .x and .y to be valid numbers. Since your users are free to enter any type of data, you need to make sure that your points only accept numbers.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError('"y" must be a number') from None