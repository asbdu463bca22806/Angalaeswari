claclass Player:
  def play(self):
    print("The player is playing cricket.")

class Batsman(Player):
  def play (self):
    print("The batsman is batting.")

class Bowler(Player):
  def play(self):
    print("The bowler is bowling.")

batsman = Batsman()
bowler = Bowler()
batsman.play()
bowler.play()ss BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
     self.__account_number = account_number
     self.__account_holder_name = account_holder_name
     self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
     self.__account_balance += amount
     print("Deposited â‚¹{}.New balance: â‚¹{}".format (amount, self.__account_balance))
    else:
     print("Invalid deposit amount.")
  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
     self.__account_balance -= amount
     print("Withdrew â‚¹{}.New balance: â‚¹{}".format(amount, self.__account_balance))
    else:
     print("Invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
   print("Account balance for {} (Account #{}): â‚¹{}". format(self.__account_holder_name, self.__account_number, self.__account_balance)) 
account = BankAccount(account_number="123456789", account_holder_name="Hari Prabu", initial_balance=5000.0)
#Test deposit and withdrawal functionality
account.display_balance() 
account.deposit(500.0) 
account.withdraw(200.0) 
#account.display_balance () LinearSearchProduct(productlist,targetProduct):
    indices=[]
    
    for index,product in enumerate(productlist):
        if product==targetProduct:
            indices.append(index)
    return indices
products=["shoes","boot",
          "loafer","shoes", 
          "sandal","shoes"]
target="shoes"
target2='apple'
result=LinearSearchProduct(products,target)
print(result)