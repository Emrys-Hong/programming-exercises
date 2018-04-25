import math

class Point2D(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return 'Point2D(' + str(self.x) + ',' + str(self.y) + ')'

	def add(self, v):
		return Point2D(self.x + v.dx, self.y + v.dy)

class Vector2D(object):
	def __init__(self, dx, dy):
		self.dx = dx
		self.dy = dy

	def length(self):
		return math.sqrt(self.dx**2 + self.dy**2)

class Polyline2D(object):
	def __init__(self, start, vectors):
		self.start = start
		self.vectors = vectors

	def addSegment(self, v):
		''' adds a line segment to the end of the polyline '''
		self.vectors.append(v)

	def length(self):
		''' returns the total length of the polyline, which is the sum of the lengths of the segments '''

		totalLength = 0
		for v in self.vectors:
			totalLength += v.length()

		return totalLength

	def vertex(self, index):
		vertexPoint = self.start
		for i in range(index):
			vertexPoint = vertexPoint.add(self.vectors[i])

		return vertexPoint

class ClosedPolyline2D(Polyline2D):
	def length(self):
		totalLength = super(ClosedPolyline2D, self).length()

		# Get coordinate of last vertex
		lastVertex = self.vertex(len(self.vectors))
		totalLength += math.sqrt((lastVertex.x - self.start.x) ** 2 + (lastVertex.y - self.start.y) ** 2)

		return totalLength

# p =  Point2D(1,2)
# v = Vector2D(3,1)
# q = p.add(v)
# print q

# pline = Polyline2D(Point2D(1,2), [Vector2D(3,1)])
# pline.addSegment(Vector2D(1,0))
# pline.addSegment(Vector2D(0,2))
# print pline.length()
# print pline.vertex(0)
# print pline.vertex(1)
# print pline.vertex(2)
# print pline.vertex(3)

cpline = ClosedPolyline2D(Point2D(1,2), [Vector2D(3,1)])
cpline.addSegment(Vector2D(1,0))
cpline.addSegment(Vector2D(0,2))
print cpline.length()