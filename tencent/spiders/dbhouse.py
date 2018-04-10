# -*- coding: utf-8 -*-
import scrapy
from tencent import settings
import re
import execjs
from scrapy.selector import Selector


class DbhouseSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['house.qq.com']
    start_urls = ['http://db.house.qq.com/index.php?mod=search&city=bj']

    def __init__(self, city=None, area=None):
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

        for k, url in all_citys.items():
            if not self.city:
                yield scrapy.Request(url, callback=self.get_city_areas)

        if self.city:
            yield scrapy.Request(all_citys[self.city], callback=self.get_city_areas)

    def get_city_areas(self, response):
        city_name = response.xpath("//div[@id='cityName']/a/text()").extract()[0]
        area_code_dic = {}
        for area in response.xpath("//ul[@id='search_condition_region1']/li"):
            params = area.xpath("a/@onclick").extract()[0]
            area_num = re.search(r"(\d*:\d*)", params).group(1)
            area_name = area.xpath("a/text()").extract()[0]
            city_area[city_name].append(area_name)

            # area_item = AreaCode()
            # area_item['city'] = city_name
            # area_item['area_name'] = area_name
            # area_item['area_code'] = area_num
            # yield area_item
            area_code_dic.update({area_name: area_num})
            if not self.area:
                url = "%s&act=newsearch&showtype=1&page_no=1& unit=1&all=&CA=%s" % (self.all_citys[city_name], area_num)
                yield scrapy.Request(url, callback=self.get_area_house)
        self.log("city_area is : %s" % city_area)
        if self.area:
            url = "%s&act=newsearch&showtype=1&page_no=1&" \
                  "unit=1&all=&CA=%s" % (self.all_citys[city_name], area_code_dic[self.area])
            yield scrapy.Request(url, callback=self.get_area_house)

    def get_area_house(self, response):
        pass
        # try:
        #     body = response.body.decode("utf8")
        #     groups = re.search("\s*var search_result = \s*(.*);var search_result_list_num\s*=\s*\d", body)
        #     body = execjs.eval(groups[1])
        #     # with open("a.html", 'w', encoding="utf-8") as f:
        #     #     f.write(body)
        #     body = Selector(text=body)
        #     for each in body.xpath("//li[@class='title']/h2"):
        #         url = each.xpath("a/@href").extract()[0]
        #         yield scrapy.Request(url, callback=self.parse_building)
        #
        #     for each in body.xpath("//div[@id='search_result_page']/a[@onclick]"):
        #         if each.xpath("text()").extract()[0] == "下一页>":
        #             search_result = re.search(r".*\(.*,.*,.*,(\d*)\)", each.xpath("@onclick").extract()[0])
        #             page_no = search_result.group(1)
        #             url = re.sub("page_no=\d*", "page_no=%s" % page_no, response.url, 1)
        #             yield scrapy.Request(url, callback=self.get_area_house)
        # except Exception as e:
        #     self.log("!!!!!error %s" % e)

    def parse_building(self, response):
        pass
