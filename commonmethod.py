#通用方法
import requests
from requests.exceptions import RequestException
import json
def savetofile(content,filepath):
    '''
    保存信息到文本
    :param content:
    :return:
    '''
    with open(filepath,"a",encoding="utf-8") as file:
        file.write(json.dumps(content,ensure_ascii=False)+"\n")

def spiderdata(url,headers,method,data):
    '''
    爬取数据
    :param url: 请求地址
    :param headers: header头信息
    :param method: 请求方法
    :param data: postq请求数据
    :return: 爬取的页面信息
    '''
    try:
        #get请求
        if method == 'GET':
            res = requests.get(url,headers=headers)
            if res.status_code == 200:
                return res.text
        #post请求
        else:
            res = requests.post(url,data=data,headers=headers)
            if res.status_code == 200:
                return res.text
    except RequestException as rep:
        print(rep)
        return 0
    except Exception as err:
        print(err)
        return 0

