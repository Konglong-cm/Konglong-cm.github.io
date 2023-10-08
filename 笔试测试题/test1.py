import requests
import json
import csv

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

# 英文版
# url = "https://iftp.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoListEN"
# 中文版
url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bond-md/BondMarketInfoList2"

# 所有数据列表
items = []

for page in range(1,7):
    data = {
        'pageNo': page,
        'pageSize': 15,
        'bondType': 100001,
        'issueYear': 2023,
    }

    resp = requests.post(url=url, headers=headers, data=data)

    content = resp.text

    resultList = json.loads(content)['data']['resultList']

    for res in resultList:
        bondName = res['bondName']
        bondCode = res['bondCode']
        entyFullName = res['entyFullName']
        bondType = res['bondType']
        issueStartDate = res['issueStartDate']
        debtRtng = res['debtRtng']
        item = [bondName, bondCode, entyFullName, bondType, issueStartDate, debtRtng]
        # 添加一条数据
        items.append(item)

with open('data.csv', 'w', encoding='GB2312',newline="") as file:
    header = ['债券简称','债券代码','发行人/受托机构','债券类型','发行日期','最新债项评级']
    writer = csv.writer(file)
    # 写入一行
    writer.writerow(header)
    # 写入多行
    writer.writerows(items)