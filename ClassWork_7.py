#!/usr/bin/python
class Figure:
    def __init__ (self, color):
        self.color = (color)
    def __repr__ (self):
        return "Figure is (%s) in color" % self.color

P = Figure("red")
print(P)
#get_color()