accountList = []


def sort_accounts(self):
    min_index = 0
    for i in len(accountList):
        min_index = i
        for j in range(min_index, len(accountList)):
            if accountList > accountList.index(j):
                i = j


class AccountData:
    def __init__(self, user_num, user, password):
        self.user_num = user_num
        self.user = user
        self.password = password
        accountList.append(self)

    def __str__(self):
        return "ID: " + str(self.user_num) + ", Name: " + self.user + "\n"

    def get_user_num(self):
        return self.user_num