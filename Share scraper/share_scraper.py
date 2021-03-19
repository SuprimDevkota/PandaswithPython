import pandas as pd
import requests
from bs4 import BeautifulSoup
df = pd.read_csv('datasets/share.csv', index_col = 0)

#creating a webscraper to go to sharesansar and get the cash dividend rates of the companies present in my dataframe
cash_div_list = []
comp_list = df.index
for company in comp_list:
    company = company.lower()
    url = 'https://www.sharesansar.com/company/' + company
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        cash_div_raw = soup.find(text="Cash Dividend").findNext().contents[0]
        list_cash = cash_div_raw.split()
        cash_div_list.append(float(list_cash[0]))     
    except:
        cash_div_list.append(0.0)

#creating a new column to hold the data stored in the list created above        
df['Cash Dividend Rate'] = cash_div_list

#getting the actual cash dividends and storing their data to a column as well
cash_dividend = []
x = 0
for company in df.index:
    cash_dividend.append(df['Number of Shares'][x] * df['Cash Dividend Rate'][x])
    x += 1
 df['Cash Dividend'] = cash_dividend

df.to_csv('datasets/cash_div_list.csv)
