# have a function accept a list as a parameter
# declare a new list
# append the first element, then append the last element of the parameter list (list.length)
# return the list


def get_list_ends(user_list):
    return [user_list[0], user_list[len(user_list) - 1]]


test = [1, 2, 3, 4, 5]
print(get_list_ends(test))


