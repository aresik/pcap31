import random

print(random.random())
print(random.random())
print(random.random())

# using a seed the numbers will always be the same 

random.seed(0)
print(random.random())
print(random.random())
print(random.random())


# using choice, an element in the list will be returned
numbers = [ 1,2,3,4,5,6,7,8,10]
names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']

print(random.choice(numbers))
print(random.choice(names))

# returning random values from a list. these can be duplicate
numbers = [ 1,2,3,4,5,6,7,8,10]
for i in range(10):
    print(random.choice(numbers))

# sample will return unique values

names = ['Alan', 'Kate', 'Mary', 'Kate', 'Jo', 'John']
random.sample(names , 3)
