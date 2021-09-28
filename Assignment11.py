import re

name = input("Enter file name: ")
if len(name) < 1:
    name = "regex_sum_1344475.txt"
fhandle = open(name)


total = 0
for line in fhandle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        total = int(number) + total


print(total)
