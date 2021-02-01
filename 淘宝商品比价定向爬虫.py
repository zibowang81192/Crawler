import requests
import re
def getHTMLText(url):
    try:
        kv = {   
            'cookie':'your cookie',#copy the cookie from browser
            'user-agent':'Mozilla/5.0'
        }
        r=requests.get(url,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("提取失败")
        return ""

def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        # print(tlt)
        print(len(plt))
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([title, price])
        # print(ilist)
    except:
        print("解析出错")

def printGoodsList(ilt):
    tplt="{0:^4}\t{1:{3}^40}\t{2:^16}"
    #tplt="{0:4}\t{1:8}\t{2:16}"
    print(tplt.format("序号","商品名称","价格",chr(12288)))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1],chr(12288)))

if __name__=="__main__":
    goods='悠悠球'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infolist=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infolist,html)
        except:
            continue
    printGoodsList(infolist)