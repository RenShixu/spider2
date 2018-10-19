from lxml import etree
import commonmethod
from urllib import request
from bs4 import BeautifulSoup
from pyquery import PyQuery

def parsePage(content):
    '''
    解析数据
    :param content:爬取的数据信息
    :return: 数据列表
    '''

    #xpath解析数据
    # html = etree.HTML(content)
    # items = html.xpath("//tr[@class='item']")
    # for item in items:
    #     print(item)
    #     atp = item.xpath(".//p[@class='pl']/text()")[0].split("/")
    #     price = atp.pop()   #价格
    #     time = atp.pop()    #时间
    #     press = atp.pop()   #出版社
    #     author = ""         #国家作者译者
    #     for v in range(len(atp)):
    #         author += atp[v]
    #
    #     yield {
    #         'title':item.xpath(".//div[@class='pl2']/a/text()")[0].strip(),
    #         'price':price,
    #         'time':time,
    #         'author':author,
    #         'press':press,
    #         'grade':item.xpath(".//span[@class='rating_nums']/text()")[0],
    #         'comment':item.xpath(".//span[@class='inq']/text()")[0],
    #         'imgurl':item.xpath(".//img[@width='90']/@src")[0]
    #     }

    #BeautifulSoup解析
    # soup = BeautifulSoup(content,"lxml")
    # items = soup.find_all(name="tr",attrs={"class":"item"})
    # for item in items:
    #     atp = item.find(name="p",attrs={"class":"pl"}).string.split("/")
    #     price = atp.pop()  # 价格
    #     time = atp.pop()    #时间
    #     press = atp.pop()   #出版社
    #     author = ""         #国家作者译者
    #     for v in range(len(atp)):
    #         author += atp[v]
    #     yield {
    #         'title':item.select("div.pl2 a")[0].get_text().replace(' ','').replace('\n',''),
    #         'price':price,
    #         'time':time,
    #         'author':author,
    #         'press':press,
    #         'grade':item.find(name="span",attrs={"class":"rating_nums"}).string,
    #         'comment':item.select("span.inq")[0].get_text(),
    #         'imgurl':item.find(name="img",attrs={"width":'90'}).attrs["src"]
    #     }

    #pyquery解析
    doc = PyQuery(content)
    items = doc("tr.item")
    for item in items.items():
        atp = item.find("p.pl").text().split("/")
        price = atp.pop()  # 价格
        time = atp.pop()    #时间
        press = atp.pop()   #出版社
        author = ""         #国家作者译者
        for v in range(len(atp)):
            author += atp[v]
        yield {
            'title':item.find("div.pl2 a:eq(0)").text().replace(' ','').replace('\n',''),
            'price':price,
            'time':time,
            'author':author,
            'press':press,
            'grade':item.find("span.rating_nums").text(),
            'comment':item.find("span.inq").text(),
            'imgurl':item.find("img[width='90']").attr("src")
        }
def main(offset):
    '''
    主程序函数
    :return:
    '''
    # 豆瓣读书top250地址
    url = 'https://book.douban.com/top250?start='+ str(offset * 25)

    # 请求头设置
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3452.0 Safari/537.36',
    }

    #爬取数据
    content = commonmethod.spiderdata(url,headers,'GET',None)
    if content != 0:
        i = 0
        for item in parsePage(content):
            i += 1
            print(item)
            commonmethod.savetofile(item, "./result.txt")
            #request.urlretrieve(item.get("imgurl"),"D:/imgs/{}.jpg".format(i))
        print("第{}次数据保存完成".format(offset+1))
    else:
        print("数据抓取失败")
#执行主函数
if __name__ == '__main__':
    for i in range(10):
        main(i)
