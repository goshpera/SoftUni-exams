import re

pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

text = input()
matches = re.findall(pattern, text)
points = 0
locations = []

for match in matches:
    location = match[1]
    locations.append(location)
    for char in location:
        points += 1

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {points}")
