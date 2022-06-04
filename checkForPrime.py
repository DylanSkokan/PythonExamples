userNum = int(input())
isPrime = 1

# start from half of userNum, go down to find a mod 0 num
for i in range(userNum - 1, 2, -1):
    if userNum % i == 0:
        isPrime = 0
        break

if isPrime == 1:
    print("It is prime")
else:
    print("NOT prime")

