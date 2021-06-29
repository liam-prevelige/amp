from math import sqrt

def dist(a = [], b = []):
	"""Distance between points a and b"""
	return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)