import accountInfo
from accountInfo import AccountData

acc1 = AccountData(1, "Dylan", "password")
acc1 = AccountData(6, "Mike", "password")
acc1 = AccountData(3, "Jerry", "password")

print(*accountInfo.accountList)

