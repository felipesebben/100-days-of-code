even_numbers = 0

for number in range(0, 101, 2):
    even_numbers += number
print(even_numbers)

# Alternative solution using modulo.
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)
