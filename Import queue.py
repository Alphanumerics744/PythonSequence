import queue   
# Queue is created as an object 'L'  
L = queue.Queue(maxsize=10)   
  
# Data is inserted in 'L' at the end using put()   
L.put(9)   
L.put(6)   
L.put(7)   
L.put(4)   
# get() takes data from   
# from the head    
# of the Queue   
print(L.get())   
print(L.get())   
print(L.get())   
print(L.get())   
