# Classe extraída do material do Real Python
# Uso didático

# property([fget=None, fset=None, fdel=None, doc=None])
# fget: A function object that returns the value of the managed attribute
# fset: A function object that allows you to set the value of the managed attribute
# fdel: A function object that defines how the managed attribute handles deletion
# doc: A string representing the property’s docstring

class Circle:

    """
    property() as a function

    """
    def __init__(self, radius):
        self._radius = radius

    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=_del_radius,
        doc="The radius property."
    )


# 
class Circle:
    """
    property() as a decorator

    You can also use property() to provide managed attributes with read-write capabilities. In practice, you just need to provide the appropriate getter (“read”) and setter (“write”) methods to your properties in order to create read-write managed attributes.
    
    For example, say you want your Circle class to have a .diameter attribute. Taking the radius and the diameter in the class initializer seems unnecessary because you can compute the one using the other.
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2