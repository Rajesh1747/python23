#key words arguments
def base_price(price,discount):
	return price * (1-discount)
net_price=base_price(100,0.3)
print(net_price)

def netprice(price,tax=0.09,discount=0.08):
	return price * (1+tax-discount)
on_net_price=netprice(500)
print(on_net_price)