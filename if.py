telugu= float (input("the telugu subject marks"))
hindi=float (input("the hindi subject marks"))
english=float (input("the english subject marks"))
social=float (input("the social subject marks"))
science=float (input("the science subject marks"))

print("/n telugu subjects marks",telugu)
print("/n hindi subjects marks",hindi)
print("/n english subjects marks",english)
print("/n social subjects marks",social)
print("/n science subjects marks",science)

total=telugu+hindi+english+social+science
print("the total value of all 5 subjects",total)
average=total/5
print("/n the average value of all subjects",average)

if(telugu>hindi and telugu>english and telugu>social and telugu>science):
	print("The higest marks telugu",telugu)
else:
	if(hindi>telugu and hindi>english and hindi>social and hindi>science):
		print("The higest marks hindi",hindi)
	else:
		if(english>hindi and english>telugu and english>social and english>science):
			print("The higest marks english",english)
		else:
			if(social>hindi and social>english and social>telugu and social>science):
				print("The higest marks social",social)
			else:
				print("The higest marks science",science)
if(telugu<hindi and telugu<english and telugu<social and telugu<science):
	print("The lowest marks telugu",telugu)
else:
	if(hindi,telugu and hindi<english and hindi<social and hindi<science):
		print("The lowest marks hindi",hindi)
	else:
		if(english<hindi and english<telugu and english<social and english<science):
			print("The lowest marks english",english)
		else:
			if(social<hindi and social<english and social<telugu and social<science):
				print("The lowest marks social",social)
			else:
				print("The lowest marks science",science)
if(telugu<35):
	print("The failed subject telugu",telugu)
else:
	if(hindi<35):
		print("The failed subject hindi",hindi)
	else:
		if(english<35):
			print("The failed subject english",english)
		else:
			if(science<35):
				print("The failed subject science",science)
			else:
				print("The failed subject social",social)