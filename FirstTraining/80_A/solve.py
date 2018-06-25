from math import sqrt

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

n,m = map(int,input().split())
boleans= []

for i in range(n,m+1):
    boleans.append(isPrime(i))

if not any(boleans[1:-1]) and boleans[-1]:
    print ('YES')
else:
    print ('NO')



        
