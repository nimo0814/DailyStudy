"""
目的：在这个游戏中，任务是创建一个脚本，能够在一个范围内生成一个随机数。
如果用户在三次机会中猜对了数字，那么用户赢得游戏，否则用户输。
"""
import random
number=random.randint(1,10)
for i in range(0,3):
    user=int(input("guess the number:"))
    if user==number:
        print("Hurray!!")
        print(f"you guessed the number right it's {number}")
        break
    elif user>number:
        print("Your guess is too high")
    elif user<number:
        print("Your guess is too low")
else:
    print(f"Nice Try!,but the number is {number}")