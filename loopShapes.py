size = int(input())

# square
for i in range(size):
    if i == 0 or i == size - 1:
        for j in range(size):
            print("-", end="")
    else:
        for j in range(size):
            if j == 0 or j == size - 1:
                print("-", end="")
            else:
                print(" ", end="")
    print()

# triangle
spaceTracker = size
for i in range(size):
    for j in range(spaceTracker):
        print(end=" ")
    spaceTracker = spaceTracker - 1
    for j in range(i + 1):
        print("* ", end="")
    print("")
