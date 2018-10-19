import requests
from urllib.parse import urlencode
import re,os
from urllib.request import urlretrieve

def paradata(content):
    '''
    解析数据
    :param json:
    :return:
    '''
    pat1 = '{.*?"thumbURL":"(.*?)".*?replaceUrl.*?}'
    pat2 = '{.*?"thumbURL":"(.*?)",.*?adType.*?}'
    data1 = re.findall(pat1,content,re.S)
    data2 = re.findall(pat2,content,re.S)
    imgs = data1 + data2
    imgs.pop()#去除无效
    imgs = list(set(imgs))#去重
    if imgs:
       return imgs



def getdata(url,param,headers):
    '''
    获取数据
    :return:
    '''
    try:
        res = requests.get(url + urlencode(param), headers=headers)
        if res.status_code == 200:
            return res.text
    except Exception as err:
        print(err)




def main():
    '''
    主程序
    :return:
    '''
    url = "https://image.baidu.com/search/index?"
    param = {
        'tn': 'baiduimage',
        'ipn': 'r',
        'ct': '201326592',
        'cl': '2',
        'lm': '-1',
        'st': '-1',
        'fm': 'result',
        'fr':'',
        'sf': '1',
        'fmq': '1539860070044_R',
        'pv':'',
        'ic': '0',
        'nc': '1',
        'z':'',
        'se': '1',
        'showtab': '0',
        'fb': '0',
        'width':'',
        'height':'',
        'face': '0',
        'istype': '2',
        'ie': 'utf-8',
        'ctd': '1539860070044^00_1519X259',
        'word': '西藏'
    }

    headers = {
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                     "Chrome/69.0.3452.0 Safari/537.36",
    }
    content = getdata(url,param,headers)

    imgs = paradata(content)
    if imgs:
        i = 0
        imgdir = "D:/im"
        if not os.path.isdir(imgdir):
            os.mkdir(imgdir)
        for img in imgs:
            print(img)
            i += 1
            urlretrieve(img,imgdir+"/{}.jpg".format(i))



'''调用主程序'''
if __name__ == "__main__":
    main()