list1 = [10, 20, 30, 40, 50]  
  
print('Current Numbers List: ', list1)  
  
el = list1.insert(3, 77)  
print("The new list is: ",list1)  
  
n = int(input("enter a number to add to list:\n"))  
  
index = int(input('enter the index to add the number:\n'))  
  
list1.insert(index, n)  
  
print('Updated Numbers List:', list1)  
