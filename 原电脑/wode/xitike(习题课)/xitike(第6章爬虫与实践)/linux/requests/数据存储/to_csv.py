"""
CSV(Comma-Separated Value) 逗号分隔符
CSV 文件是由任意的数据记录组成, 记录间以某种换行符分割, 每行记录由换行符组合
ID, UserName, Age, Country
1001, dana, 18, China
1002, huanglaoban, 28, China
"""
import csv

headers = ["ID", "UserName", "Age", "Country"]
rows = [
    (1001, "liudana", 18, "Beijing"),
    (1002, "huanglaoban", 28, "Chengdu"),
    (1003, "yitengjun", "Nan", "Jinan")
]

with open("test.csv", "w", newline="")as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
