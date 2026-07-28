"""
Sometimes, you need to keep track of what your code does and how your programs flow. A way to do that in Python is to use logging. This module provides all the functionality you require for logging your code. It allows you to constantly watch the code and generate useful information about how it works.

If you ever need to keep track of how and when you access and mutate a given attribute, then you can take advantage of property() for that, too:
"""

import logging

logging.basicConfig(
    format="%(asctime)s: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S"
)

class Circle_:
    def __init__(self, radius):
        self._msg = '"radius" was %s. Current value: %s'
        self.radius = radius

    @property
    def radius(self):
        logging.info(self._msg % ("accessed", str(self._radius)))
        return self._radius

    @radius.setter
    def radius(self, value):
        try:
            self._radius = float(value)
            logging.info(self._msg % ("mutated", str(self._radius)))
        except ValueError:
            logging.info('validation error while mutating "radius"')