from bs4 import BeautifulSoup
import requests
import time
import csv

soup = BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars").text, "html.parser")
rows = soup.find("table").find_all('tr')
data=[]
final = []

for row in rows:
  temp = []  
  for i in row.find_all('td'):
    temp.append(i.text.strip())
    
  data.append(temp)

data.pop(0)

for x in data:
  final.extend([[x[1], x[3], x[5], x[6]]])

with open("data.csv", "w", newline='', encoding='utf-8') as f:
  writer = csv.writer(f)
  writer.writerow(['Name','Distance','Mass','Radius'])
  writer.writerows(final)


