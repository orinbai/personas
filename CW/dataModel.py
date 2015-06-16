#coding=utf8
colsum = [0]*134
f = open('aa.txt')
line = f.readline()
header = line.strip().split('\t')[87:]
del header[89:91]
for line in f:
    ## start at 87th col ##
    lines = line.strip().split("\t")[87:]
    del lines[89:91]
    try:
        lines = map(float, lines)
    except:
        print 'something is wrong\n%s' % line
        exit()

    colsum = map(lambda x: x[0]+x[1], zip(colsum, lines))

f.close()

