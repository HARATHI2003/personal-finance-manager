from auth import login_user, register_user
from transactions import add_transaction, generate_report
from database import initialize_database

def main():
    initialize_database()  # Ensure database is initialized
    print("Welcome to the Personal Finance Manager!")
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            register_user(username, password)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            user_id = login_user(username, password)

            if user_id:
                print(f"Login successful! Welcome, {username}.")
                user_menu(user_id)
            else:
                print("Login failed. Please try again.")
        
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

def user_menu(user_id):
    while True:
        print("\n1. Add Transaction")
        print("2. Generate Monthly Report")
        print("3. Generate Yearly Report")
        print("4. Logout")
        choice = input("Select an option: ")

        if choice == '1':
            trans_type = input("Enter transaction type (income/expense): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_transaction(user_id, trans_type, category, amount, date)
            print("Transaction added successfully!")
        
        elif choice == '2':
            report = generate_report(user_id, period='monthly')
            print(f"Monthly report total: {report}")
        
        elif choice == '3':
            report = generate_report(user_id, period='yearly')
            print(f"Yearly report total: {report}")
        
        elif choice == '4':
            print("Logging out.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
