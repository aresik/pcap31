import math

for name in dir(math):
    print(name, end='\t')

# ceil it rouse the number upwards to be nearest integer
# floor it rouse the number downwards to be nearest integer
# trunc removes the decimal part and returns the integer number

#ceil(), floor(), trunc()
print(math.ceil(3.6))
print(math.floor(3.6))
print(math.trunc(3.6))

print("ceil of 3.1 is: ", math.ceil(3.1))
print("ceil of 3.505 is: ", math.ceil(3.505))
print("ceil of 3.945 is: ", math.ceil(3.945))
print("ceil of 3.0 is: ", math.ceil(3.0))
print("ceil of -5.4 is: ", math.ceil(-5.4))

print("floor of 3.1 is: ", math.floor(3.1))
print("floor of 3.505 is: ", math.floor(3.505))
print("floor of 3.945 is: ", math.floor(3.945))
print("floor of 3.0 is: ", math.floor(3.0))
print("floor of -5.4 is: ", math.floor(-5.4))

print("trunc of 3.1 is: ", math.trunc(3.1))
print("trunc of 3.505 is: ", math.trunc(3.505))
print("trunc of 3.945 is: ", math.trunc(3.945))
print("trunc of 3.0 is: ", math.trunc(3.0))
print("trunc of -5.4 is: ", math.trunc(-5.4))