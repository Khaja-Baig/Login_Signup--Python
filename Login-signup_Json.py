
# # ## Login - SignUp //

# import json

# def intro():
#     print("Welcome to Accounts:: \n1.Sign up\n2.Log in\n3.Exit\n")
#     opt = int(input('enter your option number: '))
#     if opt == 1:
#         sign_me()
#     elif opt == 2:
#         log_me()
#     elif opt == 3:
#         exit()
#     else:
#         print("Invalid option: ")
#         intro()

# def sign_me():
#     def strong_pwrd(pwrd):
#         special_chr = '@^&*()#%$!+-'
#         d,l,u,sp, = 0,0,0,0
#         if len(pwrd)<8 or len(pwrd)>16:
#             print('invalid password:\nlength of your password must be greater than 7 and less than 16: ')
#             pwrd = input('create password: ')
#             strong_pwrd(pwrd)
#         for i in pwrd:
#             if i.isdigit():
#                 d+=1
#             if i.islower():
#                 l+=1
#             if i.isupper():
#                 u+=1
#             if i in special_chr:
#                 sp+=1
#         if d>=1 and l>=1 and u>=1 and sp>=1:
#             print('Password Created: ')
#         else:
#             print("invalid password:\npassword must contain a capital letter-small letter_digit_special characters(@^&*()#%$!+-)")
#             pwrd = input('create password: ')
#             strong_pwrd(pwrd)

#     def valid_mail(email):
#         if type(str(email[1:4])) != int:
#             if email.count('@') == 1:
#                 if email[-4:] in ('.org','.com','.net','.edu','.gov'):
#                     pass
#         else:
#             print('invalid email.')
#             email = input('enter your email address: ')
#             valid_mail(email)
#     def mobile_num(num,code):
#         if len(num) == 10:
#             num+=code
#         else:
#             print("invalid phone number: ")
#             code = input("enter your phone number code: ")
#             mob_no = input('enter phone number: ')
#             mobile_num(mob_no,code)

#     name = input('enter your full name: ')
#     age = int(input('enter your age: '))
#     code = input("enter your phone number code: ")
#     mob_no = input('enter phone number: ')
#     mobile_num(mob_no,code)
#     email = input('enter your email address: ')
#     valid_mail(email)
#     password = input('enter your password: ')
#     strong_pwrd(password)

#     with open('login-signup_data.json','r') as data:
#         accounts_data = json.load(data)
#         accounts_data.append({"name":name,"age":age,"mobile.no":mob_no,"email":email,"password":password})
#         print("your account is successfully created:: ")

#     with open('login-signup_data.json','w') as data:
#         json.dump(accounts_data,data,indent=4)
#         print("your data is saved:: ")
#     intro()

# def log_me():
#     unid = input("enter user name: ")
#     pss = input("enter your password: ")

#     with open('login-signup_data.json','r') as data:
#         account_data = json.load(data)

#         for dict in account_data:     
#             if unid in dict.values() and pss in dict.values():
#                 print('Login successfully: ')
#                 intro()
#             elif unid in dict.values() and pss not in dict.values():
#                     print('invalid password; ')
#                     break
#             elif unid  not in dict.values() and pss in dict.values():
#                 print('invalid name: ')
#                 break
#         print('account not found: ')
#         intro()

# intro()


