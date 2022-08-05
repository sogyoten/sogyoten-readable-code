dict_file = open("dictionary-data.csv", "r", encoding="UTF-8")
dict_line = dict_file.read()
word_list = dict_line.split(",")
id = 0
for word in word_list:
    id += 1
    print(f"{id}:{word}")
dict_file.close()
