file  = open("Data.txt", "w")
file.write("Hello World")               
file.close()        

print("Data.txt file created and data written successfully.")

file = open("Data.txt", "r")
content = file.read()       
print("Content of Data.txt:", content)
file.close()        

file = open("Data.txt", "a")
file.write("\nWelcome to Python programming!")      
file.close()

print("Data appended to Data.txt successfully.")    

file = open("Data.txt", "r")
updated_content = file.read()   
print("Updated content of Data.txt:\n", updated_content)
file.close()
