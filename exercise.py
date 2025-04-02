# # ##VARIABLES
# name = input("Enter your name: ")
# surname = "gwavava"
# age = int(input("Enter your age: "))
# height = float(input("Enter your height: "))
# ID_num = "63-313745 M 18"
# num_soldiers = 100
# soldiers_work_rate = [40, 78, 80, 6, 53, 49, 78, 35, 41]
# email = input("Enter your email: ")
# overal_password = 4546
# print(f"Your emails is {email} and your password is {overal_password}, height is {height},  age is {age}")

# ##LIST
# grades  = [73, 37, 73, 83, 94, 100, 63, 78]
# grades.append("67")
# # grades.clear()
# grades.insert(-1 ,10)
# print(grades.count(73))
# muclass = [1, 2, 3, 4, 5, 6, 7]
# best_students = ["decent", "kupakwahe", "gwavava", "recent", "innocent", "definate", "vincent", "leonard"]
# percentages = [78.5, 67.9, 45.3, 56.3, 59.9]
# presents = ["fruits", "text_books", "bicycles", "pens", "new uniforms"]
# grades[6] = 77
# print(len(grades))
# print(grades[2:])
# presents = [present.upper() for present in presents]
# print(presents)
# for x in grades:
#     print(grades)

##TUPLES
# #tuples can not be modified and thehy are immutable, Duplicates
# #you can not any elements in a tuple!!
# #to modify a list you  can firstly change it to an list then modify!!
# par_of_shoes = ("force", "jordan", "puma", "nike")
# jordans = (1, 2, 3, 4, 5, 6, 11)
# identity = ("63-313750 m 345", "Decent Gwavava")
# #Modifying a tuple
# my_list = list(par_of_shoes)
# my_list.append("shangu")
# my_list.insert(2 ,"bhustu")
# par_of_shoes = tuple(my_list)
# print(par_of_shoes)
# print(par_of_shoes.index("jordan"))

# # Set--> Sets doesnt an attribute of dublicates--> doesnot follow an senquence
# #What is diference between pop and delete
# kupakwashe = {"༼ つ ◕_◕ ༽つ", "Gwavava", "decent"}
# nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# char = {"decent", 12,  "gwavava"}
# print(char)
# kupakwashe.add("ndini")
# # kupakwashe.pop()
# kupakwashe.clear()
# print(kupakwashe)

# ##DICTONARY
# #dic consist of a key and a value---. can be seen through
# ID =  {"num_chitupa":"63-313750", "zita":"decent", "surname":"gwavava", "sabhuku":"ndini", "vhireji":"hameno"}
# students = {"Chimuti":"Tinotenda", "Garwe":"Geza", "Jongwe":"Gibson", "Totendarai":"Tonde"}
# pass_marks = {"Decent":"99", "Chimuti":"78", "Tonderai":"67", "Gwavava":"85", "Brian":"75"}
# pass_marks.update({"country" : "Zimbabwe", "city": "harare","cell": "0778262633",
#              "address": "35560 unit O"})
# for key in ID.keys():
#     print(key)
# for key,value in pass_marks.items():
#     print(f"{key}:{value}")
# # ID.clear()
# print(ID)

#WHILE LOOPS

# k = 0
# while k <22:
#     print(k)
#     k +=2
# correct_password = "kupakwashe"
# password = input("Enter yoour password: ")
# # while password != correct_password:
# #     print("Make sure the password you have entered is correct")
# #     print = input("Enter yoour password: ")
# # print("You are signed up")
# num = 3
# guess = int(input("Enter your guess: "))
# while guess != num:
#     print("You have guessed wrong")
#     guess = int(input("Guess any number: "))
# print("You have got it right")
# num = int(input("Enter your name which is from 1-10: "))

# while num<1 or num>10:
#     print(f"{num} is invalid")
#     num = int(input("Enter your name which is from 1-10: "))
# print(f"{num} is valid")
#WHILE LOOP WITH AN IF STTEMENT INSIDE
# while True:
#     option = input("Enter the stingness level motves you want: ")
#     if option == "extreme":
#         print("""
#         1) A girl should not be given even a cent
#         2) Buying gifts for a girl is not permissable by the association 
#         3) The only goal  to achieve with a girl is tlof tlof
#         """)
#         break
#     elif option == "medium":
#         print("""
#         1) A girl should be an amount of not more than 2.50$
#         2) Buying of gifts is prohibited
#         """).upper()
#         break
#     else:
#         print("I dont understand")
# print(input("YOOH Wassup: "))

# ##FOR LOOPS
# for x in range(10):
#     print(x)
# boys =  "kupa", "john", "matthew", "simon", "batitsa"
# for boy in boys:
#     print(boy)
# students = {"Kupa":"Gwavava", "Sober":"Decent", "Chitereki":"Anold", "Batista":"Bhobha"}
# # for keys in students:
#     print(keys)
# items = students.items()
# for keys,values in students.items():
#     print(f"{keys}:{values}")
# items = students.items()
# for keys, values in students.items():
#     print(f"{keys}:{values}")
# keys = students.keys()
# for keys in students.keys():
# #     print(keys)
# item = students.items()
# for keys,values in students.items():
#     print(f"{keys}:{values}")

##FUNCTONS---.Used to recall any code without rewritting it by just recalling a function
# def  sorry_costumers(name):
#     print(f"Hello, {name} e are sorry for donfall of the our network")
# sorry_costumers("Mr Gwavava")
# sorry_costumers("Mr Chitereki")
###Functions with multiple parameters
#To start with functioinss with 2 parameters or arguements
# def personal_details(name, age):
#     print(f"Hello, {name} you are {age} years old now")
# personal_details("Decent", 20)
# personal_details("John", 45)
# personal_details("Peter", 34)
##With 3 parameters or arguements
# def balance_amount(name, amount, due_date):
#     print(f"Hello, {name}")
#     print(f"Be reminded that you have an unpaid amount of ${amount:.2f}")
#     print(f"You are adviced to pay before {due_date}")
# balance_amount("Decent", 50.99, "01|02|25")
##Functions with a RETURN statement
# def add(x, y):
#     d = x + y
#     return d
# def multiply(x, y):
#     d = x * y
#     return d
# def sub(x, y):
#     d = x - y
#     return d
# def div(x, y):
#     d = x / y
#     return d
# print(add(5, 7))
# print(add(100, 359))
# print(sub(4, 6))
# print(sub(54, 1))
# print(multiply(4, 4))
# print(multiply(128, 4))
# print(div(6, 3))
# print(div(6, 6))
# #Making a function with a fullname
# def my_name(first, last):
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + last
# full_name = my_name("decent","gwavava")
# print(full_name)

# #CALLNG A FILE THROUGH A PATH 
# file = open('kupa.txt', 'w')
# file.write("pakaipa!")  
# file.close()
# with open("kupa.txt","a") as f: ##The a here simply means Append
#     f.write("\nMukuitasei boiz, Haaa nhasi pakaipa mafia "
#     "toiita sei neNyika yeZimbabwe")

# file = open("kupa.txt", "w")
# with open("kupa.txt","w") as file:
#     content = file.read()
#     print(content)

# # file = open("kupa.txt", "r")
# # content = file.read()
# # print(content)
# # # file.close()

# import os
# if os.path.exists("kupa.txt"):
#     print("It exists")
#     os.remove("kupa.txt")
# else:
#     print("Doesn't exists")

# # import os 
# # os.rmdir("newcharpter")

##CONDITIONAL STATEMENTS
name = input("Enter your name: ").capitalize()
surname = input("Enter your surname: ").capitalize()
age = int(input("Enter your age: "))

if age > 25:
    print("Sorry you are too O76trdssdr67`ld to join the Association")
    
elif age <=0:
    print("You are not born yet!!")
elif age >= 18:
    print(f"Hello, {name} {surname} Welcome to Sting Man Assocition😁")

else:
    print("You too young to be in the Association")
    








































































































































































































































































































































































































































































































































