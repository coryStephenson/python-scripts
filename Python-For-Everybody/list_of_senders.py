count = 0
fname = input("Enter file name: ")
fhand = open(fname, "r")

for line in fhand :
    
    line = line.rstrip()
    # print("Line:",line)
    if not line.startswith("From ") : 
        continue
    words = line.split()
    # print("Words:",words)
    # guardian pattern
    if len(words) < 1 :
        continue
    if words[0] != "From" :
        # print("Ignore")
        continue
    print(words[1])
    count = count + 1
    
    
print("There were", count, "lines in the file with From as the first word")

