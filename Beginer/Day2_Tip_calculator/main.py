"""
Tip calculator
"""
print("Welcom to the tip calculator.")
total_bill = float(input("What was the total bill? "))
number_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 0, 10, 12, or 15? "))
pay_per_person = total_bill / number_of_people
print(f"Each person should pay: {round(pay_per_person + (pay_per_person *(tip_percentage / 100)),2):.2f}")
