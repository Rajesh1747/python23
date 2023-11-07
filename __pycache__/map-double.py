#map double
def double(rates):
	return rates*3
new_rates=[230,430,546]
print(new_rates)
iteratore=map(double,new_rates)
print(list(iteratore))