class User:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.account_balance = 0

    def greeting(self):
        print(f"Hello my name is {self.first_name}!")

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self, amount):
        self.account_balance = amount



robert = User("Robert", "Seffens", 38)
jennifer = User("Jennifer", "Anniston", 53)
rachel = User("Racheal", "Green", 25)

# robert.greeting()

robert.make_deposit(50)
robert.make_deposit(300)
robert.make_deposit(100000)
robert.make_withdrawl(50750)
print(f"Robert's balance is ${robert.account_balance}")


jennifer.make_deposit(20000000)
jennifer.make_deposit(350050)
jennifer.make_withdrawl(3500000)
jennifer.make_withdrawl(5)
print(f"Jennifer's balance is ${jennifer.account_balance}")

rachel.make_deposit(2500)
rachel.make_withdrawl(300)
rachel.make_withdrawl(2100)
rachel.make_withdrawl(99)
print(f"Racheal's balance is ${rachel.account_balance}")
