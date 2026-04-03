def convert_to_kelvin(celsius):
    return celsius + 273.15
if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    kelvin = convert_to_kelvin(celsius)
    print(f"{celsius} degrees Celsius is equal to {kelvin} Kelvin.")    