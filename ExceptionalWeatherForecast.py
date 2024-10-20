# Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

# Task 1
# Prompt the user to enter the temperature in Fahrenheit
fahrenheit = int(input("Enter the temperature in Fahrenheit: "))

# Task 2
# Define a function that converts Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):

    # Convert Fahrenheit to Celsius
    try:
        celsius = (fahrenheit - 32) * 5/9

    # Catch the ValueError exception
    except ValueError:
        return "Please enter a valid number."
        return None
    # Task 3

    # Print the result in Celsius and provide additional information based on the temperature
    else:

        # Print the result in Celsius to two decimal places
        print(f'{fahrenheit}°F is equal to {celsius:.2f}°C.')
        if celsius < 0:
            print("It's freezing!")
        elif celsius < 15:
            print("It's cold.")
        elif celsius > 50:
            print("It's hot!")
        else:
            print("It's just right.")

    # Task 4
    # Finally block to thank the user for using the application
    finally:
        print("Thank you for using the weather forecast application.")

# Call the function and print the result
print(convert_to_celsius(fahrenheit))