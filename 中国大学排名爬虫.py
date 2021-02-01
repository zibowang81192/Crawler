import requests
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    trip='\n '
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            s0=tds[0].text.strip(trip)
            s1=tds[1].text.strip(trip)
            s2=tds[2].text.strip(trip)
            s3=tds[3].text.strip(trip)
            s4=tds[4].text.strip(trip)
            s5=tds[5].text.strip(trip)
            ulist.append([s0,s1,s2,s3,s4,s5])

def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{6}^10}\t{2:{6}^10}\t{3:{6}^10}\t{4:^10}\t{5:^10}"
    print(tplt.format("排名","学校名称","省市","类型","总分","办学层次",chr(12288)))
    for i in range(num):
        u=ulist[i]
        #print(u)
        print(tplt.format(u[0],u[1],u[2],u[3],u[4],u[5],chr(12288)))
    print("Suc "+str(num))

def main():
    uinfo = []
    url = 'https://www.shanghairanking.cn/rankings/bcur/2020'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,100)

main()

