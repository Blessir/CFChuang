# triangle_area.py
import math
def testfun(a,b,c):
	sides = (a+b+c) / 2
	area = math.sqrt(sides * (sides  - a) * (sides  - b) * (sides  - c))
	return area