from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests
import random

probs = [0.45, 0.15, 0.15, 0.1, 0.05, 0.05, 0.05]
def Decision(college, exceldict, columns):
    name = exceldict['College'][college]
    print(name)
    chance = 0
    for i in range(1, len(exceldict.keys())):
            random_num = random.random()
            college_chance = exceldict[columns[i]][college]
            print(columns[i]+':', 'Random', str(random_num)+';', 'College Prob', college_chance)
            if random_num < college_chance:
                chance+=probs[i-1]
    if name == 'RPI':
        chance+=0.05
    print(chance)
    decider = random.random()
    print(decider)
    return decider < chance
'''
def get_rates():
    for college in colleges:
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
        for i in range(2, len(exceldict['College'])+2):
            wks.cell(row=i, column=3).value = acceptance_rates[i-2]/100

#WriteAcceptanceRates()
book.save(filename)
book.close
'''