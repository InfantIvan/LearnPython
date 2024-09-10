import calculator

# Get input from the user
num_list = []
while True:
    try:
        raw_input = input("Enter a number (or 'done' to finish): ")
        num = float(raw_input)
        num_list.append(num)
    except ValueError:
        if raw_input.lower() == 'done':
            break
        else:
            print("Invalid input. Please enter a number or 'done'.")

# Calculate and print the average
average_result = calculator.calculate_average(num_list)
if average_result is not None:
    print(f"The average of the numbers is: {average_result}")
else:
    print("No numbers were entered.")