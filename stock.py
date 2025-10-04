import requests
import pandas as pd
import collections
collections.Callable = collections.abc.Callable
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 
df=pd.DataFrame(columns=['S.No.','Name','CMP Rs.','P/E','Mar Cap Rs.Cr.','Div Yld %','NP Qtr Rs.Cr.','Qtr Profit Var %','Sales Qtr Rs.Cr.','Qtr Sales Var %','ROCE %','Avg Vol 1Wk','Avg Vol 1Yr','1wk return %'])
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://www.screener.in/screens/440753/price-volume-action/"
driver.get(url)
time.sleep(3)  

option=driver.find_element(By.XPATH,"/html/body/main/div[2]/div[5]/table")
option.click()
time.sleep(3)
page_data=driver.page_source
driver.quit()
soup=BeautifulSoup(page_data,'html.parser')
t_name = soup.find("table", class_="data-table text-nowrap striped mark-visited no-scroll-right")
row=t_name.find_all("tr")

for i in row[1:]: # skip header
    data = i.find_all("td")
    row_data = [(d.text).strip() for d in data]
    if len(row_data) == len(df.columns):  # ensure data matches column count
        df.loc[len(df)] = row_data
# print(df)
df.to_csv("Stock_data.csv",sep="\t",index=False)