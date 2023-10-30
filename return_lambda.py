def times(n):
    return lambda x:x*n
double=times(2)
result=double(3)
print(result)
triple=times(3)
result=triple(3)
print("Triple value print :")
print(result)