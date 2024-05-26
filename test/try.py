#guest_name=['sabira', 'anu']

#li=input(" give your name: ")

#if li in guest_name:
    #print("welcome")
#else:
   # print("Not allowed")



'''
Grades= int(input("give your grade: "))

if Grades<40:

    print("Fail")

elif Grades<=50:
    print(" Grade D")

elif Grades<=60  :
    print("Grade C")

elif Grades<=70  :
    print("Grade B")

elif Grades<80 :
    print("Grade A")

elif Grades>=80 and Grades<=100 :
    print("Grade A+")

else:
    ("take rest")

'''
'''
username=input("user name ")
password=input(" password ")

user_list=[]
user_list.append(username)
user_list.append(password)

print(user_list)
'''


''''
value=input(" Give your value ")
even_list = []
odd_list = []
for val in range(10):

 if val % 2 == 0:
    even_list.append(val)
else:
    odd_list.append(val)

print(even_list)
print(odd_list)
'''
''''
username_list=['admin','user']
password_list=['123456','1234']

username=input("Give your name")

if username in username_list:
    password = input("Give your password")
    if password in password_list:
      print("welcome")

else:
    print("Not allowed")
'''



amount=int(input("print your amount "))
if  amount>1000:
    age =int(input("give your age "))

    if age<50:
        gender = input("male or female? ")
        if gender == "male":
            print(" cake free")
        else:
            print(" chocolate")

        payment = input(" cash or card? ")
        if payment=="cash":
            print("20% disc")
        else:
            print("10% disc")

