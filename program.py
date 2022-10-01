# Take the input from the user in this code. 
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num)  
          
          
def add(a,b):
     return a+b
 
def sub(a,b):
     return a-b
 
def prod(a,b):
     return a * b
 
def div(a,b):
     return a / b
 
def si(p, r, t):
    return (p*r*t) / 100
 
def ci(p, r ,t):
    return p * pow((1 + r/100), t)
 
def sqr(num):
    return num**2
 
def sqrt(num)
    return num**0.5
 
print(add(10,15))
