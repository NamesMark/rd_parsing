## Link

[https://www.lejobadequat.com/emplois](https://www.lejobadequat.com/emplois)

## Task

- За допомогою бібліотеки requests отримати контент першої сторінки
- За допомогою бібліотеки re отримати всі назви вакансій. Скрипт має повертати список, приклад: 

```python
[
    “Menuisier H/F”,
    “Agent entretien des espaces verts H/F”,
    “...”
]
```

## Solution

1. [Getting the page](get_page.py)
2. [Extracting vacancies](get_page.py)

## Output example

```python
['Vendeur  H/F', 'Agent de nettoyage  H/F', 'Chauffeur PL  H/F', 'Assistant administratif  H/F', 'Agent d’exploitation  H/F', 'Employe commercial fruits et legumes  H/F', 'Chaudronnier métallier  H/F', 'Chauffeur spl  H/F', 'Chef d’équipe   H/F', 'Vendeur   H/F', 'Technicien de maintenance –  H/F', 'Préparateur de pièce  H/F']
```