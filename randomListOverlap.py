import random

# first parameter is range of random nums, next is size of returned list of random nums
list1 = random.sample(range(15), 15)
list2 = random.sample(range(15), 15)

inBoth = [i for i in list1 if i in list2]
print("inBoth")
print(inBoth)
