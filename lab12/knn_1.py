import numpy as np

data = np.array([	[ 6.0 , 7.0],
					[ 2.0 , 3.0],
					[ 3.0 , 7.0],
					[ 4.0 , 4.0],
					[ 5.0 , 8.0],
					[ 6.0 , 5.0],
					[ 7.0 , 9.0],
					[ 8.0 , 5.0],
					[ 8.0 , 2.0],
					[10.0 , 2.0]])

def euclidean_distance(p1, p2):
	dx = float(p1[0]-p2[0])
	dy = float(p1[1]-p2[1])
	d = np.power(dx,2) + np.power(dy,2)
	return np.sqrt(d)

print("\nAll Euclidean Distance from point: ",data[0], "\n")
for point in data:
	distance = euclidean_distance(data[0], point)
	print(distance)
