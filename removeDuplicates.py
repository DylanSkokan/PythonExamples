# given a single list, remove duplicates in the list
def loop_remove_dupe(user_list):
    new_list = []
    for i in range(len(user_list)):
        if new_list.__contains__(user_list[i]) is False:
            new_list.append(user_list[i])
    return new_list


def set_remove_dupe(user_list):
    return set(user_list)


the_list = [1, 4, 6, 6, 6, 8, 9]
print(loop_remove_dupe(the_list))
print(set_remove_dupe(the_list))

