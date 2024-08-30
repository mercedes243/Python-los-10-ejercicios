price = input("Enter the price of the product in euros (with two decimal places): ")

price_float = float(price)

euros = int(price_float)
cents = int(round((price_float - euros) * 100))

print(f"Euros: {euros}")
print(f"Cents: {cents}")
