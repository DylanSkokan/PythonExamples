# Output common numbers between two lists

# Expected is 6, 4
list1 = [1, 2, 6, 78, 4, 1, 54, 23]
list2 = [5, 6, 8, 199, 4]

for i in range(len(list1)):
    if list2.__contains__(list1[i]):
        print(list1[i])

print()
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            print(list1[i])


