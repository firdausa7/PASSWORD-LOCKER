from user import User
from user_credentials import Info


def create_account(first_name, last_name, e_mail):
    new_user = User(first_name, last_name, e_mail)
    return new_user


def create_credentials(twitter_t, email_e):
    new_cred = Info(twitter_t, email_e)
    return new_cred


def save_account(user):
    user.save_user()


def save_credentials(user_credentials):
    user_credentials.save_info()


def display_users():
    return User.display_users()


def display_creds():
    return Info.display_info()


def main():
    # global first_name
    print("HELLO THERE  WELCOME!!")
    print(" ")
    print(" ")
    while True:
        print("-" * 156)
        print("""USE THE FOLLOWING SHORT CODES!!
1. cr - CREATE NEW ACCOUNT
2. ex - EXIT PASSWORD LOCKER
3. dc - DISPLAY ACCOUNTS
4. gp - GENERATE PASSWORDS""")


        print(" ")
        print("      TYPE IN A SHORT CODE!")
        print(" ")
        short_code = input() .lower()
        if short_code =='cr':
            print(" ")
            print("-" * 30)
            print("      CREATE A NEW ACCOUNT!")
            print(" ")
            print(" ")
            print("what is your first name?..")
            print(" ")
            first_name =input()
            print("What is your middle name?..")
            print(" ")
            last_name= input()
            print("what is your email address?..")
            print(" ")
            e_mail= input()
            print ("what is your facebook password?..")
            print(" ")
            twitter_t =input()
            print("what is your email password?..")
            print(" ")
            email_e= input()
            save_account(create_account(first_name,last_name,e_mail))
            print('\n')
            save_credentials(create_credentials (twitter_t,email_e))
            print('\n')
            print("-" * 156)
            print(f"New Account  { first_name } { last_name } { twitter_t } has been created")
            print('\n')
        elif short_code =='dc':
            if display_users():
                print(" ")
                print("The user name")
                print(" ")
                print('\n')
                for user in display_users():
                    print(f"{user.first_name}{user.last_name}")
                for credential in display_creds():
                    print (f"{twitter_t}")
                    print(" ")

            else:
                    print('\n')
                    print("-" * 30)
                    print(" ")
                    print("                         PLEASE CREATE AN ACCOUNT ")
                    print(" ")
        elif  short_code == 'gp':
            print(" ")
            print(" ")
            print("TO GENERATE A PASSWORD ADD IN YOUR FIRST NAME AND FACEBOOK BELOW!!")
            print(" ")
            list_of_inputs = [c for c in input()]

            # list_of_inputs= list(list_of_inputs)
            list_of_inputs.reverse()



            print (list_of_inputs)






        elif short_code == "ex":
            print("-" * 156)
            print(" ")
            print("                        THANK YOU!")
            print(" ")
            print("-" * 156)
            break
        else:
            print("-" * 156)
            print(" ")
            print("                              RETRY!!")
            print(" ")
            print("                Please Select One Of The Options Provided")
            print(" ")

if __name__ == '__main__':
    main()
