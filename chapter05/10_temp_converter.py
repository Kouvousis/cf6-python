def fahrenheit_to_celsius(temp):
    return round((temp - 32) * 5 / 9, 2)

def main():
    fahrenheit_temps = [32, 67, 90, 102, 75, 68, 55]
    print("Fahrenheit Temperatures:", fahrenheit_temps)
    
    # Convert temperatures using list comprehension.
    celsius_temp_list = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps]
    print("Celsius Temperatures (list comprehension)", celsius_temp_list)
    
    # Convert temperatures using 
    celsius_temp_gen = (fahrenheit_to_celsius(temp) for temp in fahrenheit_temps)
    print("Celsius Temperatures", celsius_temp_gen)
    
    for celsius in  celsius_temp_gen:
        print(celsius, end=' ')
    print()
    
    # Attention!
    print("-" * 30)
    for celsius in  celsius_temp_gen:
        print(celsius, end=' ')
    print()

if __name__ == "__main__":
    main()