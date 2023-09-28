telugu=98     
english=85       
sanskrit=73      
maths=89         
social=25        
if(telugu>english and telugu>sanskrit and telugu>maths and telugu>social):
	print("The higest marks telugu",telugu)
else:
	if(english>telugu and english>sanskrit and english>maths and english>social):
		print("The higest marks english",english)
	else:
		if(sanskrit>telugu and sanskrit>english and sanskrit>maths and sanskrit>social):
			print("The higest marks sanskrit",sanskrit)
		else:
			if(maths>telugu and maths>sanskrit and maths>english and maths>social):
				print("The higest marks maths",maths)
			else:
				print("The higest marks social",social)
total=telugu+english+sanskrit+maths+social
print("The total marks of all subjects",total)
percentage=total/5
print("The percentage",percentage)
if(telugu<english and telugu<sanskrit and telugu<maths and telugu<social):
	print("The lowest marks telugu",telugu)
else:
	if(english<telugu and english<sanskrit and english<maths and english<social):
		print("The lowest marks english",english)
	else:
		if(sanskrit<telugu and sanskrit<english and sanskrit<maths and sanskrit<social):
			print("The lowest marks sanskrit",sanskrit)
		else:
			if(maths<telugu and maths<sanskrit and maths<english and maths<social):
				print("The lowest marks maths",maths)
			else:
				print("The lowest marks social",social)

if(telugu<50):
	print("The smallest marks telugu",telugu)
else:
	if(english<50):
		print("The smallest marks english",english)
	else:
		if(sanskrit<50):
			print("The smallest marks sanskrit",sanskrit)
		else:
			if(maths<50):
				print("The smallest marks maths",maths)
			else:
				print("The smallest marks social",social)
    
if(telugu<35):
	print("The failed subject telugu",telugu)
else:
	if(english<35):
		print("The failed subject english",english)
	else:
		if(sanskrit<35):
			print("The failed subject sanskrit",sanskrit)
		else:
			if(maths<35):
				print("The failed subject maths",maths)
			else:
				print("The failed subject social",social)