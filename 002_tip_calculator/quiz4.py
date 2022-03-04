# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age_int = int(age)

days = (90 - (int(age_int))) * 365
weeks = (90 - (int(age_int))) * 52
months = (90 - int(age_int)) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
a = int('5') / int(2.7)
print(type(a))