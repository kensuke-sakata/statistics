#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import sys
from scipy import stats
import matplotlib.pyplot as plt
#import numpy as np
#import os 
#import csv

def helpargv():
    """help command line
    """
    if len(sys.argv)==7:
        pass
    else:
        print("Usage: python statisticstest.py <file_name> <category#> <[category]> <category-check> <parameter#> <analysis(0:histgram,1:parametric,2;non-parametric)>")
        sys.exit()

def histgram2d(list,xlabel,ylabel):
    """Shapiro-Wilk normality test and create 2D-histgram
    """
    print(stats.shapiro(list))
    df[xlabel].plot.hist()
    #plt.title(pname, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(False) 
    print('***See histgram and confirm nomarity!***')
    
def parametoric(data,category,ylabel):
    """t-test and MN±SD
    """
    print(stats.ttest_ind(list(data[0]),list(data[1]),equal_var=False))
    #print(f'- {ylabel} in {category[0]} MN±SD: {np.mean(parameter[0])} ± {np.std(parameter[0],ddof=1)}')
    print('-',ylabel,'in',category[0],'MN±SD:',data[0].mean(),'±',data[0].std(ddof=1))          
    #print('-',ylabel,'in',category[1],'MN±SD:',np.mean(parameter[1]),'±',np.std(parameter[1],ddof=1))
    print('-',ylabel,'in',category[1],'MN±SD:',data[1].mean(),'±',data[1].std(ddof=1))      

def bargraph(data,category,xlabel,ylabel):
    """create bar graph
    """
    #plt.bar([0,1],[np.mean(parameter[0]),np.mean(parameter[1])],color="#FF5B70",width=0.6,edgecolor="#CC4959",linewidth=1,yerr=[np.std(parameter[0],ddof=1),np.std(parameter[1],ddof=1)],ecolor="black",capsize=10)
    plt.bar([0,1],[data[0].mean(),data[1].mean()],color="#FF5B70",width=0.6,edgecolor="#CC4959",linewidth=1,yerr=[data[0].std(ddof=1),data[1].std(ddof=1)],ecolor="black",capsize=10)
    plt.xticks([0,1],[category[0],category[1]],fontsize=12)
    #plt.title(ylabel,fontsize=12)
    plt.xlabel(xlabel,fontsize=12)
    plt.ylabel(ylabel,fontsize=12)
    plt.grid(which="major",axis="y",color = "gray",alpha=0.2,linewidth=1,linestyle="-")    
   
def nonparametoric(data,category,ylabel):
    """Mann-Whitney U test (default alternative is two-sided) and MDN(Q1-Q3)
    """
    print(stats.mannwhitneyu(list(data[0]),list(data[1]),alternative='two-sided',nan_policy='omit',method='asymptotic',use_continuity=True))
    #print(f'- {ylabel} in {category[0]} MDN(Q1-Q3): {np.percentile(parameter[0],50)}({np.percentile(parameter[0],25)} - {np.percentile(parameter[0],75)})')
    print(f'- {ylabel} in {category[0]} MDN(Q1-Q3): {data[0].quantile(0.5)}({data[0].quantile(0.25)} - {data[0].quantile(0.75)})')
    #print('-',ylabel,'in',category[1],'MDN(Q1-Q3):',np.percentile(parameter[1],50),'(',np.percentile(parameter[1],25),'-',np.percentile(parameter[1],75),')')
    print(f'- {ylabel} in {category[1]} MDN(Q1-Q3): {data[1].quantile(0.5)}({data[1].quantile(0.25)} - {data[1].quantile(0.75)})')

def boxwhisker(data,category,xlabel,ylabel):
    """create box-and-whisker plot
    """
    #plt.boxplot([parameter[0],parameter[1]],labels=[category[0],category[1]],widths=[0.5,0.5])
    plt.boxplot([list(data[0]),list(data[1])],labels=[category[0],category[1]],widths=[0.5,0.5])
    #plt.title(titlename, fontsize=12)
    plt.xlabel(xlabel,fontsize=12)
    plt.ylabel(ylabel,fontsize=12)
    plt.grid(which="major",axis="y",color = "gray",alpha=0.2,linewidth=1,linestyle="-")

helpargv()

# manual input
df = pd.read_csv(sys.argv[1],sep='\t',index_col=None)
# assign and define index name
index = df.columns.values[:]
cname = index[int(sys.argv[2])]
category = sys.argv[3].split(',')
# check category
if int(sys.argv[4])==1:    
    # replace 0/1 instead of A/B, male/female, or something
    df[cname] = df[cname].map({category[0]:0,category[1]:1})
elif int(sys.argv[4])==0:
    pass
else:
    print('categorization error!')
# read and separate columns as category 0/1
# parameter = [list(df.loc[df[cname]==0,index[int(sys.argv[3])]]), list(df.loc[df[cname]==1,index[int(sys.argv[3])]])]
data = [df.loc[df[cname]==0,index[int(sys.argv[5])]], df.loc[df[cname]==1,index[int(sys.argv[5])]]]
#print(df,index,data,sep="\n")

if 0<=int(sys.argv[6])<=2:
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    histgram2d(list(df.iloc[:,int(sys.argv[5])]),index[int(sys.argv[5])],'Frequency')
else:
    print('command line error!')
    
if int(sys.argv[6])==1:
    parametoric(data,category,index[int(sys.argv[5])])       
    plt.subplot(1, 2, 2)
    bargraph(data,category,cname,index[int(sys.argv[5])])
elif int(sys.argv[6])==2:   
    nonparametoric(data,category,index[int(sys.argv[5])])
    plt.subplot(1, 2, 2)
    boxwhisker(data,category,cname,index[int(sys.argv[5])])
else:
    pass

# show graph
plt.show()





    
## show results on listbox
#listbox1.insert(tk.END,"p=%.5f" %(result.pvalue))