telugu=int(input("Enter the marks : "))
hindi=int(input("Enter the marks : "))
english=int(input("Enter the marks : "))
total=telugu+hindi+english
percentage=total/3
if telugu<hindi and telugu<english :
    print("The Lowest marks in Telugu",telugu)
else:
    if hindi<telugu and hindi<english :
        print("The Lowest marks in Hindi",hindi)
    else:
        print("The Lowest marks in English",english)

