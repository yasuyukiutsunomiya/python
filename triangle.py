for x in range(10):
	for i in range(x,10):
		print('*',end='')
	print('')


for i in range(10):
	for j in range(0,10 - i):
		print(end=' ')
	for n in range(0,0 + i):
		print(end=' ')
	for m in range(0 + i,10):
		print('*',end=' ')
	for k in range(10 - i,10):
		print('*',end=' ')
	print('')

for j in range(10):
	for x in range(0,j):
		print('*',end='')
	for n in range(j,19-j):
		print(' ',end='')
	for k in range(0,j):
		print('*',end='')
	print('')
	