#井字棋
#本来想设置一个电脑对手，但我还不太会（。_   。）等以后再优化吧！

broad=['1','2','3','4','5','6','7','8','9']
game_running=True
def print_broad():
    count = 0
    for i in range(0,9):
        print(f"[{broad[i]}]",end="")   #end=""在此是为了打印出来的格子能够横着排
        count= count + 1
        if count==3:
            print("\n")
            count=0
print("欢迎游玩井字棋小游戏！玩家需要在以下九个格子中(1--9)"
      "挑选一个格子，输入它的数字，当你的三个棋子在一条线上时即可获胜")
while game_running is True:   #这里可以简化成while game_running:  ！！
    print_broad()
    while True:
        player=int(input("请玩家一输入落棋点："))
        if player in range(1, 10) and broad[player - 1]!= "O" and broad[player - 1]!= "X":
        #这里写 if  p in b:    会被识别成 pin b，虽然不知道为什么......
            broad[player - 1]= "O"
            break
        else:
            print("请输入当前的有效落棋点！")
            print_broad()
            continue
    print_broad()
    # 玩家一落子后立即检查赢家
    win = False
    # 检查行
    rc=(0,3,6)
    for j in rc:
        if broad[j]==broad[j+1]==broad[j+2]:
            if broad[j]=="O":
                print("玩家一赢！")
                win = True
                game_running = False  # 赢了就结束
                break
            elif broad[j]=="X":
                print("玩家二赢！")
                win = True
                game_running = False
                break
    if win: break  # 跳出玩家一循环
    # 检查列
    cc=(0,1,2)
    for k in cc:
        if broad[k]==broad[k+3]==broad[k+6]:
            if broad[k]=="O":
                print("玩家一赢！")
                win = True
                game_running = False
                break
            elif broad[k]=="X":
                print("玩家二赢！")
                win = True
                game_running = False
                break
    if win: break
    # 检查对角线
    if broad[0]==broad[4]==broad[8]:
        if broad[0]=="O":
            print("玩家一赢！")
            win = True
            game_running = False
        elif broad[0]=="X":
            print("玩家二赢！")
            win = True
            game_running = False
    if broad[2]==broad[4]==broad[6]:
        if broad[2]=="O":
            print("玩家一赢！")
            win = True
            game_running = False
        elif broad[2]=="X":
            print("玩家二赢！")
            win = True
            game_running = False
    if win: break
    # 棋盘满检测（玩家一下完后）
    if all(chess in ["O", "X"] for chess in broad):
        print("棋盘已满，游戏结束！正在生成结果")
        # 最后统一检查输赢，所以这里只跳出
        game_running = False
        break
    while True:
        opposite=int(input("请玩家二输入落棋点:"))
        if opposite in range(1, 10) and broad[opposite - 1]!= "O" and broad[opposite - 1]!= "X":
            broad[opposite - 1]= "X"
            break
        else:
            print("请输入有效落棋点！")
            continue
    print_broad()
    # 玩家二落子后立即检查赢家（复制同样的判断）
    win = False
    # 检查行
    rc=(0,3,6)
    for j in rc:
        if broad[j]==broad[j+1]==broad[j+2]:
            if broad[j]=="O":
                print("玩家一赢！")
                win = True
                game_running = False
                break
            elif broad[j]=="X":
                print("玩家二赢！")
                win = True
                game_running = False
                break
    if win: break
    # 检查列
    cc=(0,1,2)
    for k in cc:
        if broad[k]==broad[k+3]==broad[k+6]:
            if broad[k]=="O":
                print("玩家一赢！")
                win = True
                game_running = False
                break
            elif broad[k]=="X":
                print("玩家二赢！")
                win = True
                game_running = False
                break
    if win: break
    # 检查对角线
    if broad[0]==broad[4]==broad[8]:
        if broad[0]=="O":
            print("玩家一赢！")
            win = True
            game_running = False
        elif broad[0]=="X":
            print("玩家二赢！")
            win = True
            game_running = False
    if broad[2]==broad[4]==broad[6]:
        if broad[2]=="O":
            print("玩家一赢！")
            win = True
            game_running = False
        elif broad[2]=="X":
            print("玩家二赢！")
            win = True
            game_running = False
    if win: break
    # 新增结束

    if all(chess in ["O", "X"] for chess in broad):
        print("棋盘已满，游戏结束！正在生成结果")
        game_running = False
        break
#注意！鉴于本人python功底极差
# 接下来的检查行、列、对角线过程可能会异常丑陋！！
#但也是本人想了两节py课想出来的！
#检查行
rc=(0,3,6)
r=0
win = False  # 增加赢家标志
for j in rc:
        r=r+1
        if broad[j]==broad[j+1]==broad[j+2]:
            if broad[j]=="O":
                print("玩家一赢！")
                win = True
            elif broad[j]=="X":
                print("玩家二赢！")
                win = True
# 检查列
cc=(0,1,2)
column=0
for k in cc:
        column+=1  
        if broad[k]==broad[k+3]==broad[k+6]:
            if broad[k]=="O":
                print("玩家一赢！")
                win = True
            elif broad[k]=="X":
                print("玩家二赢！")
                win = True
#检查对角线
if broad[0]==broad[4]==broad[8]:
    if broad[0]=="O":
        print("玩家一赢！")
        win = True
    elif broad[0]=="X":
        print("玩家二赢！")
        win = True
if broad[2]==broad[4]==broad[6]:
    if broad[2]=="O":
        print("玩家一赢！")
        win = True
    elif broad[2]=="X":
        print("玩家二赢！")
        win = True

if not win and all(chess in ["O", "X"] for chess in broad):
    print("无人获胜！")
elif not win:
    print("游戏未结束，继续下棋")
