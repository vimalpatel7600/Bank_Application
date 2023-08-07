
#bank Operation Using Oop
class Bank:
    bankname = "Abc Bank"
    Branch = "Ahmedabad."
    

    def __init__(self):
        self.li = []

            
# Useraccount
    def UserAccount(self,username,mobile, accno):
        self.username= username
        self.mobile= mobile
        self.accno= accno
        self.balance = 0
        if len(str(self.mobile)) == 10 :
            if len(str(accno)) == 3 :
                print ('''
                       For Create your new account, minimum 1000 rs is mendetory to deposite.
                       1. Deposite Amount
                       ''')
                opt = int(input("Enter your option : "))
                if opt == 1 :
                    Amount = int(input("Enter Deposite Amount : "))
                    if Amount >= 1000:
                        self.balance = self.balance + Amount
                        print ("Deposite : ", Amount)
                        print ("Balance : ", self.balance )
                        print (f"Hello {username} account is successfully created.")
                        li = [self.username, self.mobile, self.accno,self.balance]
                        self.li.append(li)
                        print(self.li)
                        with open(f".//{username}_Account.txt","w") as f:
                            f.write(f'''
                                    Name : {username}
                                    Mobile No.: : {mobile}
                                    Account No. : {accno}
                                    Balance : {self.balance}
                                ''')
            
        
                    else :
                        print('''
                            NOTE :
                            Your Deposite amount is less then of Rs 1000
                            Please deposite amount above Rs. 1000
                            ''')
                else :
                    print("Invaldi Option")
            else:
                print("Enter 3 degit account number!")
        else:    
            print ("Enetr 10 degit Mobile Numnber!")
                
      
# Deposite     
    def Deposite(self, Damount):
        self.li = self.li
        
        for i in self.li:

            if choise == int(i[2]) :
                print("Name : ",i[0])
                print("Mobile : ",i[1])
                print("Account No. : ",i[2])
                print("Balance : ",i[3])
                i[3]= i[3] + Damount
                print (f"{Damount}"," is Deposited in your account.")
                print("Current Balance : ", i[3])
                with open(f".//{username}_Account.txt","w") as f:
                            f.write(f'''
                                    Name : {username}
                                    Mobile No.: : {username}
                                    Account No. : {accno}
                                    Balance : {i[3]}
                                ''')



            else:
                print("Please! Enter Correct Account Number!")

# Withrow    
    def Withraw(self,Wamount):
        self.li = self.li
        for i in self.li:
            if choise == int(i[2]):
                print("Name : ",i[0])
                print("Mobile : ",i[1])
                print("Account No. : ",i[2])
                print("Balance : ",i[3])
                if Wamount >= i[3]:
                     print("You have insufficent balance.")
                else :
                     i[3] = i[3] - Wamount
                     print(f"Your account is withraw by rs. {Wamount}.")
                     print("Current Balance : ", i[3])
                     with open(f".//{username}_Account.txt","w") as f:
                            f.write(f'''
                                    Name : {username}
                                    Mobile No.: : {username}
                                    Account No. : {accno}
                                    Balance : {i[3]}
                                ''')
               
            else :
                print("Please! Enter Correct Account Number!")
                
# statement
    def statement(self):
        self.li = self.li
        for i in self.li:
            if choise == int(i[2]):
                print("Name : ",i[0])
                print("Mobile : ",i[1])
                print("Account No. : ",i[2])
                print("Current Balance : ",i[3])
                print('''
                      
                      ''')
                with open(f".//{username}_Account.txt","w") as f:
                    f.write(f'''
                            Name : {username}
                            Mobile No.: : {username}
                            Account No. : {accno}
                            Balance : {i[3]}

                            -: Mini Statement :-
                            
                            Deposite Amount : {Damount}
                            Withrow Amount : {Wamount}
                            
                            Your Account's last Entery!
                            ''')
               
    
                print("Deposite Amount :", Damount)
                print("Withrow Amount :", Wamount)
            else :
                print("Please! Enter Correct Account Number!")            
            
# start Codding
   
print(f"\n\n Welcome to {Bank.bankname}, {Bank.Branch}")
b = Bank()
accno = 100
while True :
    ch = int(input('''
                   1. Add A New Account 
                   2. Deposite
                   3. Withrow
                   4. Statement
                   5. Exit
                   '''))
    # Create Account
    if ch == 1 :
        username = input("Name : ")
        mobile = int(input("10 Digit Mobile No. : "))
        accno += 1
        b.UserAccount(username, mobile, accno)
        # print (f"Hello {username}, Your account is successfully created.")

    # Deposite Account
    elif ch == 2:
        choise = int(input("Enter your account no. :"))
        Damount = int(input("Enter Amount To be Deposite : "))
        b.Deposite(Damount)
           
         
    
    # Withrow Account
    elif ch == 3:
        choise = int(input("Enter your account no. :"))
        Wamount = int(input("Enter Amount To be Withdraw : "))
        b.Withraw(Wamount)
       
    
    # Statement 
    elif ch == 4 :
        choise = int(input("Enter your account no. :"))
        b.statement()
        
        
    # Exit
    elif ch == 5 :
        username = username
        print(f"Hello {username}, Thank you for connecting {Bank.bankname} :)")
        break
        