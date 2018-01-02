#coding=utf-8
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import re
'''
电影名 上映日期 上映场次数 院线城市 导演 演员 影片类型 票房收入
'''

def tList(dateList):
    with open("cc.txt","a") as f:
         for i in dateList:
             f.writelines(`i`.encode("utf-8"))
         f.writelines("\n")

with open("spider.log","r") as f:
    content = f.read();

    content = content.split("\n")
    dateList = []
    for i in content:
        if i.find("票房")!=-1:
            dateList.append(i)

    for i in dateList:
        print i

    resList = []
    patten = re.compile(r".*?,.*?,(.*?);(.*?);.*?;(.*?);(.*?);(.*?);(.*?);(.*?);(.*?);(.*?)")
    for i in dateList:
        res = patten.findall(i)
        for i in res:
            i = list(i)
            resList.append(i)
    print resList
    DF = pd.DataFrame(resList)
    DF.to_csv("333.csv",encoding="utf-8")
