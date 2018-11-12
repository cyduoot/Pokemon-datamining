def getmax(dat):
    max = -1
    for i in range(6):
        if int(dat[5+i]) > max:
            max = i
    return i


def calctype(cur):
    last = int(data[cur - 1].split(",")[-1])
    print(last)
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 0
    if i[2] != now[2]:
        cnt += 1
    if i[3] != now[3]:
        cnt += 1
    if i[-1] != "0":
        cnt += calctype(last)
    return cnt


def calcegg(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 0
    print(i[16], now[16])
    if i[16] != now[16]:
        cnt += 1
    if i[17] != now[17]:
        cnt += 1
    if i[-1] != "0":
        cnt += calcegg(last)
    return cnt

def calccolor(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 0
    if i[13] != now[13]:
        cnt += 1
    if i[-1] != "0":
        cnt += calccolor(last)
    return cnt


def calcheight(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 1
    cnt = cnt * float(now[19]) / float(i[19])
    print(float(i[19]), float(now[19]))
    if i[-1] != "0":
        cnt *= calcheight(last)
    return cnt


def calcweight(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 1
    cnt = cnt * float(now[20]) / float(i[20])
    if i[-1] != "0":
        cnt *= calcweight(last)
    return cnt


def calctotal(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 1
    cnt = cnt * float(now[4]) / float(i[4])
    if i[-1] != "0":
        cnt *= calctotal(last)
    return cnt

def calcvar(cur):
    last = int(data[cur - 1].split(",")[-1])
    i = data[last - 1]
    now = data[cur - 1]
    i = i.split(",")
    now = now.split(",")
    cnt = 0
    if getmax(i) != getmax(now):
        cnt += 1
    if i[-1] != "0":
        cnt += calcvar(last)
    return cnt


f = open("data_prev.csv",'r', encoding='UTF-8')
data = f.readlines()
data.pop(0)
processed = list()
islast=[0 for i in range(722)]
#print(data)
data1 = []
for i in data:
    i = i.strip("\n")
    data1.append(i)
    t = i.split(",")
    last = len(t)
    islast[int(t[last - 1])] = 1

data = data1
features = list()
cnt = 0

for i in data:
    cnt += 1
    if (islast[cnt] == 0) and (int(i[-1])!=0):
        feature = list()
        feature.append(cnt)
        feature.append(calctype(cnt))
        feature.append(calcegg(cnt))
        feature.append(calccolor(cnt))
        feature.append(calctotal(cnt))
        feature.append(calcheight(cnt))
        feature.append(calcweight(cnt))
        feature.append(calcvar(cnt))
        feature = [str(i) for i in feature]
        features.append(','.join(feature) + '\n')

f = open("features.csv", 'w')
f.writelines(features)
