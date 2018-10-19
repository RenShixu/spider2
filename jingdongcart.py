from pyquery import PyQuery
import commonmethod

def parapages(content):
    '''
    解析数据
    :return:
    '''
    doc = PyQuery(content)
    items = doc("div.item-selected.item-item")
    for item in items.items():
        yield {
            "itemname":item.find("div.p-name a[clstag]:eq(0)").text(),
            "price":item.find("p.plus-switch strong").text(),
            "number":item.find("div.quantity-form input").attr("value")
        }

def main(offset):
    '''
    主程序
    :param offset:
    :return:
    '''
    url = "https://cart.jd.com/cart.action"
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                     'Chrome/69.0.3452.0 Safari/537.36',
        "cookie":"user-key=66c93397-5192-4de8-94e3-f70a343169a5; "
                 "shshshfpa=e6315bdf-39ce-ce9f-217f-beac5870695f-1539780330; "
                 "shshshfpb=148d135418b9b441d827602147582e95134cd7365324c102f5bc72eeef; __"
                 "jda=122270672.1539780333070667237888.1539780333.1539780333.1539780333.1; __"
                 "jdc=122270672; __jdv=122270672|direct|-|none|-|1539780333071; __"
                 "jdu=1539780333070667237888; PCSYCityID=1213; ipLoc-djd=1-72-4137-0; areaId=1; _"
                 "gcl_au=1.1.970560060.1539780344; 3AB9D23F7A4B3C9B=QOVUIF3LIZDVD4PBDBEEH2UOVACGERAZU5GKIQIU3CSUSGD747MD7FZ2S7R5U3CKY2PNNOMSWPWKDHEED7WKHKUI4I; "
                 "cart-main=xx; cn=5; cd=0; shshshfp=793773fff05a7ee099b"
                 "0d093c9bc0970; shshshsID=312126761a5a4a7ca25ad352d5e41b4c_5_1539780387592; __j"
                 "db=122270672.7.1539780333070667237888|1.1539780333",
    }
    content = commonmethod.spiderdata(url,headers,"GET",None)

    for item in parapages(content):
        print(item)

if __name__ == '__main__':
    main(0)