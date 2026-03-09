# 初始化
history = []
running = True
operators = ['+', '-', '*', '/']

print("=" * 40)
print("=" * 40)
print("命令: history(历史) clear(清空) exit(退出)")
print("=" * 40)
result=0
while running:
    command = input("\n请输入表达式 (如 5+3): ").strip()

    if command == 'exit':
        print("感谢使用！再见！")
        running = False

    elif command == 'clear':
        history = []
        print("历史已清空")

    elif command == 'history':
        if not history:
            print("暂无历史记录")
        else:
            print("\n=== 历史记录 ===")
            for i, record in enumerate(history[-5:], 1):  # 只显示最近5条
                print(f"{i}. {record}")

    elif command:
        # 查找运算符
        op = None
        for o in operators:
            if o in command:
                op = o
                break

        if op:
            parts = command.split(op)
            if len(parts) == 2:
                try:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())

                    if op == '+':
                        result = num1 + num2
                    elif op == '-':
                        result = num1 - num2
                    elif op == '*':
                        result = num1 * num2
                    elif op == '/':
                        if num2 == 0:
                            print("错误：除数不能为0！")
                            continue
                        result = num1 / num2

                    expression = f"{num1} {op} {num2} = {result}"
                    print(f"结果: {result}")
                    history.append(expression)

                except ValueError:
                    print("错误：请输入有效的数字！")
            else:
                print("错误：表达式格式不正确！")
        else:
            print("错误：请使用 +、-、*、/ 运算符")
