import re

pattern = r"^@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+$"
pattern_find_digits = r"\d"
num = int(input())

for i in range(num):
    text = input()
    product_group = ""
    matches = re.findall(pattern, text)
    if not matches:
        print("Invalid barcode")
    else:
        digits = re.findall(pattern_find_digits, "".join(matches))
        if not digits:
            product_group = "00"
        else:
            for d in digits:
                product_group += d

        print(f"Product group: {product_group}")
