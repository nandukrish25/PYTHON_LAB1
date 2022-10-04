a=int(input('enter a nuber:'))

for x in range(1,a+1):
	b=a%x
	if b==0:
		print(x)
	