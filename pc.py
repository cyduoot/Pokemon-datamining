import urllib.request
import urllib
import gzip

def getUrlContent(url):  
    #返回页面内容  
    doc = urllib.request.urlopen(url).read()  
    #解码  
    try:  
        html=gzip.decompress(doc).decode("utf-8")  
    except:  
        html=doc.decode("utf-8")  
    return html 

f = open("cnname.txt",'r', encoding='UTF-8')
names = f.readlines()
prev = [0 for i in range(722)]
cnt = 0
for name in names:
    cnt += 1
    if prev[cnt]!=0:
        continue

    t = name.strip("\n\r")
    t=urllib.parse.quote(t)
    url = r'https://wiki.52poke.com/index.php?title=' + t + '&action=edit'
    print(url)
    html = getUrlContent(url)
    cur = 0
    cur = html.find("sprite", cur)
    print(cur)
    last = 0
    while cur != -1:
        while html[cur]!='=':
            cur += 1
        if html[cur+1] == '=':
            break
        try:
            num = int(html[cur+1:cur+4])
        except:
            break
        prev[num] = last
        if html[cur-1].isdigit():
            last = num

        cur = html.find("sprite", cur)
    print(cnt,",", prev[cnt])

cnt = 0
for i in prev:
    print(cnt,",", i)