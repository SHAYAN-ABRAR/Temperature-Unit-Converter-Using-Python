unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter The Temperature: "))

if unit == "C" or unit == "c":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The Temperature in Fahrenheit is: {temp} Degree Fahrenheit ")
elif unit == "F" or unit == "f":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The Temperature in Celsius is: {temp} Degree Celsius ")
else:
    print(f"{unit} is an invalid unit of measurement")