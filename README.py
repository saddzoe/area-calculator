# area-calculator
# This is a calculator that measures the area of a given object.
"""
This program creates a calculator that computes the area of cirlces and triangles
"""

print("The calculator is starting up now.")

option = raw_input("Enter C for Circle or T for Triangle: ")

if option == "C":
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius ** 2
  print "Area: %f" % area
elif option == "T":
  base = float(raw_input("Enter base: "))
  height = float(raw_input("Enter height: "))
  area = 0.5 * base * height
  print "Area: %f" % area
else:
  print "This shape is invalid."

print "The calculator is shutting down."
