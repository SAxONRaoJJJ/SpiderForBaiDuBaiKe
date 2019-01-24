# coding=utf-8

from iURLManager import URLManager
from iHTMLDownloader import HTMLDownloader
from iHTMLParser import HTMLParser


# import iURLManager
# import iHTMLDownloader
# import iHTMLParser

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownloader()
        self.parser = HTMLParser()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.get_old_urls_size()<100):
                new_url = self.manager.get_new_url()
                html = self.downloader.downloadUrl(new_url)
                new_urls = self.parser.parse_url(new_url, html)
                self.manager.add_new_urls(new_urls)
                print "-----"
                print "已经抓去%s个链接" % self.manager.get_old_urls_size()
                print "-----"






if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/www/109924?fromtitle=%E4%B8%87%E7%BB%B4%E7%BD%91&fromid=215515")

