"""
目标：创建一个命令行游戏，游戏者可以在石头、剪刀和布之间进行选择，与计算机PK。
如果游戏者赢了，得分就会添加，直到结束游戏时，最终的分数会展示给游戏者。
提示：接收游戏者的选择，并且与计算机的选择进行比较。
计算机的选择是从选择列表中随机选取的。如果游戏者获胜，则增加1分。
"""

import random
choices=["Rock","Paper","Scissor"]
computer=random.choices(choices)
player=False
cpu_score=0
player_score=0
while True:
    player=input("Rock,Paper or Scissors?").capitalize()
    #判断游戏者和电脑的选择
    if player==computer:
        print("Tie")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("You win!",player,"smashes",computer)
            player_score+=1
    elif player=="Paper":
        if computer=="Scissors":
            print("You lose",computer,"cut",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose!",computer,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cut",computer)
            player_score+=1
    elif player=="Exit":
        print("final scores:")
        print(f"computer:{cpu_score}")
        print(f"player:{player_score}")
        break
    else:
        print("That's not a valid play. Check your spelling!")
    computer=random.choices(choices)

