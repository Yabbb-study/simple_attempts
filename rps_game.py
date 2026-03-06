#rock_paper_scissors/rps_game（剪刀石头布）
import random
print("欢迎游玩猜拳模拟器"
      "1、2、3分别表示剪刀石头布！"
      "0为退出游戏^ w ^")
while True:
    opposite=random.randint(1, 3)
    player=int(input("请选择："))
    if opposite==player:
        print("电脑对选手使用了", opposite, "!")
        print("什么？选手与电脑打平了？！")
    elif player==1 and opposite==3:
        print("电脑对选手使用了", opposite, "!")
        print("选手成功拿下一局！")
    elif player==2 and opposite==1:
        print("电脑对选手使用了", opposite, "!")
        print("好一个出奇制胜！")
    elif player==3 and opposite==2:
        print("电脑对选手使用了", opposite, "!")
        print("难道你真的是天才？！")
    elif player==3 and opposite==1:
        print("电脑对选手使用了", opposite, "!")
        print("惜败，惜败......")
    elif player==2 and opposite==3:
        print("电脑对选手使用了", opposite, "!")
        print("再试试！一定可以的。")
    elif player==1 and opposite==2:
        print("电脑对选手使用了", player, "!")
        print("真可惜，再试试吧......")
    elif player==0:
        print("感谢游玩！！！")
        break
    else:
        print("这难道是剪刀石头布的隐藏招式？")
