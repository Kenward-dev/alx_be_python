class BankAccount:
    def __init__(self, initial_balance = 0):
        self.__account_balance = int(initial_balance)

    def deposit(self, amount):
        self.__account_balance += int(amount)

    def withdraw(self, amount):
        if int(amount) <= self.__account_balance:
            self.__account_balance -= int(amount)
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")
