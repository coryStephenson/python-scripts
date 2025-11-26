count = 0
total = 0.0

# Initiate infinite loop
while True :
    # Prompt user for input
    sval = input("Enter a value: ")
    
    # Exit mechanism
    if sval == "done" :
        break
    # Input validation
    try :
        fval = float(sval)
    except :
        print("Invalid input")
        continue

    # Accumulators
    count = count + 1
    total = total + fval

# Print output
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {total / count}")

