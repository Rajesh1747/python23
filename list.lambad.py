carts=[['laptop',600],['Tv',6500],['desktop',4500]]
tax=0.2
carts=map(lambda item:[item[0],item[1] *tax],carts)
print(list(carts))