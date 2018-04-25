class Square(object):
	def __init__(self, x=0, y=0, sideLength=1.0):
		self.x = x
		self.y = y
		self.sideLength = sideLength

	def getCenter(self):
		return (self.x, self.y)

	def getSideLength(self):
		return self.sideLength

	def getArea(self):
		return self.sideLength ** 2

	def getPerimeter(self):
		return self.sideLength * 4

	def containPoint(self, px, py):
		return abs(px - self.x) <= self.getSideLength()/2 and abs(py - self.y) <= self.getSideLength()/2

	def containSquare(self, inSquare):
		# Check if each corner of inSquare is in this square
		inPos = inSquare.getCenter()
		inSide = inSquare.getSideLength()
		# p1 = (inPos[0] - inSide/2, inPos[1])
		# p2 = (inPos[0] + inSide/2, inPos[1])
		# p1 = (inPos[0], inPos[1] - inSide/2)
		# p1 = (inPos[0], inPos[1] + inSide/2)

		return self.containPoint(inPos[0] - inSide/2, inPos[1]) \
			and self.containPoint(inPos[0] + inSide/2, inPos[1]) \
			and self.containPoint(inPos[0], inPos[1] - inSide/2) \
			and self.containPoint(inPos[0], inPos[1] + inSide/2)

s= Square(x=1,y=1, sideLength=2.0)
print s.getCenter()
#(1, 1)
print s.getSideLength()
#2.0
print s.getArea()
#4.0
print s.getPerimeter()
#8.0
print s.containPoint(0,0)
#True
print s.containPoint(0,-0.5)
#False
print s.containPoint(1,1.5)
#True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1)) #True
print s.containSquare( Square(x=1.5, y = 1, sideLength = 1.1)) #False
s2 = Square()
print s2.getCenter()
#(0, 0)
print s2.getSideLength()
#1.0
print s2.getPerimeter()
#4.0
