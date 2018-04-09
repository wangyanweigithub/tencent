# -*- coding: utf-8 -*-
import scrapy
import json
import re
import execjs
from pyquery import PyQuery as pq
from tencent.items import CityLink, AreaCode


class DbhouseSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['house.qq.com']
    start_urls = ['http://db.house.qq.com/index.php?mod=search&city=bj']

    def __init__(self, city="北京", area="朝阳"):
        super(DbhouseSpider, self).__init__()
        self.city = city
        self.area = area

    def parse(self, response):
        result = response.xpath("//div[@class='qgcity']/div[@id='tabb']//div[@id='scrollBox']/"
                               "div[@class='scrollContent']/dl")
        all_citys = {}
        for each in result:
            for dd in each.xpath("dd/a"):
                href = dd.xpath("@href").extract()
                city = dd.xpath("text()").extract()
                city_link = dict(zip(city, href))
                all_citys.update(city_link)

        self.all_citys = all_citys
        self.log("!!!!!!!!!!citys is %s" % json.dumps(all_citys, ensure_ascii=False))

        for k, url in all_citys.items():
            city_item = CityLink()
            city_item['city'] = k
            city_item['link'] = url
            yield city_item
            if not self.city:
                yield scrapy.Request(url, callback=self.get_city_areas)

        if self.city:
            yield scrapy.Request(all_citys[self.city], callback=self.get_city_areas)

    def get_city_areas(self, response):
        city_name = response.xpath("//div[@id='cityName']/a/text()").extract()[0]
        area_code_dic = {}
        for area in response.xpath("//ul[@id='search_condition_region1']/li"):
            params = area.xpath("a/@onclick").extract()[0]
            area_num = re.search(r"(\d:\d)", params).group(1)
            area_name = area.xpath("a/text()").extract()[0]
            area_item = AreaCode()
            area_item['city'] = city_name
            area_item['area_name'] = area_name
            area_item['area_code'] = area_num
            yield area_item
            area_code_dic.update({area_name: area_num})

            if not self.area:
                url = "%s&act=newsearch&showtype=1&page_no=1& unit=1&all=&CA=%s" % (self.all_citys[city_name], area_num)
                yield scrapy.Request(url, callback=self.get_area_house)

        if self.area:
            url = "%s&act=newsearch&showtype=1&page_no=1&" \
                  "unit=1&all=&CA=%s" % (self.all_citys[city_name], area_code_dic[self.area])
            print(url)
            yield scrapy.Request(url, callback=self.get_area_house)

    def get_area_house(self, response):
        pass

        # html = response.body.decode('gb18030')
        # pattern1 = r'\s*var\s*search_result\s*=\s*\s*'
        # res1 = re.split(pattern1, html)
        # print(res1)
        # pattern2 = r'\s*;var\s*search_result_list_num\s*=\s*\d*;'
        # res2 = re.split(pattern2, res1[1])
        # print(res2)
        #
        # result = execjs.eval(res2[0])
        # doc = pq(result)
        # # print("doc",doc)
        # link = []
        # links = doc('li.title > h2 > a')
        # # print('links:', links)
        # if links:
        #     for val in links.items():
        #         link.append(val.attr('href'))
        #     print("links", len(link), link)
        #     if link:
        #         for val in link:
        #             print("link:", val)
        #             # yield scrapy.Request(val, callback=self.parse_building)

        # next = doc('#search_result_page a.grey:contains("下一页")')
        # print('next', next)
        # if not next:  # if not next:
        #     print('end2')
        #     self.page_no += 1
        #     request = 'http://db.house.qq.com/index.php?mod=search&act=newsearch&city=' + str(
        #         data['cityen']) + '&showtype=1&page_no=' + str(self.page_no) + '&mod=search&city=' + str(data['cityen'])
        #     print('request', request, self.page_no)
        #     # yield scrapy.Request(request,meta={'data': data}, callback=self.parse_item)


