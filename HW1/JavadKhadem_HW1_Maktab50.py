"""
ebteda jomalat makhraj ra hesab karde va dar 'terms' zakhire mikonam.
sepas ba eijad har jomle, hamzaman majmoe seri dar 'SumOfSeries' hesab mishavad.
SumOfSeries(x) = 1/x - 1/( x+ 2x^2 ) + 1/( x+ 2x^2 + 3x^3 ) - 1/( x+ 2x^2 + 3x^3 + 4x^4 ) + ...

n : number of terms
"""

def maktab_series(x, n=10):
    try :
        terms = []
        SumOfSeries = 0.0
        for i in range(1, n+1):
            terms.append( i * x  i )
            SumOfSeries += ( (-1)(i-1)  ) * ( 1 / sum( terms ) )
        return SumOfSeries
    
    except ZeroDivisionError:
        return  "inpit should not be zero"
        




x = -5.7

print("---------------------")
print("sum of maktab series is : {} ".format( maktab_series(x) ) )