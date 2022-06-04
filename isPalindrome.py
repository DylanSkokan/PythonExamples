# Keep asking user to enter a string as long as it isnt exit
# if the string entered is a palindrome, display true, else display false
# ask for another string

def is_palindrome(user_str):
    reversed_string_loop = ""

    # loop solution
    for i in range(len(userStr) - 1, -1, -1):
        reversed_string_loop += user_str[i]

    # splicing solution
    # reversed_string_splice = user_str[::-1]
    # print(reversed_string_splice)

    if reversed_string_loop == user_str:
        return 1
    else:
        return 0


userStr = ""
while userStr != "exit":
    print("Enter a string to check if it is a palindrome:")
    userStr = input()

    palindromeCheck = is_palindrome(userStr)
    if palindromeCheck == 1:
        print("true")
    elif palindromeCheck == 0:
        print("false")


