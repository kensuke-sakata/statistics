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
    if len(sys.argv)==6:
        pass
    else:
        print("Usage: python statisticstest.py <file_name> <category_name> <category[0,1]]> <parameter_name> <analysis(0:histgram,1:parametric,2;non-parametric)>")
        sys.exit()

def histgram2d(df,xlabel,ylabel):
    """Shapiro-Wilk normality test and create 2D-histgram
    """
    print(stats.shapiro(list(df[xlabel])))
    df[xlabel].plot.hist()
    #plt.title(pname, fontsize=12)
    plt.xlabel(xlabel, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    plt.grid(False) 
    print('---See histgram and confirm nomarity!')
    
def parametoric(data,ylabel,group,xlabel):
    """t-test and MN±SD
    """
    print(stats.ttest_ind(list(data[0]),list(data[1]),equal_var=False))
    print('-',ylabel,'in',xlabel,group[0],': MN±SD =',data[0].mean(),'±',data[0].std(ddof=1))          
    print('-',ylabel,'in',xlabel,group[1],': MN±SD =',data[1].mean(),'±',data[1].std(ddof=1))
    #print(f'- {ylabel} in {group[0]}: MN±SD={np.mean(data[0])}±{np.std(data[0],ddof=1)}')      
    #print('-',ylabel,'in',group[1],'MN±SD:',np.mean(data[1]),'±',np.std(data[1],ddof=1))

def bargraph(data,ylabel,group,xlabel):
    """create bar graph
    """
    #plt.bar([0,1],[np.mean(data[0]),np.mean(data[1])],color="#FF5B70",width=0.6,edgecolor="#CC4959",linewidth=1,yerr=[np.std(data[0],ddof=1),np.std(data[1],ddof=1)],ecolor="black",capsize=10)
    plt.bar([0,1],[data[0].mean(),data[1].mean()],color="#FF5B70",width=0.6,edgecolor="#CC4959",linewidth=1,yerr=[data[0].std(ddof=1),data[1].std(ddof=1)],ecolor="black",capsize=10)
    plt.xticks([0,1],[group[0],group[1]],fontsize=12)
    #plt.title(ylabel,fontsize=12)
    plt.xlabel(xlabel,fontsize=12)
    plt.ylabel(ylabel,fontsize=12)
    plt.grid(which="major",axis="y",color = "gray",alpha=0.2,linewidth=1,linestyle="-")    
    
def nonparametoric(data,ylabel,group,xlabel):
    """Mann-Whitney U test (default alternative is two-sided) and MDN(Q1-Q3)
    """
    print(stats.mannwhitneyu(list(data[0]),list(data[1]),alternative='two-sided',nan_policy='omit',method='asymptotic',use_continuity=True))
    print(f'- {ylabel} in {xlabel}{group[0]}: MDN(Q1-Q3)={data[0].quantile(0.5)}({data[0].quantile(0.25)}-{data[0].quantile(0.75)})')
    print(f'- {ylabel} in {xlabel}{group[1]}: MDN(Q1-Q3)={data[1].quantile(0.5)}({data[1].quantile(0.25)}-{data[1].quantile(0.75)})')
    #print(f'- {ylabel} in {group[0]} MDN(Q1-Q3): {np.percentile(data[0],50)}({np.percentile(data[0],25)} - {np.percentile(data[0],75)})')
    #print('-',ylabel,'in',group[1],'MDN(Q1-Q3):',np.percentile(data[1],50),'(',np.percentile(data[1],25),'-',np.percentile(data[1],75),')')

def boxwhisker(data,ylabel,group,xlabel):
    """create box-and-whisker plot
    """
    #plt.boxplot([data[0],data[1]],labels=[group[0],group[1]],widths=[0.5,0.5])
    plt.boxplot([list(data[0]),list(data[1])],labels=[group[0],group[1]],widths=[0.5,0.5])
    #plt.title(titlename, fontsize=12)
    plt.xlabel(xlabel,fontsize=12)
    plt.ylabel(ylabel,fontsize=12)
    plt.grid(which="major",axis="y",color = "gray",alpha=0.2,linewidth=1,linestyle="-")

helpargv()

# manual input
df = pd.read_csv(sys.argv[1],sep='\t',index_col=None)
# assign and define index name
cname = sys.argv[2]
category = sys.argv[3].split(',')
pname = sys.argv[4]
# check category
if category != ['0','1']:    
    # replace 0/1 instead of A/B, male/female, or something
    df[cname] = df[cname].map({category[0]:0,category[1]:1})
elif category == ['0','1']:
    pass
else:
    print('categorization error!')
# read and separate columns as category 0/1
# parameter = [list(df.loc[df[cname]==0,index[int(sys.argv[3])]]), list(df.loc[df[cname]==1,index[int(sys.argv[3])]])]
parameter = [df.loc[df[cname]==0,pname], df.loc[df[cname]==1,pname]]
#print(parameter,cname,category,sep="\n")

if 0<=int(sys.argv[5])<=2:
    plt.figure(figsize=(10, 6))
    plt.subplot(1, 2, 1)
    histgram2d(df,pname,'Frequency')
    #histgram2d(list(df.iloc[:,df.columns.get_loc(pname)]),pname,'Frequency')
else:
    print('analysis error!')
    
if int(sys.argv[5])==1:
    parametoric(parameter,pname,category,cname)       
    plt.subplot(1, 2, 2)
    bargraph(parameter,pname,category,cname)
elif int(sys.argv[5])==2:   
    nonparametoric(parameter,pname,category,cname)
    plt.subplot(1, 2, 2)
    boxwhisker(parameter,pname,category,cname)
else:
    pass

# show graph
plt.show()





# OPTION 2

# def helpargv():
#     """help command line
#     """
#     if len(sys.argv)==7:
#         pass
#     else:
#         print("Usage: python statisticstest.py <file_name> <category_name> <[category]> <categorization(0:done,1:need)> <parameter#> <analysis(0:histgram,1:parametric,2;non-parametric)>")
#         sys.exit()

# helpargv()

# # manual input
# df = pd.read_csv(sys.argv[1],sep='\t',index_col=None)
# # assign and define index name
# index = df.columns.values[:]
# cname = index[int(sys.argv[2])]
# category = sys.argv[3].split(',')
# # check category
# if int(sys.argv[4])==1:    
#     # replace 0/1 instead of A/B, male/female, or something
#     df[cname] = df[cname].map({category[0]:0,category[1]:1})
# elif int(sys.argv[4])==0:
#     pass
# else:
#     print('categorization error!')
# # read and separate columns as category 0/1
# # parameter = [list(df.loc[df[cname]==0,index[int(sys.argv[3])]]), list(df.loc[df[cname]==1,index[int(sys.argv[3])]])]
# parameter = [df.loc[df[cname]==0,index[int(sys.argv[5])]], df.loc[df[cname]==1,index[int(sys.argv[5])]]]
# #print(df,index,data,sep="\n")

# if 0<=int(sys.argv[6])<=2:
#     plt.figure(figsize=(10, 6))
#     plt.subplot(1, 2, 1)
#     histgram2d(list(df.iloc[:,int(sys.argv[5])]),index[int(sys.argv[5])],'Frequency')
# else:
#     print('analysis error!')
    
# if int(sys.argv[6])==1:
#     parametoric(parameter,category,index[int(sys.argv[5])])       
#     plt.subplot(1, 2, 2)
#     bargraph(parameter,category,cname,index[int(sys.argv[5])])
# elif int(sys.argv[6])==2:   
#     nonparametoric(parameter,category,index[int(sys.argv[5])])
#     plt.subplot(1, 2, 2)
#     boxwhisker(parameter,category,cname,index[int(sys.argv[5])])
# else:
#     pass

# # show graph
# plt.show()






    
## show results on listbox
#listbox1.insert(tk.END,"p=%.5f" %(result.pvalue))