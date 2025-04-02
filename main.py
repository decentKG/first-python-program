# print("Welcome to Mufakose")
# score = 0
# full_name = "decent gwavava"
# print(score)
# print(full_name)

# live = "5"
# time = "30" 
# counter = "5"

# print(live)
# print(time)
# print(counter)
  
# name_of_organizatioon = "uncommon"
# print (type(live)) # his  expression is printing thhe data type of the variable live

# # integer data type

# number_of_pupils = "40"
# print(type(number_of_pupils))

# #floot type or decemals 
# number_of_pupils = "40.567"
# print(type(number_of_pupils))

# x = 15
# y = 5
# print(f"addition{x+y}")
# print(f"subtraction{x-y}")
# print(f"division{x/y}") # float division
# print(f"multiplication{x*y}")
# print(f"integer division{x//y}")
# print(f"modulus{x%y}")
# print(f"expo or poer of{x**y}")



#adding items
#append
#insert 

# # make a list #modifying the list
# names =  ["kupa", "john", "matthew", "decent"]
# names[1] = "john gwavava"
# names[3] = "sober"
# print(names[-1])


weight = int(input("Weight: "))
unit = input( "(K)g or (L)bs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in (L)bs: " + str(round (converted), 2))
else:
    converted = weight * 0.45
    print("Weight in (K)g: " + str(converted))








