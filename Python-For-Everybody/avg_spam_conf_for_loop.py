# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    try :
        # find() returns -1 if substring not found
        sfind_start = line.find(":") + 1
    except :
        # index() returns a traceback error if not found
        sfind_start = line.index(":")
        quit()
    sval = line[sfind_start:].strip()
    fval = float(sval)
    total = total + fval
    count = count + 1
average = total / count
print(f"Average spam confidence: {average}")
# print("Done")

