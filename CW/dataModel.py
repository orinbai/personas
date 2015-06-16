#coding=utf8

## threshold: 60%  ##
THRESHOLD = .6
### colsum means sum by col, totalcars means the number of cars ###
colsum = [0]*134
totalcars = 0

f = open('aa.txt')
line = f.readline()
header = line.strip().split('\t')[87:]
del header[89:91]
priceArray = [[] for i in range(len(header))]
Terval = [[0]*2 for i in range(len(header))]
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

#print ','.join(filter(lambda x: x, map(lambda x: x[0]/90.0 > .6 and x[1], zip(colsum, header))))

## Computing Price Interval of Features ##
for n, priceTerval in enumerate(priceArray):
    #print n, priceTerval
    if priceTerval:
        Terval[n][0] = min(priceTerval)
        Terval[n][1] = max(priceTerval)
    try:
        print header[n], Terval[n]
    except:
        print n, priceArray[n]
        exit()

## Gen Std. Setting ##
settingstd = [n for n, item in enumerate(colsum) if item/90 > THRESHOLD]

## 
