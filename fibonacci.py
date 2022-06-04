# use a function called getFib
# depending on the len, it can do different things

# if len = 0, append 1. If len = 1, append 1. If len is 2 or greater, get
# the number at len and the number before len, add them, and append that number

def get_fib(fib_seq, num_of_fib):
    if num_of_fib > len(fib_seq):
        if len(fib_seq) == 0 or len(fib_seq) == 1:
            fib_seq.append(1)
        else:
            fib_seq.append(fib_seq[len(fib_seq) - 1] + fib_seq[len(fib_seq) - 2])

        get_fib(fib_seq, num_of_fib)

    return fib_seq


numOfFib = int(input("How many fib numbers would you like to generate?"))
print(get_fib([], numOfFib))
