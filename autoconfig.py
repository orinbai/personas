a = {}
f = open('602.html')
for line in f:
    line = line.strip()
    if line.startswith('var config '): ## base params ##
        line = line[line.index('{'):-1]
        print line
        eval('a='+line)
        print a['result']['paramtypeitems']['paramitems'][2]['name']
        pass

    if line.startswith('var option '): ## safe and others ##
        line = line[line.index('{'):]
        #print line
        pass

f.close()
