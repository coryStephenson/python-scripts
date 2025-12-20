# Use the file name mbox-short.txt as the file name
total = 0
count = 0
while True :
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print(f"Average: {average}")

