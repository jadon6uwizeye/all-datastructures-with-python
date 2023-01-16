from collections import Counter

# open file sample.txt
f = open('/home/jadon6/Documents/all-datastructures-with-python/python_primer/sample.txt','r')

# read the file
data = f.read()
# clean data by removing unnecessary panctuations
data = data.replace(',', '').replace('.', '').replace(';', '').replace('?', '').replace('!', '').replace(':', '')
# convert data to list
data_list = data.lower().split()
# create a counter
counter = Counter(data_list)
print(counter)
# print the most common words
print(counter.most_common(5))