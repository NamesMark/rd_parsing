## Link

[https://www.lejobadequat.com/emplois](https://www.lejobadequat.com/emplois)

## Task

У цьому домашньому завданні ви зможете попрактикуватися у написанні парсера за допомогою бібліотеки Selenium.

Ваше завдання — написати парсер, використовуючи Selenium для сайту https://jobs.marksandspencer.com/job-search 

Потрібно для перших 2(!) сторінок зібрати назву і посилання вакансії.

На виході у вас має бути JSON-формат:

```json
[
{
“title”: “Customer Assistant - Foods - Vangarde, York”,
“url”: “https://jobs.marksandspencer.com/job-search/in-store/york-north-yorkshire/customer-assistant-foods-vangarde-york/300003726976573”
},
{...} x 19
]
```

## Solution

- [main.py](main.py)

## Output example

```Got 24 jobs```

```json
[
    {
        "Title": "Ma\u00e7on finisseur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249678-macon-finisseur-h-f-fr"
    },
    {
        "Title": "Cariste CACES 5 H/F",
        "Link": "https://www.lejobadequat.com/emplois/249677-cariste-caces-5-f-h-fr"
    },
    {
        "Title": "Conducteur engins H/F",
        "Link": "https://www.lejobadequat.com/emplois/249676-conducteur-engins-f-h-fr"
    },
    {
        "Title": "Technicien monteur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249673-technicien-monteur-h-f-fr"
    },
    {
        "Title": "Coffreur/bancheur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249672-coffreur-bancheur-f-h-fr"
    },
    {
        "Title": "Conducteur engins H/F",
        "Link": "https://www.lejobadequat.com/emplois/249671-conducteur-engins-f-h-fr"
    },
    {
        "Title": "Agent de quai H/F",
        "Link": "https://www.lejobadequat.com/emplois/249670-agent-de-quai-f-h-fr"
    },
    {
        "Title": "Charpentier H/F",
        "Link": "https://www.lejobadequat.com/emplois/249669-charpentier-f-h-fr"
    },
    {
        "Title": "Agent de nettoyage H/F",
        "Link": "https://www.lejobadequat.com/emplois/249668-agent-de-nettoyage-f-h-fr"
    },
    {
        "Title": "Soudeur tig H/F",
        "Link": "https://www.lejobadequat.com/emplois/249667-soudeur-tig-f-h-fr"
    },
    {
        "Title": "Pr\u00e9parateur de commandes avec scan CACES 1 H/F",
        "Link": "https://www.lejobadequat.com/emplois/249666-preparateur-de-commandes-avec-scan-caces-1-h-f-fr"
    },
    {
        "Title": "Monteur c\u00e2bleur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249665-monteur-cableur-f-h-fr"
    },
    {
        "Title": "Pr\u00e9parateur avec commande vocale CACES 1 H/F",
        "Link": "https://www.lejobadequat.com/emplois/249664-preparateur-avec-commande-vocale-caces-1-f-h-fr"
    },
    {
        "Title": "Conducteur de ligne H/F",
        "Link": "https://www.lejobadequat.com/emplois/249663-conducteur-de-ligne-f-h-fr"
    },
    {
        "Title": "Technicien fibre optique H/F",
        "Link": "https://www.lejobadequat.com/emplois/249662-technicien-fibre-optique-f-h-fr"
    },
    {
        "Title": "Monteur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249661-monteur-h-f-fr"
    },
    {
        "Title": "Agent de conditionnement H/F",
        "Link": "https://www.lejobadequat.com/emplois/249660-agent-de-conditionnement-f-h-fr"
    },
    {
        "Title": "Ensacheur H/F",
        "Link": "https://www.lejobadequat.com/emplois/249659-ensacheur-f-h-fr"
    },
    {
        "Title": "Cariste H/F",
        "Link": "https://www.lejobadequat.com/emplois/249658-cariste-f-h-fr"
    },
    {
        "Title": "Charg\u00e9(e) d\u2019affaire et support technique sav H/F",
        "Link": "https://www.lejobadequat.com/emplois/249657-chargee-daffaire-et-support-technique-sav-h-f-fr"
    },
    {
        "Title": "Conducteur d\u2019engins H/F",
        "Link": "https://www.lejobadequat.com/emplois/249656-conducteur-dengins-f-h-fr"
    },
    {
        "Title": "Magasinier cariste H/F",
        "Link": "https://www.lejobadequat.com/emplois/249654-magasinier-cariste-f-h-fr"
    },
    {
        "Title": "Op\u00e9rateur regleur en usingage h-f",
        "Link": "https://www.lejobadequat.com/emplois/249653-operateur-regleur-en-usingage-h-f-fr"
    },
    {
        "Title": "Op\u00e9rateur de production H/F",
        "Link": "https://www.lejobadequat.com/emplois/249652-operateur-de-production-h-f-fr"
    }
]
```