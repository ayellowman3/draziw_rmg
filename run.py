from selenium import webdriver
import pandas as pd
from localPath import *

lPath = localPath.path

driver = webdriver.Chrome(executable_path=r'/Users/georgehuang/chromedriver.exe')

url = "https://basketball.realgm.com/nba/draft/prospects/stats"

driver.get(url)
#<tr><td class='nowrap'>
#<a href="/player/Markus-Howard/Summary/81690">Markus Howard</a></td>
#<td>MU</td><td>8</td><td>30.5</td><td>7.1</td><td>17.1</td><td>.416</td><td>3.8</td><td>8.4</td><td>.448</td><td>7.1</td><td>8.4</td><td>.851</td><td>0.2</td><td>2.1</td><td>2.4</td><td>2.8</td><td>0.8</td><td>0.1</td><td>25.1</td></tr>

items = len(driver.find_elements_by_class_name("nowrap"))
#items = 95
print(items)
total = []
players = driver.find_elements_by_class_name("nowrap")
for item in range(1, items):
    print(players[item].text)
    #for player in players:
    total.append(players[item].text)
    print(item)
df = pd.DataFrame(total)
df.to_csv('players.csv')
driver.close()
