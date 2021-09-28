# This is a sample for loop to see which number is the greatest passed.

largest_number = 0

for n in [9, 25, 8, 55, 1, 22, 88, 1]:
    if n > largest_number:
        largest_number = n
    print(largest_number, n)

print('Largest value is:', largest_number)
