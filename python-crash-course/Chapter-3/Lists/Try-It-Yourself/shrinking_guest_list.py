attendees = ['bob', 'sue', 'seth', 'katie', 'joe', 'ethan']


print(f"NOTICE: I can only invite two people to dinner.\n")


uninvited = attendees.pop(0)
print(f"I am truly sorry {uninvited.title()}. You cannot attend the dinner.\n")


uninvited = attendees.pop(1)
print(f"I am truly sorry {uninvited.title()}. You cannot attend the dinner.\n")


uninvited = attendees.pop(-2)
print(f"I am truly sorry {uninvited.title()}. You cannot attend the dinner.\n")


uninvited = attendees.pop(-1)
print(f"I am truly sorry {uninvited.title()}. You cannot attend the dinner.\n")


print(f"NOTICE: {attendees[0].title()} is still invited to the dinner.\n")


print(f"NOTICE: {attendees[1].title()} is still invited to the dinner.\n")


del attendees[0]
del attendees[0]


print(attendees)
