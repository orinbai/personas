#coding=utf8

startsign, datasign = 0, 0
tmpline = ''

def getnum(line):
    aa = []
    lines = line.split('</td>')
    for line in lines:
        if '<strong>' in line:
            aa.append(line[line.index('<strong')+8:line.rindex('</strong')])
            #print line[line.index('<strong')+8:line.rindex('</strong')]
        elif line.endswith('</span>'):
            aa.append(line[line.index('>')+1:line.rindex('<')])
        else:
            continue
    return aa
f = open('282.html')
strsales = []
for line in f:
    line = line.strip()
    if '汽车销量排行' in line and '<strong>' in line: startsign = 1
    if startsign:
        if line.startswith('<tr '): datasign = 1
        if line.startswith('</tr>'):
            datasign = 0
            tmparray = getnum(tmpline)
            if tmparray: strsales.append(tmparray)
            tmpline = ''
    if datasign:
        if line.startswith('<span '):
            tmpline += line
        else:
            continue
    if '</table>' in line: startsign = 0
f.close()
for content in strsales:
    print '\t'.join(content)
