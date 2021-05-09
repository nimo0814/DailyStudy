import random
number=int(input('Press 1 to roll the dice or 0 to exit:\n'))
while number:
    print(random.randint(1,6))
    break