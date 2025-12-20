abc = "With three words"
stuff = abc.split()
print(stuff)
print(len(stuff))
print(f"Print using list index: \n{stuff[0]}")

print(f"Print using for loop: ")
for w in stuff :
    print(w)

print(f"\n\nWhen you do not specify a \ndelimiter, "
       "multiple spaces are treated like \n"
       "a delimiter.\n")


line = " A lot               of spaces"
print(f"line = {line}\n")
etc = line.split()
print(etc)

line = "first;second;third"
thing = line.split()
print(thing)
print(len(thing))

print(f"\n\nYou can specify what \n"
       "delimiter character to \n"
       "use in the splitting.\n")

thing = line.split(";")
print(thing)
print(len(thing))
