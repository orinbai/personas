#coding=utf8

## threshold: 60%  ##
THRESHOLD = .7
EPSILON = 0.0001 ## Avoid divide by zero ##
### colsum means sum by col, totalcars means the number of cars ###
colsum = [0]*134
totalcars = 0

f = open('aa.txt')
line = f.readline()
header = line.strip().split('\t')[87:]
del header[89:91]
priceArray = [[] for i in range(len(header))]
Terval = [[0]*2 for i in range(len(header))]
SettingTerval = {}
for line in f:
    ## start at 87th col ##
    lines = line.strip().split('\t')
    ## Use min Price as Price ##
    price = float(lines[11])
    lines = lines[87:]
    totalcars += 1
    del lines[89:91]
    try:
        lines = map(float, lines)
    except:
        print 'something is wrong\n%s' % line
        exit()
    for i, v in enumerate(lines):
        if v:
            #print header[i], v
            priceArray[i].append(price)
            #print priceArray

    colsum = map(lambda x: x[0]+x[1], zip(colsum, lines))
f.close()


def priceWeight(price, dArray, rev=False):
    weightmp = [[header[i[0]], i[1]] for i in sorted([[n, Zerones(price, SettingTerval[header[n]])] for n in dArray], key=lambda x:x[1], reverse=rev)]
    return weightmp


def Zerones(price, interval):
    return (price - interval[0])/(interval[1] - interval[0] + EPSILON)

#print ','.join(filter(lambda x: x, map(lambda x: x[0]/90.0 > .6 and x[1], zip(colsum, header))))

## Computing Price Interval of Features ##
for n, priceTerval in enumerate(priceArray):
    #print n, priceTerval
    if priceTerval:
        Terval[n][0] = min(priceTerval)
        Terval[n][1] = max(priceTerval)
#    try:
#        print header[n], Terval[n]
#    except:
#        print n, priceArray[n]
#        exit()

## Gen Standard Setting and Price Interval of Feature ##
Settingstd = [n for n, item in enumerate(colsum) if item/90 > THRESHOLD]
SettingTerval = dict(zip(header, Terval))

#print ','.join(map(lambda x: header[x], settingstd))
#exit()
## Gen Summary Stat ##
m = open('competitive.tsv', 'w')
f = open('aa.txt')
f.readline()
for line in f:
    lines = line.strip().split('\t')
    price = float(lines[11])
    cname = [lines[5], lines[7]]
    lines = lines[87:]
    del lines[89:91]
    #print lines
    #print ','.join(map(lambda x: header[x], filter(lambda x: x in settingstd, [n for n, item in enumerate(lines) if not float(item)])))
    less = filter(lambda x: x in Settingstd, [n for n, item in enumerate(lines) if not float(item)])
    more = filter(lambda x: not (x in Settingstd), [n for n, item in enumerate(lines) if float(item)])
    #print ','.join([header[item] for n,item in enumerate(more)])
    priceWeight(price, more)
    #print '\t'.join(['%s,%2f' % (i[0], i[1]) for i in priceWeight(price, more)[:5]])
    m.write("%s\n" % ('\t'.join([cname[1], str(price), str(len(less)), str(len(more)), ','.join(['%s' % i[0] for i in priceWeight(price, more)[:5]]), ','.join(['%s' % i[0] for i in priceWeight(price, less, rev=True)[:5]])])))
f.close()
m.close()
