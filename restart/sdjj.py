# encoding: utf-8
import sys
sys.path.append("..")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from general_index import General, GeneralIndex


class Sdjj(GeneralIndex):
    def __init__(self, daima):
        super(Sdjj, self).__init__(daima)
        self.get_ma(5,10,20)


    def foo(self):
        print self.df['o']
        pass

    def tupo_sdhsdl(self, n=10):
        '''四点均线突破前n天最高开多，突破前n天最低开空
        暂时还想不出移动止损怎么写，先写不带移动止损的，用信号平仓的策略
        '''
        self.get_nsdl(n)
        self.get_nsdh(n)
        #self.df['tupo_sdh'] = self.df.sdjj.shift(1) < self.df.nsdh.shift(1) & self.df.sdjj > self.df.nsdh 
        self.df['tmp1'] = self.df.sdjj.shift(1) < self.df.nsdh.shift(1)
        self.df['tmp2'] = self.df.sdjj > self.df.nsdh
        self.df['tupo_sdh'] = self.df.tmp1 & self.df.tmp2  #今天的四点均价突破前n天的四点均价高点
        self.df['bksk'] = np.where(self.df['tupo_sdh'], 'bk' , None)
        #self.df.loc[: ,'bkcnt'] = 0
        #self.df['bkcnt'] = np.where(self.df['tupo_sdh'], self.df.bkcnt.shift(1)+1 , self.df.bkcnt.shift(2))

        self.df['tmp1'] = self.df.sdjj.shift(1) > self.df.nsdl.shift(1)
        self.df['tmp2'] = self.df.sdjj < self.df.nsdl
        self.df['tupo_sdl'] = self.df.tmp1 & self.df.tmp2
        # bk表示买开仓或买平仓，sk相反
        self.df['bksk'] = np.where(self.df['tupo_sdl'], 'sk' , self.df['bksk'])

        cnt = 0 # 每出一次开仓信号，就开一手，共几手的计数。一旦相反信号出来全平仓
        kprice = 0 # 所有持仓的开仓价格之和，不是多仓就是空仓
        total = 0

        # 做多
        for i, bksk in enumerate(self.df.bksk):

            idx = self.df.index[i]
            
            if bksk == 'bk':
                
                bkprice = self.df.loc[idx, 'sdjj'] # 买开仓的价位
                #print bkprice
                kprice += bkprice
                cnt += 1
            elif bksk == 'sk' and cnt != 0:
                skprice = self.df.loc[idx, 'sdjj']
                gain = skprice*cnt - kprice # 平仓盈亏
                #print skprice, kprice, gain
                total += gain
                print cnt, total
                cnt = 0
                kprice = 0
                
        

        cnt = 0 # 每出一次开仓信号，就开一手，共几手的计数。一旦相反信号出来全平仓
        kprice = 0 # 所有持仓的开仓价格之和，不是多仓就是空仓
        total = 0
        # 做空 分开计算容易写
        for i, bksk in enumerate(self.df.bksk):

            idx = self.df.index[i]
            
            if bksk == 'sk':
                
                skprice = self.df.loc[idx, 'sdjj'] # 开仓的价位
                #print skprice
                kprice += skprice
                cnt += 1
            elif bksk == 'bk' and cnt != 0:
                bkprice = self.df.loc[idx, 'sdjj'] # 平仓价格
                gain = kprice - bkprice*cnt # 平仓盈亏
                #print skprice, kprice, gain
                total += gain
                print cnt, total
                cnt = 0
                kprice = 0


if __name__ == '__main__':
    s = Sdjj('rb')
    #s.foo()
    
    s.tupo_sdhsdl()
    #print s.df.index
    #print s.df.loc[:, ['date','sdjj', 'tupo_sdl', 'tupo_sdh']]
    #s.df.to_csv('tmp.csv')  
    #df = pd.read_csv('../data/%s.xls' % 'RBL9')
    #print df