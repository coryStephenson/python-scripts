attendees = ['seth', 'katie', 'joe']


print(f"{attendees[-1].title()} cannot attend the dinner. Inviting someone else...\n")

attendees[-1] = 'judy'

greeting = attendees[-1]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-2]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")

greeting = attendees[-3]
print(f"Hello {greeting.title()}, how are you doing? I cordially invite you to dinner.")
