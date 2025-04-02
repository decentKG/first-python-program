# num = int(input("Enter: "))
# num2 = int(input("Enter: "))

# results = num + num2

# print(results)

#GETS
#And
#Or
#Not

# a = 13
# b = 16
# c = 24

# print(b < a or c>b)
# username = "admin"
# password = 1234
# useraname = input("Enter your userame: ")
# password = int(input("Enter your password: "))

# if username == "admin" and password == 1234:
#     print(f"Hey {useraname} Welcome")
# else:
#     print("Invalid credentials")

# temp = ""
# day = "sunny"

# temp = int(input("Enter the temp: "))
# day = input("Enter the condition: ")


# if temp >=30 and condition == day:
#     print(f"The weather is {day}")
# else:
#     print("it is cold")
    
students_score = int(input("Enter your score in Maths: "))

if students_score >= 90 and students_score <= 100:
    print("You scored a grade A")
elif students_score >= 80 and students_score <= 89:
    print("You scored a grade B")
elif students_score >= 70 and students_score <= 79:
    print("You scored a grade C")
elif students_score >= 60 and students_score <= 69:
    print("You scored a grade D")
elif students_score >= 100:
    print("Invalid")

else:
    print("F")





