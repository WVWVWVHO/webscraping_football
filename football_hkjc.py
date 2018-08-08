from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
from openpyxl import Workbook

book = Workbook()
sheet = book.active
header = ('Matchup','Match Time','Home','Draw','Away')
sheet.append(header)

html = urlopen('http://bet.hkjc.com/football/index.aspx?lang=EN')
print(html)
bs = BeautifulSoup(html, 'html.parser')
#print(bs)
matches = bs.findAll('tr',{'class': ["rAlt1", "rAlt0"]})
#print(matches)
for match in matches:
    rates = {"home":0,"draw":0,"away":0}
    matchup = match.find('td','cteams').text
    datetime = match.find('td','cesst').text
    rate_td = match.findAll('td','codds')
    rates["home"]=rate_td[0].text
    rates["draw"] = rate_td[1].text
    rates["away"] = rate_td[2].text
    rows = (matchup, datetime, rates["home"],rates["draw"],rates["away"])
    sheet.append(rows)
    print(rows)

book.save('football.xlsx')

print('Completed')