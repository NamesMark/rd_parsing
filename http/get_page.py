import requests

url = 'https://www.lejobadequat.com/emplois'

response = requests.get(url)

filename = "lejobadequat-emplois.html"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)