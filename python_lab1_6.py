a=input('enter a string:')
i=len(a)-1
b=''


while i>=0:
	b+=a[i]
	i-=1

if a==b:
  print(' This string is a palindrome')	
else:
  print(' This string is not a palindrome')  