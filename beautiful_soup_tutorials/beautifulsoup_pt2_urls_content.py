import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source, 'lxml')

# Now, rather than working with the entire soup, we can specify a new Beautiful Soup object.
# An example might be:
# the navigation bar
nav = soup.nav

# next we grab the links from just the nav bar
for url in nav.find_all('a'):
    print(url.get('href'))

# get the body
body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

# Sometimes there might be multiple tags with the same names, but different classes,
# and you might want to grab information from a specific tag with a specific class.
# For example, our page that we're working with has a div tag with the class of "body"
for div in soup.find_all('div', class_='body'):
    print(div.text)
