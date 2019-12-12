from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:\Users\George\Documents\Coding\chromedriver.exe')

url = "https://basketball.realgm.com/nba/draft/prospects/stats"

driver.get(url)
#//*[@id="table-6081"]/tbody/tr[1]/td[1]
#//*[@id="table-6081"]/tbody/tr[2]/td[1]
#//*[@id="table-6081"]/tbody/tr[95]
items = len(driver.find_elements_by_tag_name("nowrap tablesaw-cell-persist"))
#items = 95
print(items)
total = []
for item in range(1, items):
    players = driver.find_elements_by_id("nowrap tablesaw-cell-persist")
    #for player in players:
    total.append(players)
df = pd.DataFrame(total)
df.to_csv('players.csv')
driver.close()
