import re 
import html
from pprint import pprint
import json
import sqlite3

filename = "lejobadequat-emplois"

job_title_re = r'("jobCard_title">)(?P<title>.+)(<)'
job_url_rer = r'<a href="(.*?)"'

def extract_vacancies(html_data):
    vacancies = []
    articles = re.split(r'<article', html_data)

    for article in articles:
        if article.strip():  
            title_match = re.search(job_title_re, article)
            url_match = re.search(job_url_rer, article)
            
            if title_match and url_match:
                # html.unescape because French uses weird symbols
                title = html.unescape(title_match.group('title').strip())
                url = url_match.group(1).strip()
                vacancies.append((title, url))
    return vacancies 

def save_json(vacancies):
        data = [
            {'title': title, 'url': url}
            for title, url in vacancies
        ]
        # pprint(data)
        with open(filename + '.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

def save_sqlite(vacancies):
    conn = sqlite3.connect(filename + '.db')
    cursor = conn.cursor()

    sql = """
        create table if not exists vacancies (
            id integer primary key,
            title text,
            url text
        )
    """
    cursor.execute(sql)

    for vacancy in vacancies:
        cursor.execute("""
            insert into vacancies (title, url)
            values (?, ?)
        """, (vacancy[0], vacancy[1]))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    with open(filename + '.html', "r", encoding="utf-8") as file:
        vacancies = extract_vacancies(file.read())

        # for vacancy in vacancies:
        #    print(f"Title: {vacancy[0]}, URL: {vacancy[1]}")

        save_json(vacancies)
        save_sqlite(vacancies)

