#Generates a list of 100 random mail id's and passwords

import random
import string
lower_case_letters = list(string.ascii_lowercase)
upper_case_letters=list(string.ascii_uppercase)
digits=list(string.digits)
punctuation=list(string.punctuation)
punctuation.remove(",")
combined_list=list(string.ascii_lowercase+string.ascii_uppercase+string.punctuation+string.digits)
combined_list.remove(",")

def email_gen(mail_length, domain_length):
    mail_name = ""
    domain_name = ""
    com_name = ""
    for _ in range(mail_length):
        mail_name = mail_name+random.choice(lower_case_letters)
    for _ in range(domain_length):
        domain_name = domain_name+random.choice(lower_case_letters)
    for _ in range(3):
        com_name += random.choice(lower_case_letters)
    return mail_name+"@"+domain_name+"."+com_name

def password_gen(length):
    password="".join(map(random.choice,(digits,upper_case_letters,lower_case_letters,punctuation,combined_list)))
    for _ in range(length-5):
        password+=random.choice(combined_list)
    return password
    
password_gen(12)
print("email,password")
for _ in range(100):
    print(email_gen(random.randint(5,15), random.randint(3,7))+","+password_gen(random.randint(5,15)))
