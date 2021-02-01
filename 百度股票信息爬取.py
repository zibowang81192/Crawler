import re
import requests
import traceback
from bs4 import BeautifulSoup
def getHTMLText(url,code='utf-8'):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=code
        return r.text
    except:
        return ""
def getStockList(list,stockurl):
    html=getHTMLText(stockurl)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('tr')
    for i in a:
        try:
            href=i.attrs['id']
            list.append(re.findall(r'^tr\d{6}',href)[0])
            #print(list)
        except:
            continue
    

def getStockInfo(list,stockurl,fpath):
    count=0
    for stock in list:
        url=stockurl+stock[2:]+".html"
        html=getHTMLText(url)
        try:
            if html=='':
                continue
            infodict={}
            soup=BeautifulSoup(html,'html.parser')
            stockinfo=soup.find('div',attrs={'class':'merchandiseDetail'})

            name=stockinfo.find_all(attrs={'class':'fundDetail-tit'})[0]
            infodict.update({'股票名称':name.text.split()[0]})
            
            keylist=stockinfo.find_all('dt')
            valuelist=stockinfo.find_all('dd')
            for i in range(len(keylist)):
                key=keylist[i].text
                val=valuelist[i].text
                infodict[key]=val
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infodict)+'\n')
                count=count+1
                print('\r当前速度：{:.2f}%'.format(count*100/len(list)),end='')

        except:
            count = count + 1
            print('\r当前速度：{:.2f}%'.format(count * 100 / len(list)), end='')
            traceback.print_exc()
            continue

if __name__=="__main__":
    stock_list_url="https://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1"
    stock_info_url="https://fund.eastmoney.com/"
    output_file="D://BaiduStockInfo.txt"
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)

