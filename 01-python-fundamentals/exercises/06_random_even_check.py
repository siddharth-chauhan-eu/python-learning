import random

number = random.randint(1, 100)

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
