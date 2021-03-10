##################  1

# def asghar(a):
#     return {x : x**2 for x in range(1, a+1)}

# print(asghar(10))

##################  2

# a = 18
# b = 48

# def gcd(a, b):

#     if b > a:
#         a, b = b, a

#     while b:
#         a, b = b, a%b
#     return a
# print(f"gcd = {gcd(a, b)},lcm = {int((a*b)/gcd(a, b))}")

##################  3
###### method 1
# perfects = list()
# for i in range(1,10001):
#     asghar = list()
#     for j in range(1,i):
#         if i % j == 0:
#             asghar.append(j)
#     if sum(asghar) == i:
#         perfects.append(i)
# print(perfects)

###### method 2
# def perfect(x):
#     asghar = list()
#     for i in range(1,x):
#         if x % i == 0:
#             asghar.append(i)
#     if sum(asghar) == x:
#         return x


# perfects = filter(perfect, range(1,10001))
# for i in perfects:
#     print(i)
# print(perfect)

################# 4
# import os
# from random import randint
# secret_number = randint(1, 100)

# os.system('clear')

# def akbar(secret_number):
#     for i in range(10):
        
#         print(f"Number of chances left: {10-i}")

#         while True:

#             asghar = input("enter your guess:\n")

#             if asghar.isdigit() and int(asghar) in range(101) and int(asghar) == float(asghar):
#                 asghar = int(asghar)
#                 break
#             else:
#                 print("enter integer number between 1-100")

#         os.system('clear')

#         if secret_number > asghar:
#             print("Enter Higher Number")

#         elif secret_number < asghar:
#             print("Enter Lower Number")

#         else:
#             print(f"hooooraaaaa, secret number is {secret_number}")
#             print(f"You succeeded {i+1} times")
#             break

#     else:
#         print("you lose")



# akbar(secret_number)




