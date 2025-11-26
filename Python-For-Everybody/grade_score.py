score = input("Enter Score: ")

try :
    fscore = float(score)
except :
    print("ERROR: You entered a string. Please enter numeric value.")
    quit()

if fscore < 0.0 or fscore > 1.0 :
    print("ERROR: Please enter a numeric value between 0.0 and 1.0.")
elif fscore >= 0.9 :
    print("A")
elif fscore >= 0.8 :
    print("B")
elif fscore >= 0.7 :
    print("C")
elif fscore >= 0.6 :
    print("D")
elif fscore < 0.6 :
    print("F")
else:
    quit()     
