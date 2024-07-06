import re 
import html

filename = "lejobadequat-emplois.html"

r = r'("jobCard_title">)(?P<title>.+)(<)'

vacancies = []

with open(filename, "r", encoding="utf-8") as f:
    m = re.finditer(r, f.read())
    for match in m:
        title = match.group('title')
        vacancies.append(html.unescape(title))

print(vacancies)