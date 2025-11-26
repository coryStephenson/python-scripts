def computepay(h, r):
    if h > 40.0 :
        base_pay = 40 * r
        overtime_pay = 1.5 * r * (h - 40)
        gross_pay = base_pay + overtime_pay
    return gross_pay

hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")

try :
    h = float(hrs)
    r = float(rph)
except :
    print("Error, please enter numeric input")
    quit()
    
p = computepay(h, r)
print("Pay", p)
