
from operator import mod
import random

def compuesto(a,n,t,u):
    x0 = (a**u) % n
    if (x0==1 or x0==n-1):
        return False
    for i in range (1,t):
        i=((i-1)**2)%n
        if i == n-1:
            return False
    return True

def millerRabin(n,s):
    t=0
    u=n-1
    while (u % 2 == 0):
        u = u/2
        t = t+1
    for j in range(1,s):
        a=random.randint(2,n-1)
        if compuesto(a,n,t,u):
            return False
    return True

def randomBits(b):
    n=random.randint(0,(2**b)-1)
    m=(2**b-1)+1
    n=n|m
    return n

def randomPrimos(b):
    x0 = 1
    n = randomBits(b)
    while millerRabin(n,x0)==False:
        n = n+2
    return n

def genPrimos(n):
    s = 1
    n = n+1-(n % 2)
    while millerRabin(n,s) == False:
        n = n+2
    return n


print("Hola Mundo")

print(f"El modulo es esta cosa es : {17%5}")

for i in range(0,10,2):
    print(f"El valor de i es : {i}")

print(f"numeros random {random.randint(1,10)}")