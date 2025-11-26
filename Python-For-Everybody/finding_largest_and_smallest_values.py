largest = None
smallest = None
numbers = []

# Initiate infinite loop
while True:
    # Prompt user for input
    num = input("Enter a number: ")
    
    # Exit mechanism
    if num == "done":
        break
    
    # Input validation
    try :
        inum = int(num)
    except :
        print("Invalid input. Continuing...")
        continue
    
    # Populate an empty list
    numbers.append(inum)
    
# Accumulators
    
print(f"Finding largest number...")
largest_so_far = -1
# print(f"Before entering for loop: {largest_so_far}")
    
for inum in numbers :
    if inum > largest_so_far :
        largest_so_far = inum
print(f"Maximum is {largest_so_far}")

print(f"Finding smallest number...")
smallest = None
# print(f"Before entering loop: null value")
for inum in numbers :
    if smallest is None :
        smallest = inum
    elif inum < smallest :
        smallest = inum

print(f"Minimum is {smallest}")



    
    


