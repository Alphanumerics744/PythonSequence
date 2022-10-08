import itertools  
v = [1, 2, 3, 4]  
    
com_seq = itertools.combinations_with_replacement(v, 3)  
    
for i in com_seq:  
    print(i)  
