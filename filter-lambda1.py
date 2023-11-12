states=[['Andhra pradesh',2.4],['bihar',1.2 ],['goa',1.9 ]]
filtered=filter(lambda state : len(state)>1,states)
print(list(filtered))

