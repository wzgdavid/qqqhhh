'''
每天的平均波幅
因为这个取中位数比较的，所以用主连也问题不大，主连真实点，下次弄主连数据
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from common import *#get_DKX, get_nhh, get_nll, get_ma, avg,get_nhhzs,get_nllzs,get_atr

def foo1():
    pinzhong = 'pp'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))
    df = get_ma(df, 10)
    df['condition'] = np.where(df.c.shift(1)>df.ma.shift(1), 1, None) 
    #mean      1.000254     0.008770     0.008966
    #mean      1.000256     0.008764     0.009172
    df = df.dropna()
    df['收盘的波幅'] =   df.c/df.c.shift(1)
    #df['收盘的波幅'] =   np.abs(df.c/df.c.shift(1)-1)
    df['高价的波幅'] =   df.h/df.c.shift(1)-1
    df['低价的波幅'] = 1-df.l/df.c.shift(1)

    
    print(df.describe()[['收盘的波幅','高价的波幅','低价的波幅']])
    df.to_csv('tmp.csv')
#foo1()



'''
==============================================================================
'''

def foo2():
    pinzhong = 'rb'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))
    df = get_ma(df, 20)
    #df['condition'] = np.where(df.c.shift(1)>df.ma.shift(1), 1, None) 
    #df = df.dropna()

    df['阴阳'] = np.where(df.c>df.o, 1, None) 
    df['阴阳'] = np.where(df.c<df.o, 0, df['阴阳']) 
    df['h_to_c'] = df.h/df.c - 1
    df['l_to_c'] = 1 - df.l/df.c
    yang = df[df['阴阳']==1]
    yin = df[df['阴阳']==0]
    need_list = ['h_to_c','l_to_c']
    print(df.describe()[need_list])
    print(yang.describe()[need_list])
    print(yin.describe()[need_list])
    df.to_csv('tmp.csv')
    #df['aa'] = # 阳线高点到当天收盘价波幅
#foo2()


def foo3():
    '''
    之前是相对于前收的百分比，
    这个是相对于前收的多少ATR
    '''
    pinzhong = 'a'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))
    df = get_ma(df, 10)
    df = get_atr(df, 50)
    #df['condition'] = np.where(df.c.shift(1)>df.ma.shift(1), 1, None) 

    df = df.dropna()
    df['收盘的波幅'] =  ( df.c-df.c.shift(1))  / df.atr
    #df['收盘的波幅'] =   np.abs(df.c/df.c.shift(1)-1)
    df['高价的波幅'] =   (df.h-df.c.shift(1)) / df.atr
    df['低价的波幅'] = (df.c.shift(1)-df.l) / df.atr

    
    print(df.describe()[['收盘的波幅','高价的波幅','低价的波幅']])
    #df.to_csv('tmp.csv')
#foo3()

def foo4():
    '''
    之前是相对于前收的百分比，
    这个是相对于前收的多少ATR
    '''
    pinzhong = 'ppl930m'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))

    df = get_ma(df, 5)
    df['ma短'] = df.ma
    df = get_ma(df, 20)
    df['ma长'] = df.ma

    df = get_atr(df, 50)

    #df['condition'] = np.where(df.c.shift(1)<df.ma.shift(1), 1, None) # ma上下  
 
    
    df['收盘的波幅'] =  ( df.c-df.c.shift(1))  / df.atr.shift(1)
    df['收盘的波幅b'] =  np.abs( ( df.c-df.c.shift(1))  / df.atr.shift(1) )
    df['高价的波幅'] =   (df.h-df.c.shift(1)) / df.atr.shift(1)
    df['低价的波幅'] = (df.l-df.c.shift(1)) / df.atr.shift(1)
    df = df.dropna()
    
    print(df.describe()[['收盘的波幅','高价的波幅','低价的波幅']])
    #print('收盘标准差', df['收盘的波幅'].std())
    df.to_csv('tmp.csv')
    # 各比例  止损的期望 
    print(0.1, 0.9*df['高价的波幅'].quantile(0.1))  # 10%的幅度，有90%概率止损 
    print(0.2, 0.8*df['高价的波幅'].quantile(0.2)) 
    print(0.25, 0.75*df['高价的波幅'].quantile(0.25)) 
    print(0.3, 0.7*df['高价的波幅'].quantile(0.3)) 
    print(0.4, 0.6*df['高价的波幅'].quantile(0.4)) 
    print(0.5, 0.5*df['高价的波幅'].quantile(0.5)) 
    print(0.6, 0.4*df['高价的波幅'].quantile(0.6)) 
    print(0.7, 0.3*df['高价的波幅'].quantile(0.7)) 
    print(0.75, 0.25*df['高价的波幅'].quantile(0.75)) 
    print(0.8, 0.2*df['高价的波幅'].quantile(0.8)) 
    print(0.9, 0.1*df['高价的波幅'].quantile(0.9)) 
    print(0.95, 0.05*df['高价的波幅'].quantile(0.95)) 
    print(0.98, 0.02*df['高价的波幅'].quantile(0.98)) 
    print(0.99, 0.01*df['高价的波幅'].quantile(0.99)) 
foo4()

def foo4c(n):
    '''
    和foo4一样，
    只是不是算后一天的最高最低价范围
    而是后n天内高低价的范围
    比如后10天的最高最低价，相对于这一天收盘价的波幅（ATR）
    '''
    pinzhong = 'sr'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))
    df = get_ma(df, 20)
    df = get_atr(df, 50)

    df = get_nll2(df, n)
    df = get_nhh2(df, n)

    df['高价的波幅'] =   (df.nhh2-df.c) / df.atr
    df['低价的波幅'] = (df.nll2 -df.c) / df.atr
    df['低价的波幅abs'] = np.abs((df.nll2 -df.c) / df.atr)
    df['波幅大的一边'] = np.where(df['高价的波幅']>df['低价的波幅abs'],df['高价的波幅'],df['低价的波幅abs'])
    df['收盘的波幅'] = np.abs((df.c.shift(-n) - df.c) / df.atr)
    df = df.dropna()
    
    print(df.describe()[['高价的波幅','低价的波幅']])
    #print('收盘标准差', df['收盘的波幅'].std())
    print(df['高价的波幅'].quantile(0.5))
    print(df['低价的波幅'].quantile(0.5))
    print(df['波幅大的一边'].quantile(0.5)) #
    print(df['波幅大的一边'].quantile(0.85)) # 
    print(df['收盘的波幅'].quantile(0.5)) #
    df.to_csv('tmp.csv')
#foo4c(10)

def foo4b(n):
    '''
    和foo4一样，
    只是不是相对于昨天，而是相对于前n天
    '''
    pinzhong = 'rb'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))
    df = get_ma(df, 20)
    df = get_atr(df, 50)

    df['condition'] = np.where(df.c.shift(n)>df.ma.shift(n), 1, None) # ma上下  目前效果最明显的还是这个

    df['收盘的波幅'] =  ( df.c-df.c.shift(n))  / df.atr.shift(n)
    df['收盘的波幅b'] =  np.abs( ( df.c-df.c.shift(n))  / df.atr.shift(n) )
    df['高价的波幅'] =   (df.h-df.c.shift(n)) / df.atr.shift(n)
    df['低价的波幅'] = (df.l-df.c.shift(n)) / df.atr.shift(n)
    df = df.dropna()
    
    print(df.describe()[['收盘的波幅','高价的波幅','低价的波幅']])
    #print('收盘标准差', df['收盘的波幅'].std())
    df.to_csv('tmp.csv')
#foo4b(2)



def foo5():
    '''
    看高低点比前一天高低点多出的幅度，用ATR计
    '''
    pinzhong = 'pp'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    df = pd.read_csv(r'..\data\{}.csv'.format(pinzhong))

    df = get_ma(df, 5)
    df['ma短'] = df.ma
    df = get_ma(df, 20)
    df['ma长'] = df.ma

    df = get_atr(df, 50)

    df['h比值'] = df.h-df.h.shift(1)
    df['l比值'] = df.l-df.l.shift(1)

    df['高价超出幅度'] = np.where(df['h比值']>=0, df['h比值'], None)
    df['高价超出幅度'] = df['高价超出幅度'] / df.atr.shift(1)
    df = df.dropna()
    print(df['高价超出幅度'].mean())
    print(df['高价超出幅度'].quantile(0.8))

    #df['低价超出幅度'] = np.where(df['l比值']<=0, df['l比值'], None)
    #df['低价超出幅度'] = df['低价超出幅度'] / df.atr.shift(1)
    #df = df.dropna()
    #print(df['低价超出幅度'].mean())
    #print(df['低价超出幅度'].quantile(0.8)) 
       
    df.to_csv('tmp.csv')
#foo5()