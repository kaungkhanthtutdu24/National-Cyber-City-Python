#For second assignment
import os

class MiniBank:
    user_counter: int = 1  #  keep track of user IDs
    transaction_counter: int = 1  # keep track of transaction IDs
    user_file = "userlist.txt"

    def __init__(self):
        self.load_users_from_file()

    def firstOption(self):
        option: int = int(input("Press 1 to Login:\nPress 2 to Register:\n"))
        if option == 1:
            self.login()
        elif option == 2:
            self.register()
        else:
            print("Invalid option. Please try again.")

    def returnId(self, transfer_username):
        with open(self.user_file, "r") as f:
            for line in f:
                user_id, username, passcode, amount = line.strip().split(",")
                if username == transfer_username:
                    return int(user_id)
        return None

    def menu(self, loginId):
        while True:
            menu_input = int(input(
                "Press 1 to Transfer:\nPress 2 to Withdraw:\nPress 3 to Update User Data:\nPress 4 to View Balance:\nPress 5 to Logout:\n"))
            if menu_input == 1:
                self.transfer(loginId)
            elif menu_input == 2:
                self.withdraw(loginId)
            elif menu_input == 3:
                self.updateUserData(loginId)
            elif menu_input == 4:
                self.viewBalance(loginId)
            elif menu_input == 5:
                print("Logging out...")
                break
            else:
                print("Invalid option. Please try again.")

    def login(self):
        print("\n_______Login__________\n")
        l_username: str = input("Enter username to login: ")
        l_userpasscode: int = int(input("Enter passcode to login: "))
        loginId = self.returnId(l_username)
        if loginId is not None and self.check_passcode(loginId, l_userpasscode):
            print(f"Login Successful. User ID: {loginId}")
            self.menu(loginId)
        else:
            print("Invalid username or passcode. Please try again.")

    def register(self):
        print("\n___________Register_________\n")
        r_username: str = input("Enter username to register: ")

        # Check if username already exists
        if self.returnId(r_username) is not None:
            print("Username already exists. Please try a different username.")
            return

        r_amount: int = int(input("Enter amount: "))
        r_passcode1: int = int(input("Enter passcode to register: "))
        r_passcode2: int = int(input("Enter passcode again to confirm: "))

        if r_passcode1 == r_passcode2:
            user_id: int = self.user_counter
            self.user_counter += 1
            self.write_user_to_file(user_id, r_username, r_passcode2, r_amount)
            print(f"#### Successfully Registered! ####\nUser ID: {user_id}\n")
        else:
            print("Passcodes do not match. Please try again.")

    def transfer(self, from_user_id):
        # Check if there are at least two users
        if self.check_user_count() < 2:
            print("Transfer not possible. Only one user exists.")
            return

        transfer_username: str = input("Enter username to transfer to: ")
        transfer_id: int = self.returnId(transfer_username)
        if transfer_id is None:
            print("Recipient username not found.")
            return

        amount: int = int(input(f"Enter amount to transfer to {transfer_username}: "))
        if self.get_balance(from_user_id) >= amount:
            self.update_balance(from_user_id, -amount)
            self.update_balance(transfer_id, amount)
            transaction_id = self.transaction_counter
            self.transaction_counter += 1
            print(f"Transfer successful. Transferred {amount} to {transfer_username}.")
            print(f"Transaction ID: {transaction_id}")
            print(f"Transferee User ID: {from_user_id}, Receiver User ID: {transfer_id}")
        else:
            print("Insufficient funds.")

    def withdraw(self, user_id):
        amount: int = int(input("Enter amount to withdraw: "))
        if self.get_balance(user_id) >= amount:
            self.update_balance(user_id, -amount)
            print(f"Withdrawal successful. Amount: ${amount}")
        else:
            print("Insufficient funds.")

    def updateUserData(self, user_id):
        new_username: str = input("Enter new username: ")
        new_passcode: int = int(input("Enter new passcode: "))
        self.update_user_data(user_id, new_username, new_passcode)
        print("User data updated successfully.")

    def viewBalance(self, user_id):
        balance = self.get_balance(user_id)
        print(f"Current balance: ${balance}")

    def check_passcode(self, user_id, passcode):
        with open(self.user_file, "r") as f:
            for line in f:
                uid, username, user_passcode, amount = line.strip().split(",")
                if int(uid) == user_id and int(user_passcode) == passcode:
                    return True
        return False

    def get_balance(self, user_id):
        with open(self.user_file, "r") as f:
            for line in f:
                uid, username, passcode, amount = line.strip().split(",")
                if int(uid) == user_id:
                    return int(amount)
        return 0

    def update_balance(self, user_id, amount_change):
        users = []
        with open(self.user_file, "r") as f:
            for line in f:
                uid, username, passcode, amount = line.strip().split(",")
                if int(uid) == user_id:
                    amount = str(int(amount) + amount_change)
                users.append(f"{uid},{username},{passcode},{amount}\n")

        with open(self.user_file, "w") as f:
            f.writelines(users)

    def update_user_data(self, user_id, new_username, new_passcode):
        users = []
        with open(self.user_file, "r") as f:
            for line in f:
                uid, username, passcode, amount = line.strip().split(",")
                if int(uid) == user_id:
                    username = new_username
                    passcode = str(new_passcode)
                users.append(f"{uid},{username},{passcode},{amount}\n")

        with open(self.user_file, "w") as f:
            f.writelines(users)

    def write_user_to_file(self, user_id, username, passcode, amount):
        with open(self.user_file, "a") as f:
            f.write(f"{user_id},{username},{passcode},{amount}\n")

    def load_users_from_file(self):
        if not os.path.exists(self.user_file):
            with open(self.user_file, "w") as f:
                pass

    def check_user_count(self):
        with open(self.user_file, "r") as f:
            return sum(1 for _ in f)

if __name__ == "__main__":
    miniBank: MiniBank = MiniBank()
    while True:
        miniBank.firstOption()
