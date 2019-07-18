result = []
stock = []
operator = []
A = ['5', '+', '3']
for i in A:
    if i.isdigit():
        stock.append(i)
    else:
        operator.append(i)

for j in operator:
    if j == '+':
        result += stock
    else:
        result -= stock
print(result)

for i in range(10):
    for j in range(0,0 +i):
        print(end=' ')
    for k in range(0 + i, 10):
        print('*', end='')
    print('')


