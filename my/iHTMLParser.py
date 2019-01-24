# coding=utf-8

import re
import urlparse
from bs4 import BeautifulSoup


class HTMLParser(object):

    def parse_url(self, page_url, content):
        if page_url is None or content is None:
            return
        soup = BeautifulSoup(content, "html.parser")
        soup.encode("utf-8")
        new_urls = self.get_new_urls(page_url, soup)
        self.get_new_contents(page_url, soup)
        return new_urls

    def get_new_urls(self, page_url, soup):
        new_urls = set()  # 集合去重
        links = soup.find(class_="lemma-summary").find_all("a", {"href": re.compile(r"/item/*")})
        for link in links:
            if link is None:
                continue
            new_full_url = urlparse.urljoin(page_url, link["href"])
            new_urls.add(new_full_url)
        return new_urls

    def get_new_contents(self, page_url, soup):

        iUrl = page_url
        iTitle = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1").get_text()
        iContent = soup.find("div", class_="lemma-summary").get_text()
        print "----URL----"
        print iUrl
        print "----Title----"
        print iTitle
        print "----Content----"
        print iContent

