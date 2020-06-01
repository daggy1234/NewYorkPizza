import requests
url = f'https://api.foursquare.com/v2/venues/search?ll=&query=pizza&radius=500&client_id=QH1UD24PCMOFJJ5ZBWM2Y2QEMQQSOPQ3A2GQQVFEIBR4X3OF&client_secret=ZAC4CWGEWG1GFSDYLSPWLLGYM50EVWF3DZOUJL4MMAXLSMKD&v=20200331'
y = requests.post(url)
r = y.json()
print(r)
l = r['response']['venues']
for e in l:
    print(e['location']['postalCode'])
    print(e['location']['lat'])
    print(e['location']['lng'])
    print(e['name'])
