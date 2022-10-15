# importing the library  
import tabula  
# address of the file  
myfile = 'marksheet_table.pdf'  
# using the read_pdf() function  
mytable = tabula.read_pdf(myfile, pages = 1)  
# printing the table  
print(mytable[0])  
