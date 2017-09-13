import bs4 as bs
import urllib.request
import pandas as pd

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

table = soup.table
# table = soup.find('table')
# print(table)

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

# using pandas to illustrate same task
dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header=0)
# print(type(dfs))  # class 'list'
for df in dfs:
    print(df)

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
stew = bs.BeautifulSoup(sauce, 'xml')
for url in stew.find_all('loc'):
    print(url.text)
