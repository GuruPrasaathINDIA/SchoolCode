class bankaccount:
	def _init_(self):
		self.balance=0
	def deposit(self,amount):
		self.balance+=amount
	def withdraw(self,amount):
		if amount>self.balance:
			return 'Insufficient Balance'
		self.balance-=amount
		return self.balance

ac2001=bankaccount()
ac2001.deposit(11000)
print('balance:',ac2001.balance)
ac2001.withdraw(3000)
print('balance2:',ac2001.balance)
