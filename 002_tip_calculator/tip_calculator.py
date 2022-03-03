# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling
# to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

num_people_int = int(num_people)
percentage_tip = int(tip) / 100

total_tip_amount = bill * percentage_tip
total_bill = bill + total_tip_amount
bill_per_person = total_bill / num_people
final_number = round(bill_per_person, 2)
final_number = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_number}")
