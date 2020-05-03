from CollegeCalculator import exceldict, columns
from CollegeCalculator.admitrate import Decision, averageProbability
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
for i in range(len(colleges)):
    decision = Decision(i, f, c)
    average = averageProbability(i, f, c)
    print('Average chance for this school is: ', average)
    if decision < 0:
        print('Accepted! Congrats!')
    else:
        if decision < 0.06:
            print('Waitlisted!')
        else:
            print('Rejected! Maybe next time!')



