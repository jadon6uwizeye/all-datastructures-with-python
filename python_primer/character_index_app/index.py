from collections import defaultdict
import math

f = open('/home/jadon6/Documents/all-datastructures-with-python/python_primer/character_index_app/heart_dark.txt', 'rb')
data = f.read()
data = data.decode('utf-8')
data = data.replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!', '').replace(':', '')
data = data.lower()
data_list = data.split()

CHARACTERS = [
    "Kurtz", 
    "manager", 
     "Rusian", 
     "pilgrims",
       "cannibals", "aunt", "brickmaker", "Accountant", "helsman", "mistress", "intendend"
    ]

def paginate(data, page_length):
    # pages = []
    # page = []
    # data = data.split()
    # for i in range(len(data)):
    #     page.append(data[i])
    #     if (i+1) % page_length == 0:
    #         pages.append(page)
    #         page = []
    # if page:
    #     pages.append(page)
    # return pages

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
    '''
    This function takes a string of text and a list of characters and returns a dictionary of characters and their names
    '''
    names = defaultdict(list)
    words = data.split()
    for character in characters:
        for word in words:
            if character.lower() in word:
                names[character].append(word)
    return names

def make_index(names,pages):
    '''
    This function takes a dictionary of characters and their names and a list of pages and returns a dictionary of characters and their index
    '''
    index = defaultdict(list)
    for character, names in names.items():
        for name in names:
            for page_number, page in pages.items():
                if name in page:
                    index[character].append(page_number)
    return index

def print_index(index):
    for name, pages in sorted(index.items()):
        print("{:20}".format(name), end="", flush=True)
        for page in pages:
            print(f", {page}", end="", flush=True)
        print()


print_index(make_index(names=get_names(data),pages=paginate(data,10000)))