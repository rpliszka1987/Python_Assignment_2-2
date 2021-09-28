# Assignemtn 3.1

hrs = input("Enter Hours:")
h = float(hrs)

pay = input("Enter pay:")
p = float(pay)

if h <= 40:
    check = h * p
    print(check)
elif h > 40:
    check = 40 * p
    overTime = (h - 40) * (p * 1.5) + check
    print(overTime)
