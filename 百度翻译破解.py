import requests
import json
if __name__=="__main__":
    post_url='https://fanyi.baidu.com/sug'
    headers={
        'User-Agent':'Mozilla/5.0'
    }
    kw=input('entry a word:')

    data={
        'kw':kw
    }
    response=requests.post(url=post_url,data=data,headers=headers)
    dic_obj=response.json()
    filename=kw+'.json'
    fp =open(filename,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!')
