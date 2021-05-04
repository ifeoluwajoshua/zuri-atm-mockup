import random


database = {4035600045 : ['Ifeoluwa' , 'Ayomide' , 'oluwadahunsiayomide02@gmail.com' , 'Ayomide234@' , 100000] }


def init():

    is_valid_option_selected = False
    print("WELCOME TO BANK PYTHON")

    while is_valid_option_selected == False:
        have_account= int(input("DO YOU HAVE AN ACCOUNT WITH US?: 1 = yes 2 = no \n"))
        if (have_account ==1):
            is_valid_option_selected = True
            login()
        elif (have_account == 2):
            is_valid_option_selected = True
            register()
        else:
            print("You have selected an invalid option")


def login():
    print("***************LOGIN******************")

   
    print("WELCOME TO BANK PYTHON")


    account_number_from_user = input("WHAT IS YOUR ACCOUNT NUMBER? \n")
    is_account_number_valid = account_number_validation(account_number_from_user)
    
    if is_account_number_valid:

        
        password_from_user = input("WHAT IS YOUR PASSWORD? \n")

        
        for account_number,user_details in database.items():
            if account_number == int(account_number_from_user):
                if user_details[3] == password_from_user:
                    bank_operations(user_details)
        

        else :
            print("WRONG ACCOUNT NUMBER OR PASSWORD")
    init()
                    
            
def account_number_validation(account_number):
    if account_number :


        if len(str(account_number)) == 10:

            try:
                int(account_number)
                return True
            except ValueError:
                print("INVALID ACCOUNT NUMBER")

        else:
            print("ACCOUNT NUMBER CANNOT BE MORE OR LESS THAN 10")
            return False

    else:
        print("ACCOUNT NUMBER IS REQUIRED")
        return False


def register():
    
    print("***********REGISTER*************")
    email = input("WHAT IS YOUR EMAIL ADDRESS? \n")
    first_name = input("WHAT IS YOUR FIRSTNAME? \n")
    last_name = input("WHAT IS YOUR LASTNAME? \n")
    password = input("CREATE A NEW PASSWORD: \n")
    try:
        bonus = int(input("WHERE DID YOU HEAR ABOUT BANK PYTHON? \n1) TWITTER \n2) FACEBOOK \n3) ON TELEVISION \n4) NO WHERE \n"))
    except:
        print("invalid input")
    if bonus == 1 :
        balance = 2000
    elif bonus == 2:
        balance = 2000
    elif bonus == 3:
        balance = 2000
    elif bonus == 4:
        balance = 1000

    else :
        print("SORRY , INVALID OPTION")
        balance = 0
    
    account_number = generate_account_number()
    database[account_number] = [first_name , last_name , email , password , balance]
    
    print("Your ACCOUNT has been created")
    print("== ===== =============== ======")
    print("Your account number is %d " % account_number)
    print('PLEASE KEEP IT SAFE')
    print('== ===== ======= ======== ========')

    
    login()


def bank_operations(user_details):
    print("WELCOME %s %s " % (user_details[0] , user_details[1]))
    option = int(input("WHAT WOULD LIKE TO DO? \n1 - DEPOSIT \n2 - WITHDRWAL \n3 - CHECK BALANCE \n4 - LOGOUT \n"))

    if option == 1:
        deposit_operation(user_details)
        
    elif option == 2:
        withdrawal_option(user_details)

    elif option == 3:
        get_current_balance(user_details)
        
    elif option == 4:
         logout(user_details)
    else:
        print("Invalid Option selected")
        bank_operations(user_details)
         

def withdrawal_option(user_details):
    print("*****************WELCOME TO THE WITHDRAWAL SECTION**************")
    print(f"YOUR CURRENT BALANCE IS #{user_details[4]}")
    try:
        x = int(input("HOW MUCH WOULD YOU LIKE TO WITHDRAW: \n#"))
    except:
        print("INVALID INPUT")

    if x > int(user_details[4]):
        print("INSUFFICIENT FUNDS")
        bank_operations(user_details)

    else:
        after_withdraw = x - int(user_details[4])
        user_details[4] = after_withdraw
        print(f"YOUR ACOOUNT BALANCE IS #{user_details[4]}")
        bank_operations(user_details)


def deposit_operation(user_details):
    print("*****************WELCOME TO THE DEPOSIT SECTION**************")
    print(f"YOUR CURRENT BALANCE IS #{user_details[4]}")
    try:
        x = int(input("HOW MUCH WOULD YOU LIKE TO DEPOSIT INTO YOUR ACCOUNT: \n#"))

    except:
        print("INVALID INPUT")
        deposit_operation(user_details)

    new_balance = x + int(user_details[4])
    user_details[4] = new_balance
    print(f"YOUR NEW BALANCE IS #{user_details[4]}")

    bank_operations(user_details)


def generate_account_number():
    
    return random.randrange(1111111111,9999999999)


def get_current_balance(user_details):
    print(f"YOUR ACCOUNT BALANCE IS #{user_details[4]}")
    bank_operations(user_details)
    


def logout(user_details):
    login()


init()