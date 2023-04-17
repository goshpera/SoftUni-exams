import re

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+)\s([A-Za-z]+)#"
num = int(input())

for i in range(num):
    text = input()
    matches = re.findall(pattern, text)
    if bool(matches):
        for match in matches:
            boss_name = match[0]
            job_1 = match[1]
            job_2 = match[2]

            print(f"{boss_name}, The {job_1} {job_2}")
            print(f">> Strength: {len(boss_name)}")
            print(f">> Armor: {len(job_1) + len(job_2) + 1}")

    else:
        print("Access denied!")
