from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import random
import numpy

probs = [0.40, 0.15, 0.15, 0.1, 0.1, 0.05, 0.05]
in_state = ['Rutgers', 'TCNJ', 'Montclair State']
def Decision(college, exceldict, columns):
    name = exceldict['College'][college]
    print(name)
    input(name + "'s decision has been released! Press enter to find out!")
    chance = 0
    for i in range(1, len(exceldict.keys())):
        random_num = random.random()
        college_chance = exceldict[columns[i]][college]
        print(columns[i]+':', 'Random', str(random_num)+';', 'College Prob', college_chance)
        if random_num < college_chance:              
            chance+=probs[i-1]
        else:
            random_2 = random.random()*0.2
            chance+=probs[i-1]*(random_2)
    if name == 'RPI':
        chance+=0.05
        print('RPI Medal: +5%')
    if name in in_state:
        chance+=0.23
        print('In-state: +23%')
    print(chance)
    decider = random.random()
    print(decider)
    return decider-chance

def averageProbability(college, exceldict, columns):
    name = exceldict['College'][college]
    average = 0
    for i in range(1, len(exceldict.keys())):
        random_num = random.random()
        college_chance = exceldict[columns[i]][college]
        if columns[i] == 'Pure Luck (10%)':
            college_chance = numpy.log(5)/4            
        average += probs[i-1]*college_chance
    if name == 'RPI':
        average+=0.05
    if name in in_state:
        average+=0.23  
    return average

'''
def get_rates(college):
    query = college + " acceptance rate"
    query = query.replace(' ', '+')
    URL = f"https://google.com/search?q={query}"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for i in soup.find_all('div', {'class': 'Z0LcW'}):
            acceptance_rates.append(float(i.text[0:-1]))
#get_rates()

book = load_workbook(filename)

def WriteAcceptanceRates():
    for wks in book.worksheets:
        wks.cell(row=len(exceldict['College'])+3, column=3).value = acceptance_rates[i-2]/100

#WriteAcceptanceRates()
book.save(filename)
book.close
'''
