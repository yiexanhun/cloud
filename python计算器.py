print("欢迎来到中文简体简便计算器!")
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

# 主程序
while True:
    # 获取用户输入的数值和运算符
    num1 = float(input("请输入:第一个数："))
    operator = input("请输入:运算符号（+、-、*、/）：")
    num2 = float(input("请输入:第二个数："))

    # 调用calculate函数执行运算，并输出结果
    result = calculate(num1, num2, operator)
    if result is not None:
        print("=：", result)
    else:
        print("输入的运算符号不正确，请重新输入！")

    # 询问用户是否继续运算
    flag = input("是否继续运算？（Yes/No）")
    if flag == 'No' or flag == 'no':
        break
