smallest = None
print(f"Before entering loop: null value")
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value

print(f"Smallest: {smallest}")
print(f"Value in list: {value}")

