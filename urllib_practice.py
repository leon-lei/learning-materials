import urllib.request
import urllib.parse

# base url and values
# urlencode the values onto a variable
# encode (utf-8) the variable
# send the request
# open the request
# read the request
# print the request

# url = 'https://pythonprogramming.net'
# values = {'s':'basic',
#           'submit':'search'}
#
# data = urllib.parse.urlencode(values)  #encode the values as they should be in URL, %20 for spaces
# data = data.encode('utf-8')  #utf-8 just a type of encoding, puts it in bytes
# req = urllib.request.Request(url,data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
#
# print(respData)
#
# websites will block your request if they read the headers
# headers from regular python requests appear as python.urllib
# fake the headers by overwriting them in the request
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')

    print(x.read())

except Exception as e:
    print(str(e))

try:
    url = 'https://www.google.com/search?q=test'

    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()

    print('Headers method works!')

except Exception as e:
    print(str(e))