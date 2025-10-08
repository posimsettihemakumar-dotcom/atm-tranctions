balance = 0

while True:
    print("\n1. Withdraw")
    print("2. Deposit")
    print("3. Balance")
    print("4. Exit")
    
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        mny = int(input("Enter amount to withdraw: "))
        if mny % 100 == 0 or mny % 500 == 0:
            if mny <= balance:
                balance -= mny
                print(f"Please collect your money: {mny}")
                print(f"Remaining balance: {balance}")
            else:
                print("Not enough balance!")
        else:
            print("Enter a valid amount (multiples of 100 or 500).")
    
    elif ch == 2:
        deposite = int(input("Enter amount to deposit: "))
        balance += deposite
        print(f"Amount deposited: {deposite}")
        print(f"Current balance: {balance}")
    
    elif ch == 3:
        print(f"Your current balance is: {balance}")
    
    elif ch == 4:
        print("Thank you, visit again!")
        break
    
    else:
        print("Invalid choice. Please try again.")

