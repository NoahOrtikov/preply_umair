# a class has multiple students and they obtained from 0 to 100 marks in maths
# their score are like this
Student_scores = {'Student1': 72, 'Student2': 89, 'Student3': 93, 'Student4': 65, 'Student5': 81, 'Student6': 77, 'Student7': 55, 'Student8': 98, 'Student9': 86, 'Student10': 67, 'Student11': 74, 'Student12': 91, 'Student13': 79, 'Student14': 50, 'Student15': 94, 'Student16': 88, 'Student17': 69, 'Student18': 75, 'Student19': 97, 'Student20': 53}

# find the average of class
scores = Student_scores.values()
print('average',sum(scores)/len(scores))
# find the student with minimum score
print('minimum',min(scores))
# find te student who has maximum score
print('maximum',max(scores))
# write the name of studen who has score more than 80
for k,v in Student_scores.items():
    if v>80:
        print(v,k)