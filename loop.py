# num = 7
# guess = int(input("Guess any number: "))




# if my number is less than the correct number 
# print your number is less than the expected
#  number and if the number is greater than the
#  expected number print your number is greater than the expected number
# guess_num = int(input("Enter your guessing: "))

# while guess_num != 7:
#     if guess_num >7:
#        print("Your number is greater than the expected😪")
#        print = int(input(f"Your guess should be less than {guess_num}: "))
#     else:
#        print("Your number is lower than the expected😪")
#        print = int(input(f"Your guess should be higher than {guess_num}: "))
# print("Correct!!!👍😁")
    


##INFINITY LOOP
# guess = int(input("Enter you guess: "))

# while True:
#     if guess >7:
#         print("Your number is greater than the expected😪")
#         print = int(input(f"Your guess should be less than {guess}: "))
#     elif guess <7:
#         print("Your number is lesser than the expected😪")
#         print = int(input(f"Your guess should be less than {guess}: "))

#     else:
#         print("You got this")
#         print = int(input("Enter you guess: "))

##FOR LOOPS--->They are used to repeat a block of code for multiple times
             #There are 2 primary types of loops i.e While & For loops
             #And a nested loops
             #All sequence inluding(Sets, Lst, Dic,Tuple, Strings)
  
#  Syntax:
#for variable in senquence:
#statement

# friuts = ["a", "b", "c"]
# for fruit in friuts:
#     print(fruit)



# #Looping through a string

# num = "one"
# for letter in num:
#     print(letter)


# for  in range(start, stop, step):
#     print(even)

# for even in range(1,51):
#     if even % 5 == 0:
#         continue
#     print(even)

# def greet (name):
#     print(f"Hello, {name}")
# greet("Apo")

# POSITIONAL ARGUEMENTS 
#Exponent simply means the Power of
# def power(base,exponent):
#     return base ** exponent
# print(power(2, 3))

#KEY WORD ARGUEMENT
# {"key","word"}

#DEFAULTS ARGUMENTS
#If an arguemnt is not passed a default can be used
# def greet (name="Guest"):
#     print(F"Hello, {name} What can we help you with")
# greet()


# def multiply(a, b):
#     return a * b
# results = multiply(5, 7)
# print(results)

# def multiply(a, b):
#     return a * b
# print(multiply(2, 5))

##NESTED FUNCTION
# Creating a fuction nside a function
# def outer():
#     print("This is the outer function")
#     def inner():    
#         print("This is the inner function")
#     outer()
#     inner()
# outer()


# def global_functions():
#     print("This is a global function")
# global_functions()

# def another_functon():
#     global_functions()
# another_functon()