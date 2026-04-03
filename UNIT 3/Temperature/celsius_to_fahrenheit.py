def convert_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")    
    
    
                    