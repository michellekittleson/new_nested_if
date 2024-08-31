# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
# Task #2: Venue Selections
audio = "audio system" if attendees > 50 else "no audio system required"
visual = "projector" if attendees > 75 else "no projector required"
print(venue)
print(audio)
print(visual)

# Task 3: Catering Choices

catering_choice = input("Do you want vegetarian food? (yes/no) ")
if catering_choice == "yes":
    print("Veggie Delight Caterers")
else:
    print("Gourmet Meal Caterers")