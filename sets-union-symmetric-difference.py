# Intersection with symmetric Difference 
s1={'Python','Java','C++'}
s2={'C#','Java','C++'}
s=s1.symmetric_difference(s2)
print(s)

# Intersection with symmetric Difference 
s1={'Python','Java','C++'}
s2={'C#','Java','C++'}
s=s1^s2
print(s)


# symmetric Difference
s1={1,4,6,8,10,14}
s2=[2,3,5,7,1,6,8,14]
new_set=s1.symmetric_difference(s2)
print(new_set)