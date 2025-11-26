largest_so_far = -1
print(f"Before entering loop: {largest_so_far}")
for the_num in [9, 41, 12, 3, 74, 15] :
    if the_num > largest_so_far :
        largest_so_far = the_num 
    print(f"Largest value: {largest_so_far}")
    print(f"Value in list: {the_num}")

print(f"After exiting loop: {largest_so_far}")
