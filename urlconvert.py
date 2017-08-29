#-*- coding:utf-8 -*-

#功能:迅雷地址转换
#包含：
#输入原始地址 -> 真实地址
#输入原始地址 -> 迅雷地址
#输入原始地址 -> 快车地址
#输入原始地址 -> 旋风地址

import base64
import urllib

#解析迅雷地址
def Thunderdecode(url):
    url = url.replace('thunder://','')
    thunderUrl = base64.b64decode(url)[2:-2]
    return thunderUrl

#解析快车地址
def Flashgetdecode(url):
    url=url.replace('Flashget://','')
    if '&' in url:
        url = url.split('&')[0]
    url = base64.b64decode(url)
    flashgeturl = url.replace('[FLASHGET]','')
    flashgeturl=flashgeturl.replace('[FLASHGET]','')
    return flashgeturl

#解析QQ旋风地址
def qqdecode(url):
    url=url.replace('qqdl://','')
    qqurl=base64.b64decode(url)
    return qqurl

#生成迅雷链接
def ThunderEncode(url):
    t_url = "thunder://"+base64.b64encode("AA"+url+"ZZ")
    return t_url

#生成快车链接
def flashetencode(url):
    f_url='Flashget://'+base64.b64encode('[FLASHGET]'+url+'[FLASHGET]')+'&1926'
    return f_url

#生成QQ旋风链接
def qqencode(url):
    q_url='qqdl://'+base64.b64encode(url);
    return q_url;


def urlconvert(oldurl):
    oldurl = oldurl.strip()
    if oldurl == '':
        print u'输入错误.'
    elif 'thunder://' in oldurl:
        newurl = Thunderdecode(oldurl) #将迅雷地址解析为真实地址
    elif 'Flashget://' in oldurl: #解析快车地址
        newurl=Flashgetdecode(oldurl)
    elif 'qqdl://' in oldurl: #解析旋风地址
        newurl = qqdecode(oldurl)
    else:
        newurl = oldurl

    thunderurl=ThunderEncode(newurl)
    flashgeturl=flashetencode(newurl)
    qqurl=qqencode(newurl)
    print thunderurl
    print flashgeturl
    print qqurl
    
    # ttt = ("&nbsp;&nbsp;&nbsp;<a href='javascript://' onclick='ConvertURL2FG(\""+flashgeturl+"\",\""+newurl+"\",1926)'></a>")
    # print ttt

if __name__ == '__main__':
    s = 'ed2k://|file|%E8%B6%8A%E7%8B%B1.Prison.Break.S05E06.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HDTVrip.720P.mp4|485576874|9d5a883b071aa5b938410580b56388ea|h=twaamvlskb7xymdfd27vl45kqlo3b7xk|/'
    urlconvert(s)
