# program to calculate the volume of a sphere given the radius

#radius input and calculates the volume 4/3pi r 3  use math library for pi and ans in 2dp#
import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3 )* math.pi * math.pow(radius,3)

print(f"the volume o fthe sphere is {volume:.2f}")
