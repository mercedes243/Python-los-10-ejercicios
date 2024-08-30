birth_date = input("Enter a birth date (dd/mm/yyyy): ")

day, month, year = birth_date.split('/')

day = int(day)
month = int(month)

print("Day:", day)
print("Month:", month)
print("Year:", year)
