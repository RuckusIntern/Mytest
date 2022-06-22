import requests
u = 'https://www.google.com/search?q=Ruckus&oq=Ruckus'
result = requests.get(u)
print(result.text)
