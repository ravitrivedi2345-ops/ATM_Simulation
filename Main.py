from check_balance import display_balance
from deposite import deposit
from withdraw import withdraw
from bank_statement import show_statement
from utilis import load_account, save_account, prompt_amount


def display_menu():
    print("\n--- SIMPLE ATM MENU ---")
    print("1. Display Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Statement")
    print("5. Exit")


def main():
    account = load_account()
    print("Welcome to Simple ATM")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_balance(account)
        elif choice == "2":
            amount = prompt_amount("Enter amount to withdraw: Rs. ")
            message = withdraw(account, amount)
            save_account(account)
            print(message)
        elif choice == "3":
            amount = prompt_amount("Enter amount to deposit: Rs. ")
            message = deposit(account, amount)
            save_account(account)
            print(message)
        elif choice == "4":
            show_statement(account)
        elif choice == "5":
            save_account(account)
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
