## Link

[https://www.bbc.com/sport](https://www.bbc.com/sport)

## Task

У цьому домашньому завданні ви зможете попрактикуватися у написанні парсера за допомогою бібліотеки Beautiful Soup.

Для цього напишіть парсер, використовуючи Beautiful Soup для сайту https://www.bbc.com/sport. Вам необхідно для перших 5(!) новин зібрати Related Topics.


На виході у вас має бути JSON-формат:

```
[
    {
        “Link”: “https://www.bbc.com/sport/tennis/articles/c4nnw5ydlnjo”,
        “Topics”: [“Tennis”]
    },
    {...} x 4
]
```

## Solution

- [main.py](main.py)

## Output

```json
[
    {
        "Link": "https://www.bbc.com/sport/tennis/articles/cjjwz66n6n1o",
        "Topics": [
            "Tennis"
        ]
    },
    {
        "Link": "https://www.bbc.com/sport/swimming/articles/cw5yp32pdg6o",
        "Topics": [
            "Swimming",
            "Paris 2024 Olympics"
        ]
    },
    {
        "Link": "https://www.bbc.com/sport/football/articles/czq6edq65v6o",
        "Topics": [
            "Marseille",
            "Premier League",
            "French Ligue 1",
            "Tottenham Hotspur",
            "Football"
        ]
    },
    {
        "Link": "https://www.bbc.com/sport/cycling/articles/c978qlm1lemo",
        "Topics": [
            "Cycling"
        ]
    },
    {
        "Link": "https://www.bbc.com/sport/football/articles/cv2g3np5p9do",
        "Topics": [
            "Liverpool",
            "Premier League",
            "Football"
        ]
    }
]
```
