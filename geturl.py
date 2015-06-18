#coding=utf8
import os

datadir = '/home/orin/Job/Personas'
baseURL = 'http://www.qichexl.com/a/xiaoliangpaixing/list_1_%d.html'
#os.system('wget http://www.qichexl.com/a/xiaoliangpaixing/ -P %s/resource/saledata' % datadir)
f = open('%s/resource/saledata/index.html' % datadir)
### First Get Total Page Number ###
for line in f:
    line = line.lower().strip()
    if '汽车销量排行榜'.decode('utf8').encode('gbk') in line and '<li>' in line:
        print line.decode('gbk').encode('utf8')

    if 'class="pageinfo"' in line: pagenum = int(line[line.index('<strong')+8:line.index('</strong>')])

### Iterate ###
for i in range(2, pagenum+1):
    print baseURL % i

f.seek(0)
f.close()

