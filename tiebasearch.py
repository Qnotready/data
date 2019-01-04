import urllib.request
import re
import os


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
        os.mkdir("NewPics")
    except FileExistsError:
        pass
    os.chdir("NewPics")
    for each in imglist:
        print(each)
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each, filename, None)
    os.chdir(os.pardir)


if __name__ == '__main__':
    for i in range(1, 3):
        url = "https://tieba.baidu.com/p/5059180075?pn=%s" % i
        get_img(open_url(url))
    url = "http://tieba.baidu.com/p/5059180075"
    get_img(open_url(url))
