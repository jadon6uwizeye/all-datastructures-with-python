from collections import defaultdict
import math

f = open('/home/jadon6/Documents/all-datastructures-with-python/python_primer/character_index_app/heart_dark.txt', 'rb')
data = f.read()
data = data.decode('utf-8')
data = data.replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!', '').replace(':', '')
data = data.lower()
data_list = data.split()

CHARACTERS = [
    "Kurtz", "manager", "Rusian", "pilgrims", "cannibals", "aunt", "brickmaker", "Accountant", "helsman", "mistress", "intendend"
    ]

def paginate(data, page_length):
    pages = []
    page = []
    data = data.split()
    for i in range(len(data)):
        page.append(data[i])
        if (i+1) % page_length == 0:
            pages.append(page)
            page = []
    if page:
        pages.append(page)
    return pages

    # or we can use this algorithm
    words = data.split()
    page_count = math.ceil(len(words)/ page_length)
    pages = defaultdict(str)
    pointer = 0
    for i in range(page_count + 1):
        pages[i] = words[pointer: pointer + page_length]
        pointer += page_length
    return pages

def get_names(data,characters=CHARACTERS):
    names = defaultdict(list)
    words = data.split()
    for character in characters:
        for word in words:
            if character.lower() in word:
                names[character].append(word)
    return names

# main
names = get_names(data)
print(names)