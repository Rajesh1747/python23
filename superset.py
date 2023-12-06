#superset of true false
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
print(numbers.issuperset(scores))

#superset of true false 
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
print(scores.issuperset(numbers))

#superset >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores>=numbers
print(result)

#superset >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers>=numbers
print(result)

#superset >=
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores>=scores
print(result)

#superset of >
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers>scores
print(result)

#superset of >
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers>numbers
print(result)

#superset of >
numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=scores>scores
print(result)


numbers={1,2,3,4,5,6,7,8}
scores={1,2,3,4}
result=numbers>=scores
print(result)