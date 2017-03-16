# encoding: utf-8
import sys
sys.path.append("..")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from general_index import General, GeneralIndex, rangerun, rangerun3
from copy import deepcopy
import util

class GL(GeneralIndex):
    def __init__(self, daima):
        super(GL, self).__init__(daima)

    def tupohl(self, n, m):
        print 'tupohl------%s------%s-----------'% (n, m)
        self.get_nhh(n)
        self.get_nll(n)
        self.get_mhh(m)
        self.get_mll(m)
        df = deepcopy(self.df) 

        # duo tou
        df['higher'] = df.h > df.nhh
        df['hbz'] = np.where(df['higher'], df.mll/df.nll , None)
        #df['hbz_biggerthan1'] = np.where(df.hbz>1, True, None)
        #print df.hbz.mean() # 应该大于1
        hlist = [x for x in sorted(df.hbz) if x>0]
        hlistbiggerthan1 = [x for x in hlist if x>1]
        hgl = len(hlistbiggerthan1)/float(len(hlist)) # 大于1 的概率
        print hgl, 'hgl'

        # kong tou  
        df['lower'] = df.l < df.nll
        df['lbz'] = np.where(df['lower'], df.mhh/df.nhh , None)
        #df['lbz_smallerthan1'] = np.where(df.lbz<1, True, None)

        #print df.lbz.mean() # 应该小于1
        llist = [x for x in sorted(df.lbz) if x>0]
        llistsmallerthan1 = [x for x in llist if x<1]
        lgl = len(llistsmallerthan1)/float(len(llist)) # 小于1 的概率
        print lgl, 'lgl'

        
        #df['bksk'] = np.where(df['lower'], 'sk' , df['bksk'])
#
        #df['phigher'] = df.h > df.nhhp 
        #df['bpsp'] = np.where(df['phigher'], 'sp' , None)
        #df['plower'] = df.l < df.nllp
        #df['bpsp'] = np.where(df['plower'], 'bp' , df['bpsp'])

        df.to_csv('tmp.csv')

    def hhll(self, n, m):
        '''低点更高，高点更低'''
        print 'hhll------%s------%s-----------'% (n, m)
        self.get_nhh(n)
        self.get_nll(n)
        self.get_mhh(m)
        self.get_mll(m)
        df = deepcopy(self.df) 

        # duo tou
        df['higher'] = df.l > df.nll
        df['hbz'] = np.where(df['higher'], df.mll/df.nll , None)
        #df['hbz_biggerthan1'] = np.where(df.hbz>1, True, None)
        #print df.hbz.mean() # 应该大于1
        hlist = [x for x in sorted(df.hbz) if x>0]
        hlistbiggerthan1 = [x for x in hlist if x>1]
        hgl = len(hlistbiggerthan1)/float(len(hlist)) # 大于1 的概率
        print hgl, 'hgl'

        # kong tou  
        df['lower'] = df.h < df.nhh
        df['lbz'] = np.where(df['lower'], df.mhh/df.nhh , None)
        #df['lbz_smallerthan1'] = np.where(df.lbz<1, True, None)

        #print df.lbz.mean() # 应该小于1
        llist = [x for x in sorted(df.lbz) if x>0]
        llistsmallerthan1 = [x for x in llist if x<1]
        lgl = len(llistsmallerthan1)/float(len(llist)) # 小于1 的概率
        print lgl, 'lgl'

        
        #df['bksk'] = np.where(df['lower'], 'sk' , df['bksk'])
#
        #df['phigher'] = df.h > df.nhhp 
        #df['bpsp'] = np.where(df['phigher'], 'sp' , None)
        #df['plower'] = df.l < df.nllp
        #df['bpsp'] = np.where(df['plower'], 'bp' , df['bpsp'])

        df.to_csv('tmp.csv')

if __name__ == '__main__':
    g = GL('dy') # ta rb c m a ma jd dy 999999
    #g.tupohl(2,2)
    #g.tupohl(2,3)
    g.tupohl(2,3)
    #g.tupohl(2,5)
    #g.tupohl(2,6)
    #g.tupohl(2,7)

    #g.hhll(2,2)
    #g.hhll(2,3)
    g.hhll(2,3)
    