import math
r = float(input("Enter radius of the circle:"))
cir=2*math.pi*r

area=math.pi*(r**2)
area=round(area,2)
print('Area of a circle is :',area)
cir=round(cir,2)
print('Circumference of a circle :',cir)
