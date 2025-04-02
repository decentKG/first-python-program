# # #conditional statement
# # #formated strings
# # register = "present"
# # name = "Decent"
# # if register == "present":
# #     print(f"You are {register}")
# #     print(f"{name} is {register}")
# # # else: 
      

# # username = "decent"
# # password = 1234

# # if password == 1234:
# #     print(f"welcome {username}")
# # else:
# #     print("wrong password")

# #inputs which returns a value

# name = input("Enter your name and intials: ")
# surname = input("Enter your surname: ")
# age = int(input("Enter your age:"))

# if age >= 18:
#     print("You are signed up!")
#     print("Welcome", name, surname,"!")
# elif age >= 23:
#     print("sorry")
    
# else:
#     print("You are not eligable")

#LIST COMPREHENSION in Traditional way
# tripples = []
# for x in range(1, 31):
#  tripples.append(x * 3)
# print(tripples)

#LIST COMPREHENSION in the easiest way to read and concise
# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# fruits = ["BANANA", "APPLE", "MANGO","TSUBVU"]
# fruits = [fruit.lower() for fruit in fruits]
# print(fruits)

# fruits = ["BANANA", "APPLE", "MANGO","TSUBVU"]
# fruits_chars = [fruit[0] for fruit in fruits]
# print(fruits_chars)

# numbers = [1, -2, 3, -4, -5, 6, -7, 8, -9]
# positive_nums = [num for num in numbers if num >=0]
# negative_nums = [num for num in numbers if num <0]
# even_nums = [num for num in numbers if num %2 ==0]
# print(even_nums)

# grades = [76, 87, 45, 34, 90, 34, 26, 100]
# fails = [grade for grade in grades if grade < 45]
# print(fails)



# # Tuples (is immutable)
# nums = (1, 2, 3, 4, 5, 6, 7)
# print(nums)

# # new_element = (6,)
# # print(nums + new_element)
# # print(nums[1:-1:2])

# print(nums[::2])#Stepper

#DICTIONARYs 
# dic = {
#     "student": "kupakwashe",
#     "age": 20
# }
# print(dic)

# dic["student"] = "kupakwashe gwavava"
# print(dic)
#


# surname ={"Kupa": "Gwavava",
#             "Vincent" : "Chitereki",
#             "Innocent": "Chivhu",
#             }

# print(surname.get("Vincent"))
# surname.update({"Chimuti": "Mutoti"}) ## adding
# surname.pop("Kupa")##removing a key
#surname.clear()

# surname = surname.keys()
# surname = surname.values()

# printing ascending order##
# for key in surname.keys():
#     print(key)

# ##Items
# items = surname.items()
# for key, value in surname.items():
#     print(f"{key} : {value}")

##WHILE LOOPING

# name = input("Enter your name: ")

# while name == "":
#     print("You didn't enter your name")
#     name = input("Enter your name: ")
# print(f"Hello {name}")



# nums = int(input("Enter your number: "))

# while nums < 1 or nums >10:
#     print(f"Your {nums} is invalid")
#     nums = int(input("Enter your number: "))
# print(f"Your number is {nums}")

##Tuplee

# tup1 = (1, 3, 2, 4, 5, 7, 6, 8, 9,)
# print(len(tup1))
# my_list = list(tup1)
# # print(my_list)

# # list2 = [5, 6, 7, 8, 9]

# # my_list.exten(list2)
# # print(my_list)

# ##Sorting  
# my_list.sort()
# my_list.sort(reverse = "True")
# print(my_list)

#Sets
# nums = {1, 2, 3, 4, 5, 5, 4}
# nums2 = {5, 6, 7, 8, 9,}
# print(nums)

#Set Operations
# union = nums | nums2
# print(union)

# union = nums.union(nums2)
# print(union)
# numbers.remove(4)

# numbers.add(12)
# print(f"My set is" numbers)

##INTERSECTION
# int_sec = nums.intersection(nums2)
# int_sec = nums & nums2
# print(int_sec)

##DIFFERENCE

# diff_set = nums.difference(nums2)
# diff_set = nums - nums2
# print(diff_set)

# ##Symmetric differece
# sym_diff = nums.symmetric_difference(nums2)
# sym_diff = nums ^ nums2
# print(sym_diff)

##LOOPS##


   
# command =input("Enter a command: ")
# list = ["start", "stop", "quit"]
# while True:
#     command =input("Enter a command: ").lower()

#     if command == "help":
#         print("start - to start the car🛴")
#         print("stop - to stop the car")
#         print("quit - to exit")
#         command =input("Enter a command: ")
        
#     elif command == "start":
#         print("the car started🚖")
#         command = input("Enter a command: ")
#         while command=="start":
#             print("The car has already started stupid")
#             command = input("Enter a command: ")

#     elif command == "stop":
#         print("the car stoped🚩")
#         print(input("Enter a command: "))
#         while command == "stop":
#             print("Wangu mota yakamira kare iyi🙄")
#             command = input("Enter a command: ")

#     elif command == "quit":
#         print("Exiting the game😥")
#         break
#     else:
#         print("I dont understand this command")
#         command =input("Enter a command: ")


# while True:
#     command =  input("enter command ").lower()
#     if command == 'start':
#         print("Car started...🚗")
#     elif command == 'stop':
#         print("Car stopped...🚩")
#     elif command == 'help':
#         print("""
#         start - to start the car
#         stop - to stop the car
#         quit - to quit
#         """)
#     elif command == 'quit':
#         print("You are now exiting the ga")
#         break
#     else:
#         print("I don't understand that...")

# i = 10 

# while i >=0:
#     print(i)
#     i -=1
    

##FOR LOOPS


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


    
    
    











        