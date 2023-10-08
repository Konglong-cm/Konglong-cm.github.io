import csv
import urllib.request as req
import numpy as np

url = 'https://edidata.oss-cn-beijing.aliyuncs.com/fyx_chinamoney.csv'

req.urlretrieve(url, "fyx_chinamoney.csv")

with open("fyx_chinamoney.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)

    rows = list(csvreader)

    # 转为ndarray数组
    a = np.asarray(rows)

    # 返回指定形状的新数组
    a.resize((7,80), refcheck=False)

    for aa in a:
        # 过滤后输出
        print(list(filter(lambda x: x != '', aa)))
