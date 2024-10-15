"""
1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application 
that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, 
ensuring that this message is displayed regardless of whether an exception was caught or not.
"""
def temperature_to_celsius():
    try: 
        fahrenheit_temperature = int(input("Enter the temperature in fahrenheit: "))
        celsius_temperature = (fahrenheit_temperature - 32) * 5/9
    except ValueError:
        print("That's not a  valid number. Please try again.")
        return
    finally:
        print(f"{fahrenheit_temperature} degrees Fahrenheit is {celsius_temperature} degrees Celsius.")
        print("Thank you for using the weather application.")

temperature_to_celsius()

