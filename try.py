from account import Account
from decimal import Decimal

account1 = Account('chuench',Decimal('1000.00'))
##account2 = Account('Zool',Decimal('-50.00'))


account1.deposit(Decimal(200000))              ##Deposit RM2000
##account2.deposit(Decimal(-25))
account1.withdraw(Decimal(10))             ##withdraw RM10

print (account1.name)
print (account1.balance)                   ##1000+200000-10=200990
