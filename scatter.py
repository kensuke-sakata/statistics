#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
import sys

def helpargv():
    """help command line
    """
    if len(sys.argv)==4:
        pass
    else:
        print("Usage: python statisticstest.py <file_name> <parameter#1> <parameter#2>")
        sys.exit()

def scatterplot(data,color1,color2):
    """create scatter diagram
    """
    plt.scatter(list(data[0]),list(data[2]),c=color1)
    plt.scatter(list(data[1]),list(data[3]),c=color2)
    plt.show()
    

helpargv()

# manual input
df = pd.read_csv(sys.argv[1],sep='\t',index_col=None)
# assign and define index name
index = df.columns.values[:]
cname = index[1]
category = ['A','B']
# replace 0/1 instead of A/B, male/female, or something
df[cname] = df[cname].map({category[0]:0,category[1]:1})
# read and separate columns as category 0/1
data = [df.loc[df[cname]==i%2,index[int(sys.argv[(i+4)//2])]] for i in range(4)]
# data = [df.loc[df[cname]==0,index[int(sys.argv[2])]],\
#         df.loc[df[cname]==1,index[int(sys.argv[2])]],\
#         df.loc[df[cname]==0,index[int(sys.argv[3])]],\
#         df.loc[df[cname]==1,index[int(sys.argv[3])]]]
print(data)

plt.figure(figsize=(10, 6))
scatterplot(data,'r','b')