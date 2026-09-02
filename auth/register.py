from account.save_account import save_accounts
from settings.pyconfig import Configuration

save = save_accounts()
config_pack = Configuration()

def register_account():
    first_name_input = input("Enter First name: ")
    last_name_input = input("Enter Last name: ")
    username_input = input("Enter username: ")
    password_input = input ("Enter Password: ")

    return{"first_name":first_name_input, "last_name":last_name_input, "username":username_input, "password":password_input}



register = register_account()
save.saved_accounts(register)















