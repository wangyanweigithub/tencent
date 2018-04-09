# -*- coding: utf-8 -*-

# Scrapy settings for tecent project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tencent'

SPIDER_MODULES = ['tencent.spiders']
NEWSPIDER_MODULE = 'tencent.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tecent (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tecent.middlewares.TecentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'tecent.middlewares.TecentDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'tecent.pipelines.TecentPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_FILE = "tencent.log"
#LOG_LEVEL = "INFO"

all_citys = [{"北京": "http://db.house.qq.com/index.php?mod=search&city=bj"} ,
        {"上海": "http://db.house.qq.com/index.php?mod=search&city=sh"} ,
        {"重庆": "http://db.house.qq.com/index.php?mod=search&city=cq"} ,
        {"天津": "http://db.house.qq.com/index.php?mod=search&city=tianjin"} ,
        {"广州": "http://db.house.qq.com/index.php?mod=search&city=gz"} ,
        {"深圳": "http://db.house.qq.com/index.php?mod=search&city=sz"} ,
        {"中山": "http://db.house.qq.com/index.php?mod=search&city=zs"} ,
        {"珠海": "http://db.house.qq.com/index.php?mod=search&city=zh"} ,
        {"江门": "http://db.house.qq.com/index.php?mod=search&city=jm"} ,
        {"惠州": "http://db.house.qq.com/index.php?mod=search&city=huizhou"} ,
        {"东莞": "http://db.house.qq.com/index.php?mod=search&city=dg"} ,
        {"佛山": "http://db.house.qq.com/index.php?mod=search&city=fs"} ,
        {"清远": "http://db.house.qq.com/index.php?mod=search&city=qingyuan"} ,
        {"湛江": "http://db.house.qq.com/index.php?mod=search&city=zhanjiang"} ,
        {"阳江": "http://db.house.qq.com/index.php?mod=search&city=yangjiang"} ,
        {"茂名": "http://db.house.qq.com/index.php?mod=search&city=maoming"} ,
        {"肇庆": "http://db.house.qq.com/index.php?mod=search&city=zhaoqing"} ,
        {"汕头": "http://db.house.qq.com/index.php?mod=search&city=shantou"} ,
        {"潮州": "http://db.house.qq.com/index.php?mod=search&city=chaozhou"} ,
        {"汕尾": "http://db.house.qq.com/index.php?mod=search&city=shanwei"} ,
        {"揭阳": "http://db.house.qq.com/index.php?mod=search&city=jieyang"} ,
        {"梅州": "http://db.house.qq.com/index.php?mod=search&city=meizhou"} ,
        {"云浮": "http://db.house.qq.com/index.php?mod=search&city=yunfu"} ,
        {"韶关": "http://db.house.qq.com/index.php?mod=search&city=shaoguan"} ,
        {"成都": "http://db.house.qq.com/index.php?mod=search&city=cd"} ,
        {"南充": "http://db.house.qq.com/index.php?mod=search&city=nanchong"} ,
        {"泸州": "http://db.house.qq.com/index.php?mod=search&city=lz"} ,
        {"绵阳": "http://db.house.qq.com/index.php?mod=search&city=my"} ,
        {"自贡": "http://db.house.qq.com/index.php?mod=search&city=zigong"} ,
        {"内江": "http://db.house.qq.com/index.php?mod=search&city=neijiang"} ,
        {"乐山": "http://db.house.qq.com/index.php?mod=search&city=leshan"} ,
        {"武汉": "http://db.house.qq.com/index.php?mod=search&city=wh"} ,
        {"宜昌": "http://db.house.qq.com/index.php?mod=search&city=yichang"} ,
        {"襄阳": "http://db.house.qq.com/index.php?mod=search&city=xiangyang"} ,
        {"恩施": "http://db.house.qq.com/index.php?mod=search&city=enshi"} ,
        {"黄石": "http://db.house.qq.com/index.php?mod=search&city=huangshi"} ,
        {"黄冈": "http://db.house.qq.com/index.php?mod=search&city=huanggang"} ,
        {"鄂州": "http://db.house.qq.com/index.php?mod=search&city=ezhou"} ,
        {"荆州": "http://db.house.qq.com/index.php?mod=search&city=jingzhou"} ,
        {"十堰": "http://db.house.qq.com/index.php?mod=search&city=shiyan"} ,
        {"荆门": "http://db.house.qq.com/index.php?mod=search&city=jingmen"} ,
        {"仙桃": "http://db.house.qq.com/index.php?mod=search&city=xiantao"} ,
        {"孝感": "http://db.house.qq.com/index.php?mod=search&city=xiaogan"} ,
        {"咸宁": "http://db.house.qq.com/index.php?mod=search&city=xianning"} ,
        {"随州": "http://db.house.qq.com/index.php?mod=search&city=suizhou"} ,
        {"长沙": "http://db.house.qq.com/index.php?mod=search&city=cs"} ,
        {"株洲": "http://db.house.qq.com/index.php?mod=search&city=zhuzhou"} ,
        {"衡阳": "http://db.house.qq.com/index.php?mod=search&city=hengyang"} ,
        {"湘潭": "http://db.house.qq.com/index.php?mod=search&city=xiangtan"} ,
        {"郴州": "http://db.house.qq.com/index.php?mod=search&city=chenzhou"} ,
        {"永州": "http://db.house.qq.com/index.php?mod=search&city=yongzhou"} ,
        {"岳阳": "http://db.house.qq.com/index.php?mod=search&city=yueyang"} ,
        {"常德": "http://db.house.qq.com/index.php?mod=search&city=changde"} ,
        {"益阳": "http://db.house.qq.com/index.php?mod=search&city=yiyang"} ,
        {"邵阳": "http://db.house.qq.com/index.php?mod=search&city=shaoyang"} ,
        {"郑州": "http://db.house.qq.com/index.php?mod=search&city=zz"} ,
        {"驻马店": "http://db.house.qq.com/index.php?mod=search&city=zhumadian"} ,
        {"洛阳": "http://db.house.qq.com/index.php?mod=search&city=luoyang"} ,
        {"南阳": "http://db.house.qq.com/index.php?mod=search&city=nanyang"} ,
        {"许昌": "http://db.house.qq.com/index.php?mod=search&city=xuchang"} ,
        {"开封": "http://db.house.qq.com/index.php?mod=search&city=kaifeng"} ,
        {"平顶山": "http://db.house.qq.com/index.php?mod=search&city=pingdingshan"} ,
        {"漯河": "http://db.house.qq.com/index.php?mod=search&city=luohe"} ,
        {"周口": "http://db.house.qq.com/index.php?mod=search&city=zhoukou"} ,
        {"三门峡": "http://db.house.qq.com/index.php?mod=search&city=sanmenxia"} ,
        {"南京": "http://db.house.qq.com/index.php?mod=search&city=nj"} ,
        {"苏州": "http://db.house.qq.com/index.php?mod=search&city=suzhou"} ,
        {"无锡": "http://db.house.qq.com/index.php?mod=search&city=wuxi"} ,
        {"常州": "http://db.house.qq.com/index.php?mod=search&city=changzhou"} ,
        {"扬州": "http://db.house.qq.com/index.php?mod=search&city=yangzhou"} ,
        {"镇江": "http://db.house.qq.com/index.php?mod=search&city=zhenjiang"} ,
        {"南通": "http://db.house.qq.com/index.php?mod=search&city=nantong"} ,
        {"徐州": "http://db.house.qq.com/index.php?mod=search&city=xuzhou"} ,
        {"盐城": "http://db.house.qq.com/index.php?mod=search&city=yancheng"} ,
        {"淮安": "http://db.house.qq.com/index.php?mod=search&city=huaian"} ,
        {"宿迁": "http://db.house.qq.com/index.php?mod=search&city=suqian"} ,
        {"泰州": "http://db.house.qq.com/index.php?mod=search&city=taizhou"} ,
        {"连云港": "http://db.house.qq.com/index.php?mod=search&city=lianyungang"} ,
        {"石家庄": "http://db.house.qq.com/index.php?mod=search&city=sjz"} ,
        {"唐山": "http://db.house.qq.com/index.php?mod=search&city=tangshan"} ,
        {"承德": "http://db.house.qq.com/index.php?mod=search&city=chengde"} ,
        {"张家口": "http://db.house.qq.com/index.php?mod=search&city=zjk"} ,
        {"大同": "http://db.house.qq.com/index.php?mod=search&city=datong"} ,
        {"朔州": "http://db.house.qq.com/index.php?mod=search&city=shuozhou"} ,
        {"长治": "http://db.house.qq.com/index.php?mod=search&city=changzhi"} ,
        {"临汾": "http://db.house.qq.com/index.php?mod=search&city=linfen"} ,
        {"运城": "http://db.house.qq.com/index.php?mod=search&city=yuncheng"} ,
        {"晋城": "http://db.house.qq.com/index.php?mod=search&city=jincheng"} ,
        {"杭州": "http://db.house.qq.com/index.php?mod=search&city=hz"} ,
        {"绍兴": "http://db.house.qq.com/index.php?mod=search&city=shaoxing"} ,
        {"宁波": "http://db.house.qq.com/index.php?mod=search&city=nb"} ,
        {"台州": "http://db.house.qq.com/index.php?mod=search&city=tz"} ,
        {"金华": "http://db.house.qq.com/index.php?mod=search&city=jinhua"} ,
        {"湖州": "http://db.house.qq.com/index.php?mod=search&city=huzhou"} ,
        {"温州": "http://db.house.qq.com/index.php?mod=search&city=wenzhou"} ,
        {"嘉兴": "http://db.house.qq.com/index.php?mod=search&city=jiaxing"} ,
        {"舟山": "http://db.house.qq.com/index.php?mod=search&city=zhoushan"} ,
        {"丽水": "http://db.house.qq.com/index.php?mod=search&city=ls"} ,
        {"吉林": "http://db.house.qq.com/index.php?mod=search&city=jilin"} ,
        {"大连": "http://db.house.qq.com/index.php?mod=search&city=dl"} ,
        {"沈阳": "http://db.house.qq.com/index.php?mod=search&city=sy"} ,
        {"抚顺": "http://db.house.qq.com/index.php?mod=search&city=fushun"} ,
        {"鞍山": "http://db.house.qq.com/index.php?mod=search&city=anshan"} ,
        {"营口": "http://db.house.qq.com/index.php?mod=search&city=yingkou"} ,
        {"本溪": "http://db.house.qq.com/index.php?mod=search&city=benxi"} ,
        {"铁岭": "http://db.house.qq.com/index.php?mod=search&city=tl"} ,
        {"辽阳": "http://db.house.qq.com/index.php?mod=search&city=ly"} ,
        {"丹东": "http://db.house.qq.com/index.php?mod=search&city=dandong"} ,
        {"盘锦": "http://db.house.qq.com/index.php?mod=search&city=panjin"} ,
        {"锦州": "http://db.house.qq.com/index.php?mod=search&city=jinzhou"} ,
        {"葫芦岛": "http://db.house.qq.com/index.php?mod=search&city=huludao"} ,
        {"朝阳": "http://db.house.qq.com/index.php?mod=search&city=chaoyang"} ,
        {"丽江": "http://db.house.qq.com/index.php?mod=search&city=lijiang"} ,
        {"曲靖": "http://db.house.qq.com/index.php?mod=search&city=qujing"} ,
        {"玉溪": "http://db.house.qq.com/index.php?mod=search&city=yuxi"} ,
        {"保山": "http://db.house.qq.com/index.php?mod=search&city=baoshan"} ,
        {"临沧": "http://db.house.qq.com/index.php?mod=search&city=lincang"} ,
        {"德宏州": "http://db.house.qq.com/index.php?mod=search&city=dehongzhou"} ,
        {"怒江": "http://db.house.qq.com/index.php?mod=search&city=nujiang"} ,
        {"迪庆": "http://db.house.qq.com/index.php?mod=search&city=diqing"} ,
        {"威海": "http://db.house.qq.com/index.php?mod=search&city=weihai"} ,
        {"潍坊": "http://db.house.qq.com/index.php?mod=search&city=weifang"} ,
        {"东营": "http://db.house.qq.com/index.php?mod=search&city=dongying"} ,
        {"德州": "http://db.house.qq.com/index.php?mod=search&city=dezhou"} ,
        {"泰安": "http://db.house.qq.com/index.php?mod=search&city=taian"} ,
        {"菏泽": "http://db.house.qq.com/index.php?mod=search&city=heze"} ,
        {"聊城": "http://db.house.qq.com/index.php?mod=search&city=lc"} ,
        {"淮南": "http://db.house.qq.com/index.php?mod=search&city=huainan"} ,
        {"芜湖": "http://db.house.qq.com/index.php?mod=search&city=wuhu"} ,
        {"阜阳": "http://db.house.qq.com/index.php?mod=search&city=fuyang"} ,
        {"黄山": "http://db.house.qq.com/index.php?mod=search&city=huangshan"} ,
        {"安庆": "http://db.house.qq.com/index.php?mod=search&city=anqing"} ,
        {"蚌埠": "http://db.house.qq.com/index.php?mod=search&city=bengbu"} ,
        {"马鞍山": "http://db.house.qq.com/index.php?mod=search&city=maanshan"} ,
        {"宿州": "http://db.house.qq.com/index.php?mod=search&city=suz"} ,
        {"铜陵": "http://db.house.qq.com/index.php?mod=search&city=tongling"} ,
        {"六安": "http://db.house.qq.com/index.php?mod=search&city=luan"} ,
        {"宣城": "http://db.house.qq.com/index.php?mod=search&city=xuancheng"} ,
        {"淮北": "http://db.house.qq.com/index.php?mod=search&city=huaibei"} ,
        {"亳州": "http://db.house.qq.com/index.php?mod=search&city=bozhou"} ,
        {"滁州": "http://db.house.qq.com/index.php?mod=search&city=chuzhou"} ,
        {"池州": "http://db.house.qq.com/index.php?mod=search&city=chizhou"} ,
        {"吉安": "http://db.house.qq.com/index.php?mod=search&city=jian"} ,
        {"宜春": "http://db.house.qq.com/index.php?mod=search&city=yichun"} ,
        {"赣州": "http://db.house.qq.com/index.php?mod=search&city=ganzhou"} ,
        {"九江": "http://db.house.qq.com/index.php?mod=search&city=jiujiang"} ,
        {"上饶": "http://db.house.qq.com/index.php?mod=search&city=shangrao"} ,
        {"新余": "http://db.house.qq.com/index.php?mod=search&city=xinyu"} ,
        {"景德镇": "http://db.house.qq.com/index.php?mod=search&city=jingdezhen"} ,
        {"抚州": "http://db.house.qq.com/index.php?mod=search&city=fz"} ,
        {"鹰潭": "http://db.house.qq.com/index.php?mod=search&city=yingtan"} ,
        {"西宁": "http://db.house.qq.com/index.php?mod=search&city=xining"} ,
        {"西安": "http://db.house.qq.com/index.php?mod=search&city=xian"} ,
        {"宝鸡": "http://db.house.qq.com/index.php?mod=search&city=baoji"} ,
        {"汉中": "http://db.house.qq.com/index.php?mod=search&city=hanzhong"} ,
        {"咸阳": "http://db.house.qq.com/index.php?mod=search&city=xy"} ,
        {"渭南": "http://db.house.qq.com/index.php?mod=search&city=wn"} ,
        {"福州": "http://db.house.qq.com/index.php?mod=search&city=fuzhou"} ,
        {"厦门": "http://db.house.qq.com/index.php?mod=search&city=xiamen"} ,
        {"泉州": "http://db.house.qq.com/index.php?mod=search&city=quanzhou"} ,
        {"莆田": "http://db.house.qq.com/index.php?mod=search&city=putian"} ,
        {"宁德": "http://db.house.qq.com/index.php?mod=search&city=ningde"} ,
        {"海外地产": "http://db.house.qq.com/index.php?mod=search&city=haiwai"} ,
        {"三亚": "http://db.house.qq.com/index.php?mod=search&city=sanya"}]