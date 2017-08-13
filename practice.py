import bs4 as bs
import urllib.request
#
# sauce = urllib.request.urlopen('https://www.carmax.com/sitemap.xml').read()
# stew = bs.BeautifulSoup(sauce, 'xml')
# for url in stew.find_all('loc'):
#     print(url.text)

try:
    url = 'https://www.carmax.com/sitemap.xml'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('carmax_sitemap.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

    print('We have the data!')

except Exception as e:
    print(str(e))