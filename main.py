def top_word_in_news_json(file_name):
    import json
    with open(file_name,"r",encoding="utf-8") as news_file:
        json_data = json.load(news_file)
        json_news = json_data["rss"]["channel"]["items"]
        tmp_list = []
        for i in json_news:
            tmp_list.append(i.get("description").split())
        dict_count = {}
        for list in tmp_list:
            for word in list:
                if word not in dict_count:
                    dict_count[word] = 1
                else:
                    dict_count[word] += 1
        tmp_dict = {}
        for key, value in dict_count.items():
            if len(key) < 6:
                continue
            else:
                tmp_dict[key] = value

        sorted_dict = sorted(tmp_dict.items(), key=lambda item: item[1],reverse=True)
        top_word = sorted_dict[0:10]
    print(*top_word)

top_word_in_news_json("newsafr.json")