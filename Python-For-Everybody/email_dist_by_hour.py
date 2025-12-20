# Prompt the user for a file name, defaulting to "mbox-short.txt" if no name is entered.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Use a try-except block to gracefully handle cases where the file is not found.
try:
    handle = open(name)
except FileNotFoundError:
    print(f"Error: File '{name}' not found.")
    exit()

# Initialize a dictionary to store the counts for each hour.
hour_counts = dict()

# Read through the file line by line.
for line in handle:
    # Remove trailing whitespace from the line.
    line = line.rstrip()
    
    # We are only interested in lines that start with 'From '.
    # The space is important to exclude lines like 'From:'.
    if not line.startswith('From '):
        continue
    
    # Split the line into a list of words.
    words = line.split()
    
    # The time string is the sixth word (at index 5).
    # Example: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
    #                                               ^^       ^   ^
    #                                               0       1   2
    # We want the '09:14:16' part.
    time_string = words[5]
    
    # Split the time string by the colon to get the hour.
    # '09:14:16' -> ['09', '14', '16']
    hour = time_string.split(':')[0]
    
    # Add the hour to the dictionary and increment its count.
    hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Close the file handle as it's no longer needed.
handle.close()

# --- Sort the hours and print the counts ---

# To print the results sorted by hour, we need to sort the keys of the dictionary.
# We create a new list containing the sorted keys.
sorted_hours = sorted(hour_counts.keys())

# Loop through the sorted list of hours and print the hour and its count.
for hour in sorted_hours:
    print(hour, hour_counts[hour])
