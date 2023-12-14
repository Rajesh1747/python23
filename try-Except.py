# try except 
a=20
b=4
try:
    c=a/b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print('Finising up.')