class Bank:
    def __init__(self,accNo,name,typ,bal):
        self.acc=accNo
        self.n=name
        self.t=typ
        self.b=bal
    def deposit(self,amt1):
        self.b+=amt1
        print("Balance:",self.b)
    def withdraw(self,amt2):
        if self.b<amt2:
            print("insufficient balance")
        else:
            self.b-=amt2
            print("Balance:",self.b)
    def display(self):
        print('\n accNo:',self.acc,'\n account holder name:',self.n,'\nacc type:,self.t,'\nbalance:',self.b)
print("***menu***")
print("1.deposit")
print("2.withdraw")
print("3.display")
print("4.exit")
b1=Bank(1002,"nidhi","savings",0)
b1.display()
while True:
   choice=int(input("\n enter your choice (1-4):"))
   if choice==1:
       d=int(input("enter amount to be deposited:"))
       b1.deposit(d)
   elif choice==2:
       w=int(input("enter amount to be withdraw:"))
       b1.withdraw(w)
   elif choice==3:
       b1.display()
   elif choice>4:
       print("enter a valid choice")
   else:
      break;
              
              
