import scrapy
from scrapy import cmdline
import os


def parser(html_path):
    html_str = open(html_path).read()
    tds = scrapy.Selector(text=html_str).xpath("//td/text()").extract()
    print(tds)


if __name__ == '__main__':
    html_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                             "html_data", "html1.html")
    print(html_path)
    parser(html_path)
    cmdline.execute()
