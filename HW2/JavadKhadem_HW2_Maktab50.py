############## ex1

#### method 2:
    

#for i in range(4):
#    for j in range(2):
#        print( "bla" , end = " " )
#    print("bla")
#    if i == 1:
#        print('\"\\\"\"' , end = "" )

        
#### method 1:
    
#bla2 = """bla bla bla
#bla bla bla
#"\\""bla bla bla
#bla bla bla
#"""
#print(bla2)


############## ex2

#a  = list( input("enter your inpu:\n").split() )
#b = tuple(a)
#print(a)
#print(b)

############## ex3



##arr = list( input("enter your list:\n").split() )
##arr = [int(i) for i in arr]

import numpy as np
arr = np.random.randint(low = -100, high=101, size=20)
print(arr)
#print(f"{min(arr) = } & {max(arr) = } & {sum(arr) = }")