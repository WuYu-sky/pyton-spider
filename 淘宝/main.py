import time
from parsel import Selector
import re
from SeleniumGetCookies import SeleniumGetCookies
from urllib import request
import myTool
import os


class TaoBao:
    def __init__(self, session):
        self.session = session
        
        # 店铺全部商品的列表
        self.list_url = 'https://beihuanjj.tmall.com/i/asynSearch.htm?mid=w-23290845082-0'
        
        # 商品名称
        self.file_name = ''

    def get_html(self, url):
        resp = self.session.get(url)
        return resp
    
    # 下边的逻辑需要根据你想爬取的网站更改
    def get_name(self, commodity_html):
        name = re.findall(r'<meta name="keywords" content="(.*?)"', commodity_html)[0]
        return name
   
    def get_preview_img(self, selector):
        preview_list = selector.css('#J_UlThumb li')
        for index, preview in enumerate(preview_list):
            preview_url = preview.css('img::attr(src)').get()
            preview_url = 'https:' + preview_url.replace('60x60q', '430x430q').replace('https:', '')
            request.urlretrieve(preview_url, self.file_name + '/主图/' + str(index) + '.jpg')

    def get_spec_img(self, selector):
        spec_list = selector.css('ul.tb-img li')
        for spec in spec_list:
            spec_name = spec.css('span::text').get()
            spec_name = myTool.set_file_name(spec_name)
            spec_url = spec.css('a::attr(style)').get()
            spec_url = re.findall(r'background:url\((.*?)\)', spec_url)[0]
            spec_url = 'https:' + spec_url.replace('40x40q', '430x430q').replace('https:', '')
            request.urlretrieve(spec_url, self.file_name + '/规格/' + spec_name + '.jpg')

    def get_big_img(self, commodity_html):
        icoss = re.findall('itemcdn.tmall.com/desc/(.*?)\?var=desc', commodity_html)[0]
        big_url = 'https://itemcdn.tmall.com/desc/' + icoss
        big_html = self.get_html(big_url).text
        big_urls = re.findall('(https://img.alicdn.com.*?)"', big_html)
        for index, big_img in enumerate(big_urls):
            request.urlretrieve(big_img, self.file_name + '/详情/' + str(index) + '.jpg')

    def extract_url(self):
        text = self.get_html(self.list_url).text
        urls = re.findall(r'//detail.tmall.com/item.htm(.*?)\\', text)
        urls = set(urls)
        for url in urls:
            commodity_url = 'https://detail.tmall.com/item.htm' + url
            commodity_html = self.get_html(commodity_url).text
            selector = Selector(text=commodity_html)
            name = self.get_name(commodity_html)
            self.file_name = myTool.set_file_folder(name)
            os.mkdir(self.file_name + '/主图')
            os.mkdir(self.file_name + '/规格')
            os.mkdir(self.file_name + '/详情')
            self.get_preview_img(selector)
            self.get_spec_img(selector)
            self.get_big_img(commodity_html)
            print(self.file_name + '---爬取完毕！')
            time.sleep(10)


if __name__ == '__main__':
    s = SeleniumGetCookies(账号，密码)
    session = s.run()
    t = TaoBao(session)
    t.extract_url()

