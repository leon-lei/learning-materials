import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')   # beautiful soup object we can interact with

# title of the page
print(soup.title)

# get attributes:
print(soup.title.name)

# get values:
print(soup.title.string)

# beginning navigation:
print(soup.title.parent.name)

# getting specific values:
print(soup.p)

# printing what's between the paragraph tags in the source code
print(soup.find_all('p'))

# iterate through the tags
for paragraph in soup.find_all('p'):
    print(paragraph.string)   # paragraph.string will return navigable string as None if there are child tags
    # print(paragraph.text)

print(soup.get_text())

for url in soup.find_all('a'):
    print(url)
