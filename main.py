def calculator(a, b, k='+'):
    return eval(f'{a} {k} {b}')
print(calculator(a = 2, k = '*', b = 5))