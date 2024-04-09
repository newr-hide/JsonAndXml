import xml.etree.ElementTree as ET
def read_xml(file_path, word_max_len=6, top_words_amt=10):
    tree = ET.parse(file_path)
    root = tree.getroot()
    list_news = root.findall("channel/item")
    tmp_list = []
    for row in list_news:
        description = row.find("description")
        tmp_var = description.text.split()
        tmp_list.append(tmp_var)
    dict_count = {}
    for list in tmp_list:
        for word in list:
            if word not in dict_count:
                dict_count[word] = 1
            else:
                dict_count[word] += 1
    tmp_dict = {}
    for key, value in dict_count.items():
        if len(key) <= word_max_len:
            continue
        else:
            tmp_dict[key] = value
    sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1], reverse=True)
    list_word = []
    for i in sorted_dict:
        list_word.append(i[0])
    top_word = list_word[0:top_words_amt]

    return top_word

read_xml("newsafr.xml")
