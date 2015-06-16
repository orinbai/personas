#coding=utf8
import xlrd

## float not encode ##
def typedetectiv(aa):
    if type(aa) == float:
        return str(aa)
    else:
        return aa

## Read All Conf ##
age = {}
bb = {}
ch = {}
gd = {}
pe = {}
sc = {}
wd = {}
ci = {}
city = {}
st = {}
conflist = {"Age.conf": age,"BuyBehavior.conf": bb,"Channel.conf": ch,"Gender.conf": gd,"Province.conf": pe,"subChannel.conf": sc,"Word.conf": wd, "CompetitiveWord.carVersusid.conf": ci, 'citi.conf':city, 'Setting.conf':st}
for everyconf in conflist:
    #print "="*10, everyconf, "="*10
    f = open("conf/%s" % everyconf)
    f.next()
    for line in f:
        if line.strip():
            lines = line.strip().split("\t")
            conflist[everyconf][lines[0]] = lines[1].decode('utf8')
        else:
            continue
    f.close()

TotalUserPcar = {}

data = xlrd.open_workbook('lingdu.xls')
table = data.sheet_by_index(1)
#print '\t'.join(table.row_values(0)).encode('utf8')
tmp = []
### Gen Channel Report #1 ###

###### PV UV #####
#f = open('data/PVUVURL.txt', 'w')
#for i in range(table.nrows):
#    tmp.append(table.row_values(i)[0:4])
#for el in tmp:
#    f.write("%s\t%s\n" % (ci[el[0]].encode("utf8"), "\t".join(el[1:]).encode('utf8')))
#f.close()
##################

#### Big Word ###
tmpHash = {}
#### Need a Sum of Users for EveryCar, Male(1) plus Female(2) ###
f = open('aa.txt','w')
for i in range(table.nrows):
    if i == 0:
        f.write('%s\n' % '\t'.join(map(lambda x: st[x].encode('utf8'), map(typedetectiv, table.row_values(i)))))
        #pass
    else:
        #print type(table.row_values(i)[4]), str(table.row_values(i)[4])
        f.write('%s\n' % '\t'.join(map(lambda x: x.encode('utf8'), map(typedetectiv, table.row_values(i)))))
f.close()

#print TotalUserPcar

#f = open('data/ca.csv', 'w')
#for i in range(table.nrows):
#    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[9])
#tmpArr = []
#f.write("%s,%s\n" % ('Car', ','.join(map(lambda x: wd[x], sorted(wd.keys()))).encode('utf8')))
#for car in tmpHash:
#    for word in sorted(wd.keys()):
#        tmpArr.append(str(float(tmpHash[car][word]['uv'])/TotalUserPcar[car]))
#    f.write("%s,%s\n" % (ci[car].encode("utf8"), ','.join(tmpArr)))
#    tmpArr = []
#f.close()

### City Level ###
#f = open('data/bw.citi.csv', 'w')
#for i in range(table.nrows):
#    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[8])
#
#for car in tmpHash:
#    if car == '01001001001.395': continue
#    ### Big Word in City ###
#    for clvl in sorted(tmpHash[car]):
#        #tmpHash[car][clvl]['pcontent']
#        for word in sorted(wd):
#            f.write('%s,%s,%s,%s\n' % (ci[car].encode('utf8'), city[clvl].encode('utf8'), wd[word].encode('utf8'), tmpHash[car][clvl]['pcontent'][word]['uv']))
#f.close()

#### Gender Level ###
#f = open('data/bw.gender.csv', 'w')
#for i in range(table.nrows):
#    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[6])
#
#for car in tmpHash:
#    if car == '01001001001.395': continue
#    for gender in sorted(tmpHash[car]):
#        for word in sorted(wd):
#            f.write('%s,%s,%s,%s\n' % (ci[car].encode('utf8'), gd[gender].encode('utf8'), wd[word].encode('utf8'), tmpHash[car][gender]['pcontent'][word]['uv']))
#
#f.close()

### Age Level ###
#f = open('data/bw.age.csv', 'w')
#for i in range(table.nrows):
#    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[7])
#
#for car in tmpHash:
#    if car == '01001001001.395': continue
#    for ages in sorted(tmpHash[car]):
#        for word in sorted(wd):
#            f.write('%s,%s,%s,%s\n' % (ci[car].encode('utf8'), age[ages].encode('utf8'), wd[word].encode('utf8'), tmpHash[car][ages]['pcontent'][word]['uv']))
#f.close()

#f = open('data/bw.channel.csv', 'w')
#for i in range(table.nrows):
#    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[10])
#
#for car in tmpHash:
#    if car == '01001001001.395': continue
#    for channel in sorted(tmpHash[car]):
#        print '%s, %s, %s' % (ci[car].encode('utf8'), ch[channel].encode('utf8'), tmpHash[car][channel]['uv'])

