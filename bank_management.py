import random
import time
users = {}


def deposit(acc):
    while True:
        try:
            choice = float(input("Enter deposit amount greater than 0: "))
            if choice < 0:
                print("Invalid! Amount must be greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
    users[acc][2] += choice
    print(
        f"\033[92m{'*'*30}\033[00m\nAmount added successfully!\n Your Balance is {users[acc][2]:.3f}\n\033[92m{'*'*30}\033[00m"
    )


def withdraw(acc):
    balance = users[acc][2]
    while True:
        try:
            amount = float(
                input(f"Enter withdraw amount (0 < amount ≤ {balance:.3f}): ")
            )
            if amount < 0:
                print("Amount must be greater than zero.")
            elif amount > balance:
                print(f"\033[91mInsufficient funds. You have {balance:.3f}.\033[00m")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a number.")
    users[acc][2] -= amount
    print(
        f"{'*'*30}\nWithdraw successful!\nYou have {users[acc][2]:.3f} left.\n{'*'*30}\n"
    )


def menu(acc):
    print(f"Balance: {users[acc][2]:.3f}")
    while True:
        print("1. Deposit\n2. Withdraw\n3. Change password\n4. Exit\n")
        try:
            choice = int(input("Enter choice [1-4]: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        if choice == 1:
            deposit(acc)
        elif choice == 2:
            withdraw(acc)
        elif choice == 3:
            new_pin = input("Enter new password: ")
            users[acc][0] = new_pin
            print(
                f"\033[92m{'*'*30}\033[00m\nPassword changed successfully.\n\033[92m{'*'*30}\033[00m\n"
            )
        else:
            return


def create():
    account_number = random.randint(50, 100)
    while account_number in users.keys():
        account_number = random.randint(50, 100)
    name = input("Enter Name: ")
    password = input("Enter password: ")
    users[account_number] = [password, name, 0]
    print(
        f"\033[92m{'*'*30}\033[00m\nAccount created successfully!\nYour Account details are:\n\nName of Account: {name}\nPassword:{password}\nAccount Number:{account_number}  [Important note: Don't Forget your Account number, it will be required for login!!!]\n\033[92m{'*'*30}\033[00m\n"
    )


def login():
    print("\n1. Show Details:\n2. Exit\n")
    try:
        choice = int(input("Enter number[1 or 2]: "))
    except ValueError:
        print("Invalid input! Please enter 1 or 2.")
        return
    if choice == 1:
        try:
            acc = int(input("Enter account number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            return
        if acc in users:
            i = 0
            while i < 3:
                password = input("Enter Password: ")
                if password == users[acc][0]:
                    print(f"\n\033[33m{'*'*5} Welcome {users[acc][1]}! {'*'*5}\033[0m")
                    menu(acc)
                    break
                else:
                    print(
                        f"\033[91mInvalid password! You have {2 - i} attempt(s) left.\033[00m"
                    )
                    i += 1
            else:
                print("\033[91mToo many failed attempts. Access denied.\033[00m")
        else:
            print("\033[91mAccount number not found!\033[00m")
            return

    else:
        return


def main():
    while True:
        print(
            f"\033[33;40m{'<'*10}\033[0m\033[34;47mBank System!\033[0m\033[33;40m{'>'*10}\033[0m"
        )
        print("\n1. Create New Account\n2. Login to existing Account\n3. Exit\n")
        try:
            choice = int(input("Enter[1-3]: "))
        except ValueError:
            print("Invalid input! Please Enter a number between 1 and 3.")
            continue
        if choice == 1:
            create()
        elif choice == 2:
            login()
        elif choice == 3:
            print("\033[34;40mClosing System...\033[0m")
            break
        else:
            print("Invalid!")


if __name__ == "__main__":
    main()
