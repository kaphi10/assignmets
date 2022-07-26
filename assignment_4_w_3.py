# week 3 Lession 4 assignment
class Bank_account:
    MIN_BALANCE=500
    def __init__(self, first_name, last_name,bal):
        self.first_name= first_name
        self.last_name=last_name
        self.bal=bal
    def name(self):
        return '{} {}'.format(self.first_name,self.last_name)
        

    def deposit(self, deposit):
        self.balance = Bank_account.MIN_BALANCE + deposit + self.bal
        return self.balance 
    def withraw(self,with_amount):
        #self.with_amount=with_amount
        self.balance= self.bal + Bank_account.MIN_BALANCE
        #self.amount= with_amount-Bank_account.MIN_BALANCE

        if with_amount < self.bal and Bank_account.MIN_BALANCE:
            self.balance= self.balance-with_amount
            #self.r_balance= self.balance-with_amount
           # print('insufficient amountto withdrawl the available balance is',self.balance)
        #elif self.balance <= Bank_account.MIN_BALANCE:
        else:
            print ('insufient amount')
        
            # self.r_balance= self.bal-with_amount
            # self.amount=self.r_balance + Bank_account.MIN_BALANCE
            # return self.amount

            
    
customer1=Bank_account(first_name='Amina', last_name='Abubakar',bal=2200)
customer1.deposit(5000)
print('Welcome',customer1.name() + ' :' + 'The available balance is:', customer1.balance)
customer1.withraw(2000)
print('Welcome',customer1.name() + ' :' + 'The available balance is:', customer1.balance)

