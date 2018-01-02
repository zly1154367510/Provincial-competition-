#coding=utf-8
import pandas as pd
import datetime
import sys
reload(sys)
sys.setdefaultencoding("GB18030")
import matplotlib.pyplot as mp

mp.rcParams['font.sans-serif'] = ['FangSong']

A = "《冲上云霄》"
B = "《百团大战》"
C = "《简单爱》"
M = "武汉"
N = "北京"


def clearCSV(name):
    content = "";
    with open(name,"r") as f:
        content = f.read();

    content = content.replace("，","-")

    content = content.replace(";",",")

    content = content.replace(".", "-")

    dataList = content.split("\n")

    clearList = []

    for i in dataList:
        i = i.split(",")
        clearList.append(i)

    df = pd.DataFrame(clearList)

    return df
def clearCSV1(name):
    content = "";
    with open(name,"r") as f:
        content = f.read();

    content = content.replace("，","-")

    content = content.replace(";",",")


    dataList = content.split("\n")

    clearList = []

    for i in dataList:
        i = i.split(",")
        clearList.append(i)

    df = pd.DataFrame(clearList)

    return df

# df.to_csv("222.csv")
def getDayNum(movieName,df):
    AStartTime = df[df[0]==movieName][1].values[0].split("-")
    AEndTime = df[df[0]==movieName][2].values[0].split("-")
    AdayNum = (datetime.datetime(int(AEndTime[0]),int(AEndTime[1]),int(AEndTime[2]))-datetime.datetime(int(AStartTime[0]),int(AStartTime[1]),int(AStartTime[2]))).days
    return AdayNum

def getAverage(Aname,df,dayNum):
    dataList = list(df[df[0]==A][7])
    clearList = []
    he = 0
    for i in dataList:
        i = float(i.replace("票房（万）",""))
        he += i
    print round(he/dayNum,6)

def getWeekNum(num):
    if num%7 != 0:
        return num/7+1
    else:
        return num/7

def getPlot(df):
    ADayNum = getDayNum(A,df)
    BDayNum = getDayNum(B,df)
    CDayNum = getDayNum(C,df)
    '''ABC上映周数'''
    AweekNum = getWeekNum(ADayNum)
    BweekNum = getWeekNum(BDayNum)
    CweekNum = getWeekNum(CDayNum)
    '''ABC周票房'''

def clearCityData(data):
    '''
    按电影名去重
    '''
    data = data.drop_duplicates([0])
    '''
    按月分组
    '''
    dataList = []
    yuefenzongList = []
    cc = data[data[1] >= datetime.datetime(2015, 1, 1)]
    cc = cc[cc[1] < datetime.datetime(2015, 2, 1)]
    dataList.append(cc)
    bb = data[data[1] >= datetime.datetime(2015, 2, 1)]
    bb = bb[bb[1] < datetime.datetime(2015, 3, 1)]
    dataList.append(bb)
    aa = data[data[1] >= datetime.datetime(2015, 3, 1)]
    aa = aa[aa[1] < datetime.datetime(2015, 4, 1)]
    dataList.append(aa)
    he = 0
    for j in range(0,3):
        for i in dataList[j][7]:
            i = float(i.replace("票房（万）", ""))
            he += i
        yuefenzongList.append(he)
        he = 0
    return yuefenzongList
    # for i in dataList[0][7]:
    #     i = float(i.replace("票房（万）",""))
    #     he += i
    #
    # for i in dataList[1][7]:
    #     i = float(i.replace("票房（万）",""))
    #     he += i
    # for i in dataList[2][7]:
    #     i = float(i.replace("票房（万）", ""))
    #     he += i

def getCity(df):
    df[1] = pd.to_datetime(df[1])
    df = df[df[1]>datetime.datetime(2015,1,1)]
    finalDf =  df[df[1]<datetime.datetime(2015,4,1)]
    MData = finalDf[finalDf[8]==M]
    NData = finalDf[finalDf[8]==N]
    Ndata = clearCityData(NData)
    Mdata = clearCityData(MData)
    xList = [1,2,3]
    mp.subplot(2,2,1)
    mp.plot(xList,Ndata)
    mp.title("北京 title")
    mp.subplot(2,2,2)
    mp.plot(xList,Mdata)
    mp.title("武汉 title")
    return mp

if __name__ == '__main__':
    #票房处理df
    df1 = clearCSV1("film_log3.csv")
    '''
    处理A电影
    ADayNum 上映天数
    Aaverage 日均票房
    '''

    #Aaverage = getAverage(A,df,ADayNum)

    getCity(df1).show()




