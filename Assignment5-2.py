# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    # This checks to make sure its a number or done
    try:
        num = input("Enter a number: ")

        if num == "done":
            break

        # Converts to an int
        num_value = int(num)

        # Checks for largest number
        if largest is None:
            largest = num_value
        if num_value > largest:
            largest = num_value

        # Checks for smallest number
        if smallest is None:
            smallest = num_value
        if num_value < smallest:
            smallest = num_value

    except:
        print('Invalid input')


print("Maximum is", largest)
print("Minimum is", smallest)
