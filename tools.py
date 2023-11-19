#!/usr/bin/env python
# vim: noet:ts=4:sts=4:sw=4
from scipy import stats
import matplotlib.pyplot as plt

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
