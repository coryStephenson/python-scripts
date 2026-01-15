A = [1, 2, 3]
B = [4, 5, 6]

cross_x = (2 * 6) - (3 * 5)  # A2B3 - A3B2
cross_y = (3 * 4) - (1 * 6)  # A3B1 - A1B3
cross_z = (1 * 5) - (2 * 4)  # A1B2 - A2B1

cross_product = [cross_x, cross_y, cross_z]
print(cross_product)  # Output: [-3, 6, -3]
