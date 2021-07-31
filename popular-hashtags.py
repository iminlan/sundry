from collections import Counter
import re

hashes = []                                   # все хештеги
most_hash = []                                # самые популярные хештеги
dictionary = {}                               # словарь из 10 самых популярных хештегов и соответствующих им 5ти самых распространенных значимых слов

### Функция собирает все слова для заданного хештега (из разных твитов)

def all_words(tag):
    words = []                                # массив для сбора слов
    with open('in.txt', 'r', encoding="utf-8-sig") as u:
        for tweet in u:
            mass = tweet.casefold().split()
            for sl in mass:                   # ищем твит с нашим тегом и берём из него все последовательности без решёток
                if (tag in mass and not '#' in sl):
                    ww = re.findall(r'[a-яА-Яa-zA-ZёЁ]\D+', sl)   # из каждой последовательности символов выделяем слова
                    words += ww
    return (words)

### Функция выбирает num наиболее популярных значений (из заданного массива)

def repeated(mas, num):
    common = []
    freq = Counter(mas).most_common(num)      # самые используемые значения + их частота (в порядке убывания)
    for i in freq:                            # оставляем только значения
        common.append(i[0])
    return common

### Поиск десяти самых популярных хештегов

with open('in.txt', 'r', encoding="utf-8-sig") as u:
    for line in u:
        text = line.casefold().split()        # значения хештегов регистронезависимы, поэтому уравниваем регистр для упрощения поиска
        for ind, sl in enumerate(text):       # Извлекаем хештеги
            if '#' in sl:                     # если хештег входит в слово - забираем только то, что после '#'
                text[ind] = sl[sl.index('#') : None]
                hashes.append(text[ind])

most_hash = repeated(hashes, 10)               # массив из 10ти популярных хештегов
print(most_hash)

### Формирование словаря из 10 самых популярных хештегов и соответствующих им 5 самым популярным словам

for most in most_hash:                        # перебираем список популярых хештегов
    most_words = []                           # массив для популярных слов
    words = all_words(most)                   # собраем все слова для одного популярного хештега (из разных твитов)
    most_words = repeated(words, 5)           # ищем 5 самых популярных слов
    dictionary[most] = most_words             # заполняем словарь популярными тегами и их частыми словами

print (dictionary)
