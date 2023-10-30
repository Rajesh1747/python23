def sum(n):
	if n>=1:
		return n+sum(n-1)
	return 0
result=sum(100)
print(result)