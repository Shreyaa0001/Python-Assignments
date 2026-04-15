#creat a file taking user input contain FileNotFoundError and PermissionError


file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        content = file.read()   
except FileNotFoundError:
    print("The file you are trying to access does not exist.")  
    print("You do not have permission to access this file.")    
    
