from CollegeCalculator import exceldict, columns
from CollegeCalculator.admitrate import Decision
f = exceldict
c = columns
colleges = f['College']
collegedict = {}
for i in range(len(colleges)):
    collegedict[colleges[i]] = i

'''
college = 'MIT'
decision = Decision(collegedict[college], f, c)
'''
college = int(input())
decision = Decision(college, f, c)


if decision:
    print('Accepted! Congrats!')
else:
    print('Rejected! Maybe next time!')
