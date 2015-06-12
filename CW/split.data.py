import xlrd

## Read All Conf ##
age = {}
bb = {}
ch = {}
gd = {}
pe = {}
sc = {}
wd = {}
ci = {}
conflist = {"Age.conf": age,"BuyBehavior.conf": bb,"Channel.conf": ch,"Gender.conf": gd,"Province.conf": pe,"subChannel.conf": sc,"Word.conf": wd, "CompetitiveWord.carVersusid.conf": ci}
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

data = xlrd.open_workbook('CompetitiveWord.xls')
table = data.sheet_by_name(u'Sheet1')
#print '\t'.join(table.row_values(0)).encode('utf8')
tmp = []
### Gen Channel Report #1 ###

###### PV UV #####
#f = open('PVUVURL.txt', 'w')
#for i in range(table.nrows):
#    tmp.append(table.row_values(i)[0:4])
#for el in tmp:
#    f.write("%s\t%s\n" % (ci[el[0]].encode("utf8"), "\t".join(el[1:]).encode('utf8')))
#f.close()
##################
tmpHash = {}
for i in range(table.nrows):
    tmpHash[table.row_values(i)[0]] = eval(table.row_values(i)[6])


for car in tmpHash:
    print tmpHash[car]['1']['uv']
    #print tmpHash['01001001001.844']['2.A.8']['uv']
