attendees = ['seth', 'katie', 'joe']


print(f"NOTICE: I have found a larger table. Inviting more people...\n")


attendees.insert(0, 'bob')
attendees.insert(0, 'sue')
attendees.append('ethan')


greeting = attendees[-1]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-2]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-3]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-4]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-5]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-6]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")
