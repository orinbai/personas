import os, re
#coding=utf8
progdir = '/home/orin/Job/Personas'
if not os.path.exists('%s/resource/search' % progdir): os.makedirs('%s/resource/search' % progdir)
specKey = '上市'
realAuto = {}
similar = {}
simMAP = {}
startsign = False
## Match Price ##
aPrice1 = re.compile('售([0-9,.]+)-([0-9,.]+)万')
aPrice2 = re.compile('售价([0-9,.]+)万')
eEm = re.compile('<em>(.*?)</em>')



def Gethtml(autoname):
    baseURL = 'http://sou.autohome.com.cn/wenzhang?q=%s&class=1&sort=Relevance&pvareaid=&searchtypeContent=content&entry=43&error=0'
    newURL = baseURL % autoname
    os.system('wget --output-document=%s/resource/search/tmpfile.txt %s' % (progdir, newURL))

def getINFO(a, b):
    #a = re.sub(eEm, '', a)
    k = eEm.findall(a)
    if k:
        print ':'.join(k)
    print ':'.join(eEm.findall(a))
    m = aPrice1.search(a)
    n = aPrice2.search(a)
    if m:
        price = m.groups()
        return price
    elif n:
        price = n.groups()
        return price
    else:
        print a
    return False
    titles = a.split('<em>')
    print ':'.join(titles)
    return False
    for tmpstr in titles:
        tmpstr = tmpstr.strip()
        ## Get Price ##
        m = aPrice1.search(tmpstr)
        n = aPrice2.search(tmpstr)
        if m:
            price = m.groups()
        elif n:
            price = n.groups()
        if isinstance(price, list): pass


## Read Auto List ##
## Need Mapping Similar Auto Id ##
f = open('%s/result/autoprice.txt' % progdir)
for line in f:
    lines = line.strip().split('\t')
    if float(lines[2]) == 0: continue
    realAuto[lines[1]] = [lines[0], lines[2], lines[3]]
    if '进口' in lines[0]: similar[lines[0][:lines[0].index('进口')-1]] = lines[1]
    continue
f.seek(0)
for line in f:
    lines = line.strip().split('\t')
    if float(lines[2]) == 0: continue
    if similar.has_key(lines[0]): simMAP[similar[lines[0]]] = lines[1]
f.close()

for tmpkey in realAuto.keys():
    #Gethtml(realAuto[tmpkey])
    #f = open('%s/resource/search/tmpfile.txt' % progdir)
    # Testing File ##
    print tmpkey
    tmpkey = '511'
    f = open('o.txt')
    for line in f:
        line = line.strip()
        if line.startswith('<dl class="list-dl">'):
            startsign = True
            continue
        if line == '</dl>': startsign = False
        if startsign:
            if line.startswith('<dt>'):
                urLink = line[line.index('href')+6:line.index('target')-2]
                title = line[line[5:].index('>')+6:line.rindex('</a>')]
                print urLink, title
                print getINFO(title, tmpkey)
                #print realAuto[tmpkey][1], realAuto[tmpkey][2]
        
    f.close()

