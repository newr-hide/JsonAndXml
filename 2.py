import xml.etree.ElementTree as ET
#def read_xml(file_path, word_max_len=6, top_words_amt=10):
tree = ET.parse("newsafr.xml")
root = tree.getroot()
list_news = root.findall("channel/item")
for row in list_news:
    description = row.find("description")
    tmp_list = description.text.split()
dict_count = {}

for word in tmp_list:
    if word not in dict_count:
        dict_count[word] = 1
    else:
        dict_count[word] += 1
tmp_dict = {}
for key, value in dict_count.items():
    if len(key) <= 6:
        continue
    else:
        tmp_dict[key] = value

sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)
print(sorted_dict)
list_word = []
for i in sorted_dict:
    list_word.append(i[0])
top_word = list_word[0:10]

print(top_word)


#read_xml("newsafr.xml")