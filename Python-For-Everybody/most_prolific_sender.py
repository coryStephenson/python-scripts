# Prompt the user for a file name, 
# defaulting to "mbox-short.txt" if no name is entered.
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

# Use a try-except block to gracefully 
# handle cases where the file is not found.
try:
    handle = open(name)
except FileNotFoundError:
    print(f"Error: File '{name}' not found.")
    exit()

# Initialize a dictionary to store email counts.
counts = dict()

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
    
    # The email address is the second word (at index 1).
    email = words[1]
    
    # Add the email to the dictionary and increment its count.
    # This is a concise way to do it.
    counts[email] = counts.get(email, 0) + 1

# Close the file handle as it's no longer needed.
handle.close()

# --- Find the most prolific sender ---

# Check if any emails were found to avoid errors.
if not counts:
    print("No 'From ' lines were found in the file.")
else:
    # Initialize variables to track the maximum count and the corresponding email.
    max_count = -1
    prolific_sender = None
    
    # Loop through the dictionary (email, count) pairs.
    for email, count in counts.items():
        # If the current count is greater than the max count found so far,
        # update the max count and the prolific_sender.
        if count > max_count:
            max_count = count
            prolific_sender = email
    
    # Print the final result.
    print(f"The most prolific sender is {prolific_sender} with {max_count} emails.")


