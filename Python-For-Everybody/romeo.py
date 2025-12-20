# Initialize an empty list to store the unique words.
lst = []

# Prompt the user for input
fname = input("Enter file name: ")

# Open the file 'romeo.txt' for reading.
fhand = open(fname, "r")

# Iterate over each line in the file.
for line in fhand :
    
    # Split the line into a list of words.
    words = line.split()

    # Iterate over each word in the list of words.
    for word in words :
        # Check if the word is already in the lst list.
        # If it is not, append it.
        if word not in lst :
            lst.append(word)
  

# After processing all lines, sort the list of unique words.
lst.sort()

# Print the final sorted list.
print(lst)
    
    

    
    

