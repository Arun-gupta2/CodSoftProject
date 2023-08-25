import random
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number_list=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol_list=['!', '#', '$', '%', '&', '*', '+', '(', ')']
print("welcome to password generator")
letter=int(input("enter how many letter you like into your passcode"))
symbol=int(input("enter how many symbol you like into your passcode"))
number=int(input("enter how many number you like into your passcode"))

password_list=[]
for x in range(1,letter+1):
    password_list.append(random.choice(alphabet))
for x in range(1,symbol+1):
    password_list+=random.choice(symbol_list)
for x in range(1,number+1):
    password_list+=random.choice(number_list)
random.shuffle(password_list)
password=""
for x in password_list:
    password+=x
print(password)