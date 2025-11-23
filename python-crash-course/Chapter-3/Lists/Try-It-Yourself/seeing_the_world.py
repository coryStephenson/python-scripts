# Store the locations in a list
locations = ['Hawaii', 'Indonesia', 'Bali', 'New Zealand', 'Tahiti', 'Australia']

# Print the list in its original order
print(locations)

# Temporarily stores the list in alphabetical order
print(f"\n{sorted(locations)}")

# Verify that the list in still in its original order
print(f"\n{locations}")

# Temporarily stores the list in reverse alphabetical order
print(f"\n{sorted(locations, reverse = True)}")

# Verify that the list in still in its original order
print(f"\n{locations}")

# Reverse the sequential order of the list
locations.reverse()
print(f"\n{locations}")

# Reverse the sequential order of the list again, reverting back to the original order
locations.reverse()
print(f"\n{locations}")

# Permanently stores the list in alphabetical order
locations.sort()
print(f"\n{locations}")

# Permanently stores the list in reverse alphabetical order
locations.sort(reverse = True)
print(f"\n{locations}")
