#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pandas as pd
import matplotlib.pyplot as plt
#from tools import histgram2d, parametoric, bargraph, nonparametoric, boxwhisker
from .tools import histgram2d

def helpargv():
    """help command line
    """
    if len(sys.argv)==6:
        pass
    else:
        print("Usage: python stattest.py <file_name> <category_name> <category[0,1]]> <parameter_name> <analysis(0:histgram,1:parametric,2;non-parametric)>")
        sys.exit()

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