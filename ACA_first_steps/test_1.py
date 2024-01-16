class BankAccount:

    def __init__(self, account_number: str):

        self.account_number = account_number
        self.__balance = 0
        self.__transactions = []

    def deposit(self,ammount):
        self.__balance += ammount
        self.__transactions.append(f'Deposit: + ${ammount}ammount')

    def withdraw(self,ammount):
        if self.__balance >= ammount:
         self.__balance -= ammount
         self.__transactions.append(f'withdraw: - ${ammount}ammount')

        else:
            return 'there is no enough money'

    def transfer(self,other_account,ammount):
        self.__balance -= ammount
        other_account.__balace += ammount
        self.__transactions.append(f'Withdraw: - ${ammount} amount')
        other_account.__transactions.append(f'Deposit: + ${ammount} amount')

    def generate_statement(self):
        return f'{self.__transactions}{self.__balance}'

    def get_balance(self):
        return self.__balance

    def clear_transactions(self):
        self.__transactions.clear()
        return self.__transactions


a = BankAccount('12345',50000)
a.deposit(500)
a.withdraw(700)
a.transfer('324',15400)

print(a.clear_transactions())





