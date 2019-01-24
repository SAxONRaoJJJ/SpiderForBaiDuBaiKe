# coding=utf-8

import requests


class HTMLDownloader(object):

    # 下载url资源
    def downloadUrl(self, url):
        if url is None:
            return
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        headers = {"User-Agent": user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = "utf-8"
            return r.text
        return None




