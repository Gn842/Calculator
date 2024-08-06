def calculator (num1,num2,operator):
    
    if operator == '+':
        res = num1 + num2

    elif operator == '-':
        res = num1-num2

    elif operator == '/':
        res = num1/num2

    elif operator == '*':
        res = num1*num2

    else:
        res = "ERROR"
    
    return print(res)

calculator(9,3,'=')
