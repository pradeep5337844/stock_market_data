import requests
url = 'http://www1.nseindia.com/archives/equities/bhavcopy/pr/PR260521.zip'
r = requests.get(url, allow_redirects=True)
open('bhavcopy.zip', 'wb').write(r.content)