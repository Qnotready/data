import urllib.request
import re
import os
#from bs4 import BeautifulSoup as bsp

def display():
    print("-" * 30)
    print("      贴吧表情包爬取    V999   ")
    print("1.输入爬取的页数")
    print("2.退出系统")
    print("-" * 30)


def getchoice():
    selectkey = input("请选择序列号：\n")
    return selectkey


def key_in():
    ye_start = int(input("请输入需要爬取的起始页："))
    ye_end = int(input("请输入需要爬取的终止页："))
    return ye_start, ye_end


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header(
        'User-Agent',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.59 Safari/537.36 115Browser/8.4.0')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html


def get_img(html):
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)"'
    imglist = re.findall(p, html)
    try:
        os.mkdir("BiaoqingbaoPics")
    except FileExistsError:
        pass
    os.chdir("BiaoqingbaoPics")
    for each in imglist:
        print(each)
        print("表情包爬取中。。。。。")
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)
    os.chdir(os.pardir)


a = []


def main():
    while True:
        display()
        key_Id = getchoice()
        try:
            key = int(key_Id)
            if key == 1:
                a = key_in()
                for i in range(a[0], a[1]+1):
                    url = "https://tieba.baidu.com/p/5668053051?pn=%s" % i
                    get_img(open_url(url))
                    print("表情包爬取完成！！！")
                # url = "http://tieba.baidu.com/p/5668053051"
                # get_img(open_url(url))
            elif key == 2:
                break
        except:
            print("请重新输入数字选项!")


if __name__ == '__main__':
    main()
