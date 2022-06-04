# create seed for random
import random
# password should contain a mix of characters


def generate_password(pass_length):
    password = ""
    for i in range(pass_length):
        password += chr(random.randint(33, 125))
    return password


user_length = int(input("How long do you want the password to be?"))
print(generate_password(user_length))

