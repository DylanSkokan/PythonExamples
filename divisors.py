
# Get user input
inputNum = int(input())

# Starting at inputNum, use for loop to go down and check if modulo is 0 and print it
for i in range(inputNum, 0, -1):
    if inputNum % i == 0:
        print(str(i))
