libraries = [
    {"language": "Java", "name": "Spring"}, 
    {"language": "python", "name": "Django"},
    {"language": "Javascript", "name": "node"},
    {"language": "python", "name": "flask"}
    ]

v = {k: [dic[k] for dic in libraries] for k in libraries[0]}
print(v)

languages = []
items = {}
for dic in libraries:
    if not dic["language"] in languages:
        languages.append(dic["language"])
        items[dic["language"]] = []
    for name in dic["name"]:
        if not dic["name"] in items[dic["language"]]:
            items[dic["language"]].append(dic["name"])
print(items)