import numpy as np

s="2+8/2*(5+5+3)"
stack_num=[]
stack_fuhao=[]


for value in s:
    if value>='1' and value<='9':
        stack_num.append(int(value))
    else:
        stack_fuhao.append(value)

while stack_fuhao is not None:
    fuhao_1=stack_fuhao.pop()
    if fuhao_1==')':
        while stack_fuhao[-1] is not  '(':
            fuhao_2=stack_fuhao.pop()
            num1=stack_num.pop()
            num2=stack_num.pop()
            if fuhao_2=='+':
                stack_num.append(num1+num2)
            elif fuhao_2=='*':
                stack_num.append(num1*num2)
            elif fuhao_2=='-':
                stack_num.append(num2-num1)
            elif fuhao_2=='/':
                stack_num.append(num2/num1)
        stack_fuhao.pop()
    else:
        num1 = stack_num.pop()
        num2 = stack_num.pop()
        if fuhao_1 == '+':
            stack_num.append(num1 + num2)
        elif fuhao_1 == '*':
            stack_num.append(num1 * num2)
        elif fuhao_1 == '-':
            stack_num.append(num2 - num1)
        elif fuhao_1 == '/':
            stack_num.append(num2 / num1)
    print(stack_num)




