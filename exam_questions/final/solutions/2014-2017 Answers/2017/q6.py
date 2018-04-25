class Parallelogram(object):
	def __init__(self, side1, side2, diagonal):
		self.side1 = side1
		self.side2 = side2
		self.diagonal = diagonal

	def get_diagonal(self):
		return self._diagonal

	def set_diagonal(self, value):
		''' set the value of the diagonal. If a negative value is given, set to 0 '''
		self._diagonal = max(value, 0)

	diagonal = property(get_diagonal, set_diagonal)

	def __str__(self):
		''' returns diagonal formatted to 2 d.p. '''
		return "{0:.2f}".format(self.diagonal)

	def __call__(self):
		''' returns True if side1, side2, and diagonal form a triangle (sum of any two sides greater than the third side) '''
		return self.side1 + self.side2 > self.diagonal \
		 and self.side1 + self.diagonal > self.side2 \
		 and self.side2 + self.diagonal > self.side1

	def calc_area(self):
		''' This is only required in the parallelogram class, as the other shapes can be generalized to the same formula '''
		s = (self.side1 + self.side2 + self.diagonal)/2.0
		area = 2 * (s * (s - self.side1) * (s - self.side2) * (s - self.diagonal)) ** 0.5
		return round(area, 2)

class Rhombus(Parallelogram):
	def __call__(self):
		''' Returns True if it's a valid rhombus, i.e. if side1 = side2 '''
		valid_para = super(Rhombus, self).__call__() # to be a valid square it has to be a valid parallelogram
		valid_rhom = self.side1 == self.side2
		return valid_para and valid_rhom
    
class Rectangle(Parallelogram):
	def __call__(self):
		''' Returns True if it's a valid rectangle, i.e. if side1^2 + side^2 = diagonal^2 (right angled triangle) '''
		valid_para = super(Rectangle, self).__call__() # to be a valid rectangle it has to be a valid parallelogram
		valid_rect = round(self.side1 ** 2.0 + self.side2 ** 2.0, 2) == round(self.diagonal ** 2.0, 2)
		return valid_para and valid_rect

class Square(Rectangle):
	def __call__(self):
		''' Returns True if it's a valid square, i.e. if side1 = side2 '''
		valid_rect = super(Square, self).__call__() # to be a valid square it has to be a valid rectangle
		valid_square = self.side1 == self.side2
		return valid_rect and valid_square

print "Test case 1"
para = Parallelogram(2,3,4)
print para

print "Test case 2"
para = Parallelogram(2,3,4)
para.diagonal = 3
print para

print "Test case 3"
para = Parallelogram(2,3,4)
para.diagonal = -1
print para

print "Test case 4"
para = Parallelogram(3,4,5)
print para()

print "Test case 5"
para = Parallelogram(3,4,8)
print para()

print "Test case 6"
rect = Rectangle(3,4,6)
print rect()

print "Test case 7"
rhom = Rhombus(3,3,2)
print rhom()

# print "Test case 7"
# rhom = Rhombus(3,4,2)
# print rhom()

print "Test case 8"
from math import sqrt
squr = Square(2,2,3)
print squr()
squr = Square(2,2,sqrt(8))
print squr()

print "Test case 9"
para = Parallelogram(3,4,2)
print para.calc_area()

print "Test case 10"
para = Parallelogram(5,7,9)
print para.calc_area()

print "Test case 11"
rect = Rectangle(3,4,5)
print rect.calc_area()

print "Test case 12"
rhom = Rhombus(3,3,4)
print rhom.calc_area()

print "Test case 13"
squr = Square(2,2,2.83)
print squr.calc_area()