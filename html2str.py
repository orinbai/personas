import os, sys, time, re
### Convert HTML file to Structure Txt File ###
jobdir = '/home/orin/Job/Personas'


### Wget the Full List of Auto ###
#baseURL = 'http://www.autohome.com.cn/grade/carhtml'
#for i in range(97, 123):
#    os.system('wget %s/%s.html' % (baseURL, chr(i)))
#    time.sleep(10)

##################################
def genStructure(lines):
    carHash = {}
    for line in lines:
        if line.startswith('<dt>'):
            tmpline = line.split('</a>')
            brand = tmpline[1][tmpline[1].rindex('>')+1:]
            carHash[brand] = {}
        if line.startswith('<div'):
            ## subrand ##
            subrand = line[line.index('>')+1: line.rindex('<')]
            carHash[brand][subrand] = []
            ## car id ##
        if '<li' in line:
            carID = line[line.index('"')+2: line.rindex('"')]
            ## car name ##
        if line.startswith('<h4'):
            line1 = line.split('</a>')
            carNM = line1[0][line1[0].rindex('>')+1:]
            carPR = line1[1][line1[1].rindex('>')+1:-2]
            if '-' not in carPR:
                if carPR.isdigit():
                    (carPRmin, carPRmx) = (carPR, carPR)
                else:
                    (carPRmin, carPRmx) = ('0', '0')
            else: (carPRmin, carPRmx) = carPR.split('-')
            carHash[brand][subrand].append([carNM, carID, carPRmin, carPRmx])
    return carHash

for filename in os.listdir('%s/resource' % jobdir):
    lines = []
    rHash = {}
    startsign = False
    if os.path.getsize('%s/resource/%s' % (jobdir, filename)) < 1: continue
    f = open('%s/resource/%s' % (jobdir, filename))
    ##  Test file  ##
    #f = open('c.html')
    #################
    for line in f:
        line = line.strip()
        ## subBrand start ##
        if line == '<dl>':
            startsign = True
            continue
        if startsign:
            lines.append(line)
        if line == '</dl>':
            startsign = False
            rHash = genStructure(lines)
            for pkeys in rHash.keys():
                for tkeys in rHash[pkeys]:
                    if tkeys:
                        for tmpcar in rHash[pkeys][tkeys]:
                                print '%s\t%s\t%s' % ('\t'.join(tmpcar).decode('gbk').encode('utf8'), tkeys.decode('gbk').encode('utf8'), pkeys.decode('gbk').encode('utf8'))


            lines = []

    f.close()

