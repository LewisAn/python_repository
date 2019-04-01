import re
import tld

import math
from core.config import badTypes
try:
    from urllib.parse import urlparse
except:
    from urlparse import urlparse


def extract_headers(headers):
    sorted_headers = dict()

    matches = re.findall(r'(.*):\s(.*)', headers)
    for match in matches:
        header = match[0]
        value = match[1]
        try:
            # Remove all the commas
            if value[-1] == ',':
                value = value[:-1]
            sorted_headers[header] = value
        except IndexError:
            pass

    return sorted_headers

def top_level(url):
    ext = tld.get_tld(url, fix_protocol=True) # ignore the protocol
    toplevel = '.'.join(urlparse(url).netloc.split('.')[-2:]).split(ext)[0] + ext
    return toplevel



def regxy(pattern, response, supress_regex, custom):
    """基于用户提供的正则表达式提取字符串"""
    try:
        matches = re.findall(r'%s' % pattern, response)
        for match in matches:
            custom.add(match)
    except:
        supress_regex = True

def is_link(url, processed, files):
    """检查一个链接是否应该被爬取"""
    # 如果文件存在就不应该被爬取
    conclusion = False
    # 如果这个链接并没有被爬取过
    if url not in processed:
        if url.split('.')[-1].lower() in badTypes:
            files.add(url)
        else:
            return True
    return conclusion

def entropy(string):
    """计算字符串的熵"""
    entropy = 0
    for number in range(256):
        result = float(string.encode('utf-8').count(chr(number)))/len(string.encode('utf-8'))
        if result != 0:
            entropy = entropy - result * math.log(result, 2)
    return entropy

def xmlParser(response):
    return re.findall(r'<loc>(.*?)</loc>', response)