#subsets of true or false
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
print(numbers.issubset(scores))

#subsets of true or false
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
print(scores.issubset(numbers))

#subsets <=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores<=numbers
print(result)

#subsets <=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers<=numbers
print(result)

#substes <=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores<=scores
print(result)

#subsets >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores>=numbers
print(result)

#subsets >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers>=numbers
print(result)

#substes >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores>=scores
print(result)


#subsets <
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores<numbers
print(result)

#subsets <
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers<numbers
print(result)

#substes <
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores<scores
print(result)