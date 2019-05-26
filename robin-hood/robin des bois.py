import math

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

Q1 = 0 # (+,+)
Q2 = 0 # (-,+)
Q3 = 0 # (-,-)
Q4 = 0 # (+,-)

for x,y in points: 
	if x>= 0 and y >0:
		Q1+=1
	elif x<0 and y >=0: 
		Q2+=1
	elif x<=0 and y<0: 
		Q3+=1
	else: 
		Q4+=1

print("il y a ",Q1,"fleches dans le cadran 1") 
print("il y a ",Q2,"fleches dans le cadran 2")
print("il y a ",Q3,"fleches dans le cadran 3") 
print("il y a ",Q4,"fleches dans le cadran 4") 

 
def distance(point1,point2):
	x1, y1 = point1 
	y2, y2 = point2
	d= (x2-x1)**2 + (y2-y1)**2
	d=math.sqrt(d)
	return d

distance_min = distance(points[0],(0,0))
point_min = points[0]

for x,y in points [1:]:
	d = distance ((x,y),(0,0))
	if d<distance_min: 
		distance_min = d
		point_min = (x,y)

print("le point le plus proche est",point_min,"et la distance",distance_min)











