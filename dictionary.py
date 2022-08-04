# 辞書ファイルを読み込み
dict_file = open("dictionary-data.csv", "r", encoding="UTF-8")
# ファイルから見出し語を取得
dict_data = dict_file.read()
print(dict_data)
dict_file.close()
