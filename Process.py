# Python multiprocessing example  
# importing the multiprocessing module  
  
import multiprocessing  
def cube(n):  
   # This function will print the cube of the given number  
   print("The Cube is: {}".format(n * n * n))  
  
def square(n):  
    # This function will print the square of the given number  
   print("The Square is: {}".format(n * n))  
  
if __name__ == "__main__":  
   # creating two processes  
   process1 = multiprocessing.Process(target= square, args=(5, ))  
   process2 = multiprocessing.Process(target= cube, args=(5, ))  
  
   # Here we start the process 1  
   process1.start()  
   # Here we start process 2  
   process2.start()  
  
   # The join() method is used to wait for process 1 to complete  
   process1.join()  
   # It is used to wait for process 1 to complete  
   process2.join()  
  
   # Print if both processes are completed  
   print("Both processes are finished")  
