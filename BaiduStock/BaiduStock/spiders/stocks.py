import scrapy
import re


class StocksSpider(scrapy.Spider):
    name = 'stocks'
    #allowed_domains = ['baidu.com']
    start_urls = ['https://fund.eastmoney.com/fund.html#os_0;isall_0;ft_;pt_1']

    def parse(self, response):
        for tr in response.css('tr::attr(id)').extract():
            try:
                stock=re.findall(r'^tr\d{6}',tr)[0]
                url="https://fund.eastmoney.com/"+stock[2:]+".html"
                yield scrapy.Request(url,callback=self.parse_stock)
            except:
                continue

    def parse_stock(self,response):
        infoDict={}
        key=''
        val=''
        k=[]
        v=[]
        stockinfo=response.css('.merchandiseDetail')
        name=stockinfo.css('.fundDetail-tit').extract()[0]
        infoDict.update({'股票名称':re.findall('\>.*?\<',name)[1][1:-1]+re.findall('\>.*?\<',name)[4][1:-1]})
        keylist=stockinfo.css('dt').extract()
        valuelist=stockinfo.css('dd').extract()
        for i in range(len(keylist)): 
            k=re.findall('\>.*?\<',keylist[i])
            v=re.findall('\>.*?\<',valuelist[i])
            for j in k:
                key=key+j[1:-1]
            for j in v:
                val=val+j[1:-1]
            
            infoDict[key]=val
        '''
        for i in range(len(keylist)):   
            key=keylist[i]
            val=valuelist[i]
            infoDict[key]=val
        '''
        yield infoDict
        



