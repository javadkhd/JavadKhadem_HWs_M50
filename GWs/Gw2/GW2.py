################################## 1

# for i in range(2000,3200+1):
#     if (i % 7 == 0) and (i % 5 != 0):
#         print(i, end=", ")



################################## 2

# a = input("enter your numbers:\n").split(',')

# l_a = list(map(int,a))
# t_a = tuple(l_a)


################################## 3

# def fact(n):
#     return 1 if n <=1 else n * fact(n-1)

# print(fact(5))

################################## 4

# def score (a, b):
#     if    a == b:
#         return [0, 0]
#     elif (a == 'rock' and b == 'scissor') or (a == 'paper' and b == 'rock') or (a == 'scissor' and b == 'paper'):
#         return [1, 0]
#     else:
#         return [0, 1]

# # print([0,0]+[1,0])

# max_of_iter = int(input("max of iter :\n"))
# ss = [0, 0]
# while max(ss) < max_of_iter:

#     while True:
#         a = input("first player action:\n")
#         b = input("secend player action:\n")

#         if (a in ['scissor', 'paper', 'rock']) and (b in ['scissor', 'paper', 'rock']):
#             break
#         else:
#             print("choose from : 'scissor', 'paper' and 'rock'")
        
#     ss[0] += score(a, b)[0]
#     ss[1] += score(a, b)[1]




########################### 5
# from numpy import sqrt
# def isprime(n):
#     asghar = set(  2 , *range(1, 1+int(sqrt(n) ) , 2 )  )
#     return n if all(n % i for i in asghar ) else None

# # a = int(input("enter your number:\n"))
# a=55
# for i in range(2,a):
#     if isprime(i):
#         print(isprime(i))


######################## 6

tmp = [ 0, '', '3.4558', [], [1, 2], [(8,{'[(8,)]':'444'})], [(8,)], (3, [4, 5]), {}, {3}, {'':''}, {'346.5466':'444'} ]


out = list()
while True:

    for i in tmp:

        if type(i) in [list, tuple, dict, set, str]:
            
            if type(i) == str and i:
                out.append(eval(i))
            else:
                out.extend(i)
            
        else:
            out.append(i)
            

    if all( [ False for i in out if type(i) in [list, tuple, dict, set, str] ] ):
        break
        
    else:
        tmp, out = out, list()


print(out)


