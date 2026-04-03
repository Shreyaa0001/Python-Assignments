def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9
if __name__ == "__main__":
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")    