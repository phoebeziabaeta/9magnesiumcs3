class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number__ = account_number
        self.balance = float(balance)

    def set_account_number(self, account_number):
        print(f"Account Number: {account_number}")
        self.__account_number__ = account_number

    def set_balance(self, balance):
        bal = float(balance)
        if bal >= 0:
            self.balance = bal
            print(f"Balance: {self.balance}")
        else:
            print("The balance must not be a negative number.")
        return bal

    def get_account_number(self):
        print(f"Account Number: {self.__account_number__}")

    def get_balance(self):
        print(f"Balance: {self.balance}")

a1 = BankAccount("12345", 1000)
print("Output:")
print("")
print("Account 1")
a1.set_account_number("123456789")
a1.set_balance(1000)
print("")
a1.set_balance(-100)
a1.get_account_number()
a1.get_balance()
