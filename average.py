print("Enter numbers one by one. Type 'done' to exit.\n")

numbers = []
while True:
    user_input = input("Enter number (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

average = sum(numbers)/len(numbers)
print(f"The average of {len(numbers)} numbers is: {average}")