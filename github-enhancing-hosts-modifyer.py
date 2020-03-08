####################
##Coded by CTRWaZ!##
####################

import requests as rq
from bs4 import BeautifulSoup
import os

os.chdir('C:\\Windows\\System32\\drivers\\etc\\')
def sip(lnk):
    get = rq.get(url = lnk)
    html = get.text
    bf = BeautifulSoup(html, 'html.parser')
    a = bf.find_all('li')[0].text.replace('<li>', '')
    return a

def mip(mlnk):
    get = rq.get(url = mlnk)
    html = get.text
    bf = BeautifulSoup(html, 'html.parser')
    ip1 = bf.find_all('a')[3].text.replace('<a>', '')
    ip2 = bf.find_all('a')[4].text.replace('<a>', '')
    ip3 = bf.find_all('a')[5].text.replace('<a>', '')
    ip4 = bf.find_all('a')[6].text.replace('<a>', '')
    return [ip1, ip2, ip3, ip4]

def mip3(mlnk3):
    get = rq.get(url = mlnk3)
    html = get.text
    bf = BeautifulSoup(html, 'html.parser')
    ip1 = bf.find_all('a')[3].text.replace('<a>', '')
    ip2 = bf.find_all('a')[4].text.replace('<a>', '')
    ip3 = bf.find_all('a')[5].text.replace('<a>', '')
    return [ip1, ip2, ip3]

github, fastly, codeload, nodeload, gist, raw, training, avtr1, avtr2, cdn1, cdn2, cdn3, cdn4, doc1, doc2, doc3, doc4, help1, help2, help3, help4, stat1, stat2, stat3 = sip("https://github.com.ipaddress.com/"),sip("http://fastly.net.ipaddress.com/github.global.ssl.fastly.net"),sip("https://github.com.ipaddress.com/codeload.github.com"),sip("https://github.com.ipaddress.com/nodeload.github.com"),sip("https://github.com.ipaddress.com/gist.github.com"),sip("https://github.com.ipaddress.com/raw.github.com"),sip("https://github.com.ipaddress.com/training.github.com"),sip("https://githubusercontent.com.ipaddress.com/avatars0.githubusercontent.com"),sip("https://githubusercontent.com.ipaddress.com/avatars1.githubusercontent.com"),mip("https://github.com.ipaddress.com/assets-cdn.github.com")[0],mip("https://github.com.ipaddress.com/assets-cdn.github.com")[1],mip("https://github.com.ipaddress.com/assets-cdn.github.com")[2],mip("https://github.com.ipaddress.com/assets-cdn.github.com")[3],mip("https://github.com.ipaddress.com/documentcloud.github.com")[0],mip("https://github.com.ipaddress.com/documentcloud.github.com")[1],mip("https://github.com.ipaddress.com/documentcloud.github.com")[2],mip("https://github.com.ipaddress.com/documentcloud.github.com")[3],mip("https://github.com.ipaddress.com/help.github.com")[0],mip("https://github.com.ipaddress.com/help.github.com")[1],mip("https://github.com.ipaddress.com/help.github.com")[2],mip("https://github.com.ipaddress.com/help.github.com")[3],mip3("https://github.com.ipaddress.com/status.github.com")[0],mip3("https://github.com.ipaddress.com/status.github.com")[1],mip3("https://github.com.ipaddress.com/status.github.com")[2]

with open('hosts', 'r+') as f:
    h = f.readlines()   
    ln = 0
    tgln = []

    for l in h:
        if l.find('github.com') != -1 or l.find('githubusercontent.com') != -1 or l.find("github.global") != -1:
            tgln += [ln]
        ln += 1
    f.close()

tgln.reverse()
for a in tgln:
    del h[a]

with open('hosts_new.txt', 'w+') as wr:
    wr.writelines(h + [github+' github.com\n', cdn1 + ' assets-cdn.github.com\n', cdn2 + ' assets-cdn.github.com\n', cdn3 + ' assets-cdn.github.com\n', cdn4 + ' assets-cdn.github.com\n', fastly + ' github.global.ssl.fastly.net\n', codeload + ' codeload.github.com\n', nodeload + ' nodeload.github.com\n', help1 + ' help.github.com\n', help2 + ' help.github.com\n', help3 + ' help.github.com\n', help4 + ' help.github.com\n', gist + ' gist.github.com\n', raw + ' raw.github.com\n', training + ' training.github.com\n', doc1 + ' documentcloud.github.com\n', doc2 + ' documentcloud.github.com\n', doc3 + ' documentcloud.github.com\n', doc4 + ' documentcloud.github.com\n', stat1 + ' status.github.com\n', stat2 + ' status.github.com\n', stat3 + ' status.github.com\n', avtr1 + ' avatars0.githubusercontent.com\n', avtr2 + ' avatars1.githubusercontent.com\n'])
    wr.close()

os.rename('hosts', 'hosts.bak')
os.rename('hosts_new.txt', 'hosts')
os.remove('hosts.bak')
os.system("ipconfig /flushdns")