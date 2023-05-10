#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = abs(number) % 10
else:
    last_digit = ((abs(number) * -1) % 10) * -1

message = f"Last digit of {number:d} is {last_digit:d} and is" % (number, last_digit)

if last_digit == 0:
    print(message, "0")
elif last_digit > 5:
    print(message, "greater than 5")
else:
    print(message, "less than 6 and not 0")
