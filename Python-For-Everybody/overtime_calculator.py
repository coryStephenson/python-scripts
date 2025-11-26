# Overtime Calculator


hrs = input("Enter Hours:")
rph = input("Enter rate per hour:")

try :
    h = float(hrs)
    r = float(rph)
except :
    print("Error, please enter numeric input")
    quit()

print(f"You entered: {hrs} hours")
print(f"You entered: {rph} dollars")

if h > 40.0 :
    base_pay = 40 * r
    overtime_pay = 1.5 * r * (h - 40)
    gross_pay = base_pay + overtime_pay
    print(f"\n\n")
    print(f"Base pay: ${base_pay}")
    print(f"Overtime pay: ${overtime_pay}")
    print(f"Gross pay: ${gross_pay}")
else :
    print(f"\n\n")
    print(f"Base pay: ${base_pay}")
    print(f"Gross pay: ${gross_pay}")


