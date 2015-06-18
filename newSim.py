# coding=utf8
import numpy as np
import math

class ClusterClassify:
    def __init__(self, samplefile):
        ### Data Part ###
        self.samplefile = samplefile
        self.symbolHash = {}
        self.fnameHash = {}
        self.Matrix = np.array([])
        self.Matrix.num = []
        self.Matrix.nom = []
        self.numvar = []
        self.colnum = 0
        self._symbol2var()
        self._genMatrix()
        ### Num Part ###
        self.addbycol = [0]*self.colnum
        self.sumbycol = [0]*self.colnum
        self.addvarcol = [0]*self.colnum
        self.varbycol = [0]*self.colnum
        self.rownum = 0.0

    def _symbol2var(self):
        ## Nominal Variable Auto Detection ##
        f = open(self.samplefile)
        symbolArray = []
        for line in f:
            lines = line.strip().split('\t')
            ## Sample Text must have Header ## 
            if not lines[-1].startswith('clus'):
                ### Exclude Name, ClusterName, Get Variable ###
                self.colnum = len(lines)-2
                tmpnum = range(len(lines))
                symbolArray = [{} for tmp in tmpnum]
                fnameHash = dict(zip(tmpnum, lines))
                continue
            for indexnum, tmpline in enumerate(lines):
                ### element is int or decimal ###
                if tmpline.isdigit() or tmpline.replace('.', '', 1).isdigit():
                    continue
                else:
                    ### NOT Use First and Last Variable (Car Name and Cluster Name) ###
                    if symbolArray[indexnum].has_key(tmpline) or indexnum == 0 or indexnum==len(lines)-1:
                        continue
                    else:
                        symbolArray[indexnum][tmpline] = True
        f.close()

        for indexnum, tmpline in enumerate(symbolArray):
            if tmpline:
                self.symbolHash[indexnum] = dict(zip(tmpline.keys(), range(len(tmpline.keys()))))
            else:
                self.numvar.append(indexnum)
#        print self.symbolHash.keys()
#        print self.symbolHash[3]['涡轮增压']
#        print ':'.join(self.symbolHash[3].keys())
        
        return True

    def _genMatrix(self):
        self.Matrix = np.loadtxt(self.samplefile, dtype=np.str)
        self.Matrix.nom = self.Matrix[:, self.symbolHash.keys()+1].astype(np.str)
        self.Matrix.num = self.Matrix[:, self.numvar].astype(np.float)
        return True

    def clear(self):
        self.Matrix = ''
        self.addbycol = [0]*self.colnum
        self.sumbycol = [0]*self.colnum
        self.addvarcol = [0]*self.colnum
        self.varbycol = [0]*self.colnum
        self.rownum = 0.0


    def Mean(self, Matrix, AddElement=False):
        self.sumbycol = [0]*self.colnum
        self.rownum = 0.0
        #if AddElement: Matrix.append(AddElement)
        for ele in Matrix:
            self.rownum += 1
            for i in range(self.colnum): self.sumbycol[i] += ele[i]

        return map(lambda x: x/float(self.rownum), self.sumbycol)

    def Var(self, Matrix, AddElement=False):
        #if AddElement: Matrix.append(AddElement)
        self.Mean(Matrix)
        self.varbycol = [0]*self.colnum

        for ele in Matrix:
            for i in range(self.colnum):
                self.varbycol[i] += (ele[i] - self.sumbycol[i]/self.rownum)**2
        #if AddElement: Matrix.pop()
        return map(lambda x: x/self.rownum, self.varbycol)

    def Prob(self, Matrix):
        return False

    def Epsilon(self, VARk, VARvk, Nv):
        ### According to the TwoStep Cluster: Epsilon(i) = -Nv*Sum(0.5*log(Vark, Varvk)) ###
        epsilon = 0
        for varnum in range(self.colnum):
            #print VARk[varnum], VARvk[varnum]
            #print VARk[varnum] + VARvk[varnum]
            #print 0.5*math.log(VARk[varnum] + VARvk[varnum])
            epsilon += 0.5*math.log(VARk[varnum] + VARvk[varnum])

        epsilon = -1*epsilon*Nv
        #print Nv, epsilon
        #print '='*30
        return epsilon

