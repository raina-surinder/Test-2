name = input("Please enter your name: ")
income = int(input("Plesae enter your income: "))
tax = int(input("Please enter your tax: "))
salary = income-tax
if salary>80: 
    print(name, "is rich")
else:
    print(name, "is poor")