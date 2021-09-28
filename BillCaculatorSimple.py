# This is a simple bill calculator to get tax, tip and all.

bill = input("Enter the bill ammount: \n")


def billCalculator(value):
    tip = float(value) * 0.20
    return tip


print(billCalculator(bill))
