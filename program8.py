def Evaluate_Postfix(exps):
    stck = []

    for i in list(exps):
        if i.isdigit():
            stck.append(i)
        else:
            b = stck.pop()
            a = stck.pop()
            stck.append(eval(f'{a}{i}{b}'))
    return int(stck.pop())

print(Evaluate_Postfix('14+93/*'))
print(Evaluate_Postfix("743*15+/*"))