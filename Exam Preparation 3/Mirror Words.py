import re

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]){3,}\1"
data = input()
mirrored_words = []

matches = re.findall(pattern, data)

for match in matches:
    first_word = match[1]
    second_word = match[2]

    if first_word == second_word[::-1]:
        mirrored_words.append(first_word + " <=> " + second_word)

if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")

if len(mirrored_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirrored_words))
