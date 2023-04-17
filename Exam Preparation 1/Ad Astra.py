import re

pattern = r"([#|])([A-Za-z\s])\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
text = input()

matches = re.findall(pattern, text)

total_kcal = 0
products = []

for match in matches:
    product = match[1]
    exp_date = match[2]
    kcal = match[3]

    products.append(f"Item: {product}, Best before: {exp_date}, Nutrition: {kcal}")
    total_kcal += kcal

days = total_kcal // 2000
print(f"You have food to last you for: {days} days")
print("\n".join(products))
