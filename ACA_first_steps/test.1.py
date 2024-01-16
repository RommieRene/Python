class BankAccount:

    def __init__(self, account_number: str, balance: int = 0):

        self.account_number = account_number
        self.__balance = balance
        self.__transactions = []


    def deposit(ammount):
        self.__balance += ammount
        self.__transactions.append(f'Deposit: + ${ammount}ammount')

    def withdraw(ammount):
        if self.__balance >= ammount:
         self.__balance -= ammount
         self.__transactions.append(f'withdraw: - ${ammount}ammount')

print(type(BankAccount))
    # def account_number(self,number:str):
    #     _number = number
    #
    #
    # def balance(self,_balance = 0):
    #
    # def transactions(self,deposit,withdraw,transfer):
    #     self.deposit = [deposit]
    #     self.withdraw = [withdraw]
    #     self.transfer = [transfer]


