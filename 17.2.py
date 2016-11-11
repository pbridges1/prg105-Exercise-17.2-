class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print "The X coordinate is %d" % self.x, "and the Y coordinate is %d" % self.y
"""
   Represents point in space
"""

points = Point(11, 16)
