# year = input("Which year do you want to check? ")
#   TypeError - noy all arguments converted during string formatting.
#   Basically, you are trying to do something with the wrong dtype.

year = int(input("Which year do you want to check? "))
# print(type(year)) to check whether you are working with the right dtype.

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
