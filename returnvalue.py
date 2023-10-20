#multiple Default marameters values in python Function 
def greet (name='\n hi Rajesh', message='\n how are you',data='\n 01/01/2000'):
	return f"{name} {message} {data}"
greeting=greet()
print(greeting)