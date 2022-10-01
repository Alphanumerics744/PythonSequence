# Python 3 code to find sum of elements in given array 
def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
          
    return(sum) 
  
# driver function 
arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 
  
# calculating length of array 
n = len(arr) 
  
ans = _sum(arr) 
  
# display sum 
print ('Sum of the array is ', ans) 
  
# This code is contributed
Output:
Sum of the array is  34
Method 2:
      
year = int(input('enter year'))
if year % 400 == 0:
  print('it is a leap year')
elif year % 4 == 0:
  print('it is a leap year')
elif year % 100 == 0:
  print('not a leap year')
else:
  print('not a leap year')


# Python 3 code to find sum 
# of elements in given array
# driver function
arr = []
  
# input values to list
arr = [12, 3, 4, 15]
  
# sum() is an inbuilt function in python that adds 
# all the elements in list,set and tuples and returns
# the value 
ans = sum(arr)
  
# display sum
print ('Sum of the array is ',ans)
