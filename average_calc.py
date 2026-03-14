#仿B站林粒粒Python-《3小时......》---21---while循环
print("平均值计算器")
count=0
total=0
query=input("请输入数字(按q退出程序并返回结果):")
while query != "q":
    num=float(query)
    total+=num
    count+=1
    query=input("请输入数字(按q退出程序并返回结果):")
if count==0:
    result=0
else:
    result=total/count
print("您输入的数字平均值结果为"+str(result))
