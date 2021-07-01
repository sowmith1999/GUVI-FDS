import sqlite3
import re
import string

conn = sqlite3.connect("user_details.db")

cur = conn.cursor()

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
punctuation=list(string.punctuation)
punctuation.remove(",")


def validate_email(user_email):
    if(re.search(regex, user_email)):
        return True
    else:
        return False

def validate_password(password):
    length,upper,lower,digit,spc_char=len(password),0,0,0,0
    if(length<5 or length>16):
        print("Password length is {}, expected length is {}-{}".format(length,5,15))
        return None
    else:
        for x in password:
            if(x.isupper):
                upper+=1
            elif(x.islower):
                lower+=1
            elif(x.isdigit):
                digit+=1
            elif(x in punctuation):
                spc_char+=1
    return (upper and lower and digit and spc_char and length>5)


def get_password_by_email(email):
    cur.execute("SELECT password FROM users WHERE email=:email",
                {"email": email})
    password=cur.fetchone()
    return password[0] if(password) else 0

def insert_user(email,password):
    with conn:
        cur.execute("INSERT INTO users VALUES (:email,:password)",
                  {"email": email, "password": password})
    return 0


main_menu = """Main menu:
            1)Login
            2)Register
            3)Forgot Password
            4)Exit
            choose an option: """
while(True):
    choice = int(input(main_menu))
    print(choice)
    if(choice == 1):
        user_email = input("please enter your email id: ")
        if(validate_email(user_email) and get_password_by_email(user_email)):
            password = get_password_by_email(user_email)
            user_password = input("please enter your password: ")
            if(user_password == password):
                print("Login Successful")
            else:
                print(
                    "you've entered a wrong password,\n please check your password and login again")
        elif not validate_email(user_email):
            print("the email id entered is invalid")
        elif not get_password_by_email(user_email):
            print("the mail-id entered is not registered")
    elif(choice==2):
        user_email=input("please enter a email id to register: ")
        if(validate_email(user_email) and not get_password_by_email(user_email)):
            user_password=input("please enter a password of length 5 to 15 with at least \n\t1)Upper_case_Letter \n\t2)Lower_Case_Letter\n\t3)digit\n\t4)special character: \n")
            if(validate_password(user_password)):
                insert_user(user_email,user_password)
                print("user created successfully")
            else:
                print("password is not of expected format")
        elif not validate_email(user_email):
            print("the email id entered is invalid")
        elif get_password_by_email(user_email):
            print("mail already exists, please login")
    elif(choice==3):
        user_email=input("please enter your email-id: ")
        if(validate_email(user_email) and get_password_by_email(user_email)):
            password=get_password_by_email(user_email)
            print("your password: ",password)
        elif not validate_email(user_email):
            print("the email id entered is invalid")
        elif not get_password_by_email(user_email):
            print("The email id entered doesn't exist")
    elif(choice==4):
        break

        
