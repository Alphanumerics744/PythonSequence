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

num = 5
a = (2 * num) - 2
for i in range(0, num):
     for j in range(0, a ):
         print(end=" ")
     for j in range(0, i+1)
     print('*' , end=" ")
print(" ")
