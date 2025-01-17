### 1. Почнімо з дат:
01/02/2021, 12-25-2020, 2021.03.15, 2022/04/30, 2023.06.20 та 2021.07.04 

#### 1.1. Перші 2:

```js
(?<day>\d{2})[\/\.\-](?<month>\d{2})[\/\.\-](?<year>\d{4})
```

#### 1.2. Останні 4:
```js
(?<year>\d{4})[\/\.\-](?<month>\d{2})[\/\.\-](?<day>\d{2})
```

### 2. Також ви можете спробувати знайти дати зі словами: 
March 14, 2022, and December 25, 2020 

```js
(?<month>January|February|March|April|May|June|July|August|September|October|November|December)\s(?<day>\d{2})(,\s)(?<year>\d{4})
```

### 3. Тепер перейдемо до телефонних номерів:
(123) 456-7890, +1-800-555-1234, 800.555.1234, 800-555-1234 та 123.456.7890 

```js
\+?\d?\-?\(?(\d{3})\)?[\s\-\.]?(\d{3})[\s\-\.]?(\d{4})
```

### 4. Інші формати номерів:
+44 20 7946 0958, +91 98765 43210

```js
\+?(\d{2})\s?(\d{2})\s?(\d{3})\s?(\d)\s?(\d)?(\d{4})
```

### 5. Ось кілька електронних адрес для пошуку:
john.doe@example.com, jane_doe123@domain.org, support@service.net, info@company.co.uk та contact.us@my-website.com 

### 6. Трішки складніший формат електронних адресів:
weird.address+spam@gmail.com, "quotes.included@funny.domain" та this.one.with.periods@weird.co.in

#### На 5 + 6:
```js
(?<name>[a-zA-Z0-9\.\_]+)(?<ignore>\+[a-zA-Z0-9]*)?@(?<domain>[a-zA-Z0-9\-]+\.[a-zA-Z0-9\.\-]+)
```

### 7. Наступний крок - пошук URL-адрес:
http://example.com, https://secure.website.org, http://sub.domain.co, www.redirect.com, та ftp://ftp.downloads.com 

```js
((?<protocol>[a-z]+)(:\/\/)|(www\.))(?<domain>[a-zA-Z0-9\.]+)
```

### 8. Також не забудьте про “path” та “param”:
https://my.site.com/path/to/resource?param1=value1&param2=value2, http://www.files.net/files.zip, https://example.co.in/api/v1/resource та https://another-site.org/downloads?query=search#anchor

```js
((?<protocol>[a-z]+)(:\/\/)|(www\.))(?<domain>[a-zA-Z0-9\.\-]+)\/?(?<path>[a-zA-Z0-9\/\.]+)(\?(([a-zA-Z0-9]*=)(?<param>[a-zA-Z0-9]*)&?)+)?#?(?<anchor>[a-zA-Z0-9]*)?
```
 
### 9. Шістнадцяткові числа з'являються в різних контекстах:
0x1A3F, 0xBEEF, 0xDEADBEEF, 0x123456789ABCDEF, 0xA1B2C3 та 0x0

```js
0x[0-9A-F]+
```

### 10. Також попрактикуйте такий формат: 
#FF5733, #C70039, #900C3F, #581845, #DAF7A6 та #FFC300

```js
#(?<rgb>[0-9A-F]{2}){3}
```

### 11. Коди кольорів RGB: 
rgb(255, 99, 71), rgba(255, 99, 71, 0.5)

```js
rgba?\((?<red>\d+)\D*?(?<green>\d+)\D*?(?<blue>\d+)\D*?(?<alpha>0.\d+)?\)
```

### 12. Номери соціального страхування:
123-45-6789, 987-65-4321, 111-22-3333, 555-66-7777 та  999-88-7777
 
### 13. Також номери соціального страхування можуть бути записані ще в такому форматі:
123 45 6789 або 123456789

#### На 12 та 13:
```js
\d{3}\D?\d{2}\D?\d{4}
```

### 14. Пошукайте кілька випадкових речень для порівняння:
The quick brown fox jumps over the lazy dog.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Jack and Jill went up the hill to fetch a pail of water.
She sells seashells by the seashore.

```js
(\w+.?\s?)+\.
```

### 15. І на завершення, давайте додамо деякі спеціальні символи та цифри:
1234567890, !@#$%^&*()_+-=[]{}|;':",./<>?, 3.14159, 42 та -273.15

#### Числа:
```js
(?<any_number>\-?\d+\.?\d+)
```

#### Спецсимволи:
Можна зметчити ось так: `\D+`

Але якщо необхідно кожен окремо, то:

```js
!@#\$%\^&\*\(\)_\+\-=\[\]\{\}\|;':",\.\/<>\?,
```