#for first assignment

class MiniBank:

    main_userInfo:dict = {}

    def firstOption(self):
        option :int = int(input("Press1 to Login:\n Press2 to Register:"))
        if(option==1):
            self.login()
        else:
            self.register()

    def returnId(self, transfer_username) :
        userInfo_length :int =len(self.main_userInfo)
        for i in userInfo_length:
            if self.main_userInfo[i]["r_username"]==transfer_username:
                return i
        return None
    def menu (self, loginId):
        menu_input=int(input("Press1 to Transfer: \nPress 2 to Withdraw: \nPress 3 to update user data: "))
        if menu_input ==1:
            transfer_username:str=input("Pls enter username to transfer")
            transfer_id:int=self.returnId(transfer_username)
            print("\n\nWE get to Transer id:", transfer_id)
            print("myId",loginId)
            
            amount:int =int(input("Enter mount to transfer {0}:".format(self.main_userInfo[transfer_id]["r_username"])))
            print("Amount is:",amount)

    def login(self) :
        print ("\n_______This is from login__________\n")
        l_username:str = input("Pls enter user name to login:")
        l_userpasscode:int = int(input("Pls enter passcode to login:"))
        exitUser = self.exitUser(l_username,l_userpasscode)
        if(exitUser):
            print("LoginSuccessful")
            loginId:int = self.returnId(l_username)
            self.menu(loginId)

        else:
            print("You can't login")


    def exitUser(self,l_username,l_passcode):
        user_count = len(self.main_userInfo)
        for i in range(1,user_count+1): #start stop step
            if self.main_userInfo[i]["r_username"]==l_username and self.main_userInfo[i]["r_passcode"]==l_passcode:
                return True
            return False

        
    def register(self):
        print("\n___________This is from register_________\n")
        r_username:str = input("Pls enter username to register:")
        r_amount:int = int(input("Enter amount:"))
        r_passcode1:int = int(input("Pls enter passcode to register:"))

        r_passcode2: int = int(input("Pls enter again passcode to com:"))

        if (r_passcode1 == r_passcode2):
            id:int =self.checkingUserCount()
            userInfoForm: dict = {id:{"r_username":r_username,"r_passcode":r_passcode2, "amount":r_amount}}
            self.main_userInfo.update(userInfoForm)
            print("#### Success Registered! ####\n\n")
            print(self.main_userInfo)

    def checkingUserCount(self) :
        count =len(self.main_userInfo)
        return count+1
    

if __name__=="__main__":
    miniBank : MiniBank =MiniBank()
    while True:
        miniBank.firstOption()