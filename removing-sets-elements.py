#removing the elements from the sets list
subjects={'python','java','aws','devops'}
subjects.remove('aws')
print(subjects)

#discarding the elements from the sets list
subjects={'python','java','aws','devops'}
subjects.discard('aws')
print(subjects)

#returing the elements from the sets list
subjects={'python','java','aws','devops'}
subject=subjects.pop()
print(subjects)

#cleaning the elements from the sets list
subjects={'python','java','aws','devops'}
print("Before cleaning")
print(subjects)

print("After cleaning")
subjects.clear()
print(subjects)