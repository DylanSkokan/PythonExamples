# create a function that returns a reverse of that string
# use a for loop backwardly appending chars to new string

def reverse_string(user_str):
    str_reversed = ""
    for i in range(len(user_str) - 1, -1, -1):
        str_reversed += user_str[i]
    return str_reversed


print(reverse_string("hello"))



