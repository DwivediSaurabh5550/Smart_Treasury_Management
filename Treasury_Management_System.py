class person():
    def __init__(self,ID,name):
        self.ID = ID
        self.name = name

class User(person):
    def __init__(self,ID,name,bal):
        super().__init__(ID,name)
        self.__balance = bal

    def deposit(self,amount):
        if amount >0:
            self.__balance += amount
            return self.__balance
        else:
            print("Invalid deposit amount!")

    def withdraw(self,amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

    def display(self):
        print(f"ID: {self.ID} Name: {self.name} Balance: ₹{self.__balance}")

class Manager:
    def __init__(self):
        self.__data = {}

    def check_pin(self,pin):
        return pin == 9099

    def add_user(self,ID,name,balance):
        if ID in self.__data:
            print("User already exists.")
        else:
            self.__data[ID] = User(ID, name, balance)
            print(f"User {name} added.")
    def remove_user(self,ID):
        if ID in self.__data:
            removed = self.__data.pop(ID)
            print(f"User {removed.name} removed.")
        else:
            print("User not found.")

    def info(self):
        print("Each User Details:")
        for user in self.__data.values():
            user.display()

    def total_bal(self):

        total = sum(n.get_balance() for n in self.__data.values())
        print(f"Total Managerial Balance: ₹{total}")

    def deposit_money(self,ID,amount):

        res = self.__data[ID].deposit(amount)
        print(f"{self.__data[ID].name} Successfully Deposited ₹{amount} ,Total Balance: ₹{res}")

    def withdraw(self,ID,bal):
        res = self.__data[ID].withdraw(bal)
        print(f"{self.__data[ID].name} Successfully Withdrew ₹{bal} ,Total Balance: ₹{res}")

    def deduct_all(self,bal):
        for user in self.__data.values():
            user.withdraw(bal)
        print("Successfully Withdrew from each account")

    def balance(self,ID):
        if ID in self.__data:
            print(f"{self.__data[ID].name} your total balance: {self.__data[ID].get_balance()}")
        else:
            print("User not exist")

#  Main Execution  Part

u1 = Manager()
u1.add_user(114,'SAURABH',1000)
u1.add_user(116,'NAVNEET',1000)
u1.add_user(118,'ANSHUMAN',1000)
u1.add_user(120,'KISHAN',1000)
u1.add_user(122,'ANKIT',1000)
u1.add_user(124,'RISHI',1000)
def excution():
    limit = 3
    while limit > 0:
        if u1.check_pin(int(input("Hello Manager \nWelcome to Treasury Management System\nEnter your pin: "))):
            while True:
                try:
                    menu = int(input("\nCheck..\n1. Each User Information \n2. Total Managerial Balance\n3. Deposit to wallet\n4. Withdraw from your wallet\n5. Deduct from each account\n6. Add New User\n7. Remove User\n8. Exit\n..."))
                    if menu == 1:
                        u1.info()
                    elif menu == 2:
                        u1.total_bal()
                    elif menu == 3:
                        u1.deposit_money(int(input("Enter id: ")),int(input('Balance: ')))
                    elif menu == 4:
                        u1.withdraw(int(input("Enter id: ")),int(input('Balance: ')))
                    elif menu == 5:
                        u1.deduct_all(int(input('Balance: ')))
                    elif menu == 6:
                        u1.add_user(int(input("Enter id: ")),input("Enter Name: "),int(input('Balance: ')))
                    elif menu == 7:
                        u1.remove_user(int(input("Enter id: ")))
                    elif menu == 8:
                        print("Thank you for using the system.")
                        return
                    else:
                        print("Invalid option.")
                except Exception as e:
                        print("Error:", e)
        else:

                print("You have entered wrong pin")
                limit -= 1
                print(f"Wrong PIN. Attempts left: {limit}")
                if limit == 0:
                    print("Access Denied. Please try later.")
                    break

def operation():
    while True:
        n = int(input("1. Manager \n2. User \nChoose your role: \n..."))
        if n == 1:
            excution()
        elif n == 2:
            ch = int(input("1. Check Balance \n2. Deposit \n3. Exit \n..."))
            if ch == 1:
                u1.balance(int(input("Enter ID: ")))
            elif ch == 2:
                u1.deposit_money(int(input("Enter ID: ")),int(input("Balance: ")))
            elif ch == 3:
                return
            else:
                print("Invalid input")
operation()