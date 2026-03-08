#rock_paper_scissors/rps_game（剪刀石头布）
import random
print("欢迎游玩猜拳模拟器"
      "1、2、3分别表示剪刀石头布！"
      "0为退出游戏^ w ^")
player_grade=0
opposite_grade=0
win_rules = {
        1: 3,  # 剪刀(1) 赢 布(3)
        2: 1,  # 石头(2) 赢 剪刀(1)
        3: 2  # 布(3) 赢 石头(2)
    }
while True:
    opposite=random.randint(1, 3)
    player=int(input("请选择："))
    if player == 0:
        if opposite_grade > player_grade:
            print(f"{opposite_grade}:{player_grade},电脑获胜。")
        elif opposite_grade < player_grade:
            print(f"{player_grade}:{opposite_grade},选手获胜。")
        else:
            print(f"{player_grade}:{opposite_grade},平局！。")
        print("感谢游玩！！！")
        break
    if player not in [1, 2, 3]:
        print("这难道是剪刀石头布的隐藏招式？")
        continue
    if player == opposite:
        print("平局！")
    elif win_rules[player] == opposite:
        print("玩家赢了！")
        player_grade += 1
    else:
        print("电脑赢了！")
        opposite_grade += 1
