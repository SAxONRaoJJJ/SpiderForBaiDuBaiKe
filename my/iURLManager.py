# coding=utf-8

# url管理器


class URLManager(object):

    def __init__(self):
        self.new_urls = set()  # 未爬取url集合
        self.old_urls = set()  # 已爬取url集合

    # 判断是否还有未爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取一个新的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    # 添加一个新的url
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 添加一些新的url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 获取未爬取的url集合的大小
    def get_new_urls_size(self):
        return len(self.new_urls)

    # 获取已爬取的url集合的大小
    def get_old_urls_size(self):
        return len(self.old_urls)