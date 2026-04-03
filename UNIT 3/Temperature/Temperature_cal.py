from Temperature import Temperature 
temp = Temperature()
temp.celsius_to_fahrenheit()
temp.celsius_to_kelvin()
temp.fahrenheit_to_celsius()

value = temp.get_value()
print(f"Temperature value: {value}")    

print("Choose the conversion you want to perform (1-3):")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")       
print("3. Fahrenheit to Celsius")
choice = input("Enter your choice (1-3): ")
if choice == '1':   
    temp.celsius_to_fahrenheit()
elif choice == '2':
    temp.celsius_to_kelvin()    
elif choice == '3':   
    temp.fahrenheit_to_celsius()
else:   
    print("Invalid choice. Please enter a number between 1 and 3.")