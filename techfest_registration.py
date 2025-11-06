print("Welcome to SMIT TechFest!")
print("Event organized by Daniella Kalinisan of APPDAET BTCS1")
print()

#Task 1: Registration Setup
#Ask the event organizer:
num = int(input("How many participants will register? "))

if num <= 0:
    print("Invalid number of participants")
    quit()

#Task 2: Collect Participant Information
participants = []

for i in range(num):
    name = input("Enter participant name: ")
    track = input("Enter chosen track: ")

    record = {"name": name, "track": track}
    participants.append(record) #add to the list

print("\nRegistered participants:")
for i in range(len(participants)):
    print(str(i+1) + ". " + participants[i]['name'] + " - " + participants[i]['track'])

#Task 3: Track Diversity Report
tracks = []
for p in participants:
    tracks.append(p['track'])

unique_tracks = set(tracks)

if len(unique_tracks) < 2:
    print("\nNot enough variety in tracks.")
else:
    print("\nTracks offered in this event: " + ",".join(unique_tracks))
