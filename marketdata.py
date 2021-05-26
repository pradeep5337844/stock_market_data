import wget
print(f"")
print("enter the date in ddmmyy format")
print(f"")
a = 'http://www1.nseindia.com/archives/equities/bhavcopy/pr/PR'
b = str(input())
c = '.zip'
url = a + b + c
filename = b + c
print(f"")
print(url)
print(f"")
wget.download(url, filename)
print(f"")
print(f"")
print(filename)
