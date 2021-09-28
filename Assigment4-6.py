# Pay calculation which uses a function.

def computepay(h, r):
    paycheck = 0
    if h >= 40:
        normal = 40 * r
        paycheck = (h - 40) * (r * 1.5) + normal
    else:
        paycheck = h * r

    return paycheck


hrs = input("Enter Hours:")
rate = input("Enter Rate:")
h = float(hrs)
r = float(rate)
p = computepay(h, r)
print("Pay", p)
