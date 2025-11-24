# Overtime Calculator


hrs = input("Enter Hours:")
h = int(hrs)

rph = input("Enter rate per hour:")
r = float(rph)


if h > 40.0 :
    gross = 40 * r
    overtime = 1.5 * r * (h - 40)
    pay = gross + overtime
    print(f"Overtime pay: {pay}")
else :
    print(f"Gross pay: {gross}")

