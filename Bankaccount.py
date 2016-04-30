# This is the code for a simple BankAccount

class BankAccount(object):
	balance = 0
	def __init__(self, name):
		self.name = name   
	
	def __repr__(self):  
		return "This is %s's account. The balance is $%.2f" % (self.name, self.balance)

	def show_balance(self):	
		print "This is your balance, $%.2f" % (self.balance) 
    
	def deposit(self, amount):  
		if amount < 0:
			print "Error! Your input should be positive."      
			return 
		else:
			print "This is your balance, $%.2f" % (self.balance)   
			self.balance += amount
			self.show_balance()		
      
	def withdrow(self, amount):     
		if amount > self.balance:    
			return "You are withdrowing more than your balance."
		else:
			self.balance -= amount
			self.show_balance() 
      
my_account = BankAccount("Yoshi")
print my_account.__repr__()
print my_account.show_balance()
print my_account.deposit(2000)
print my_account.withdrow(1000)
print my_account.__repr__()