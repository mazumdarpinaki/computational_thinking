import sys
sys.getrecursionlimit()

def Fib(n):
    if n==0 or n==1:
        return 1
    else:
        return Fib(n-1)+Fib(n-2)
for i in range(12):
    print('Fib('+str(i)+')=',Fib(i))

def fastFib(n,memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result= fastFib(n-1,memo)+fastFib(n-2,memo)
        memo[n]=result
        return result

#for i in range(120):
    #print('Fib('+str(i)+')=',Fib(i))
    

        
