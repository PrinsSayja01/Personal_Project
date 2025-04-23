def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def is_valid_number(value):
    """Validate if the input can be converted to a float."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_temperature_input(unit):
    """Get and validate temperature input from the user."""
    while True:
        temp = input(f"Enter temperature in {unit}: ")
        if is_valid_number(temp):
            return float(temp)
        else:
            print(f"Invalid input. Please enter a valid number for {unit}.")

def temperature_converter():
    """Main function to run the temperature converter."""
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == "1":
            celsius = get_temperature_input("Celsius")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
        
        elif choice == "2":
            fahrenheit = get_temperature_input("Fahrenheit")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
        
        elif choice == "3":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    temperature_converter()