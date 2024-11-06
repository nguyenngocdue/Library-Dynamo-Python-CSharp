class Point:
	def __init__(self, x,y,z):
		self.x = x
		self.y = y
		self.z = z
	
	def createPoint(self):
		return Point.ByCoordinate(self.x, self.y, self.z)
	
	def offsetPointByDistance(self, offset):
		return Point.ByCoordinate(self.x + offset, self.y + offset, self.z + offset)