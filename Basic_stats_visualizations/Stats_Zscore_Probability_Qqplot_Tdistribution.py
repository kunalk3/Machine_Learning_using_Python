#---------------------------------------------------------------------
# File Name   : Association_apriori.py
# Author      : Kunal K.
# Description : Implementing Stats with Z score, prob, t distribution (basics)
# Date:       : 5 Nov. 2020
# Version     : V1.0
# Ref No      : DS_Code_P_K07
#---------------------------------------------------------------------

# Importing necessary libraries
import pandas as pd

# importing data set using pandas
mba = pd.read_csv("mba.csv")


# Finding mean,median,mode
mba['gmat'].mean() # mba.gmat.mean()
mba['gmat'].median()
mba['gmat'].mode()
mba['gmat'].var()
mba['gmat'].std()

# variance & Standard Deviation for Sample
mba['gmat'].var() # 860
mba['gmat'].std() # 29.39

# Variacne & Standard Deviation for Population
import numpy as np
np.var(mba['gmat']) # 859.70
np.std(mba['gmat']) # 29.32


# calculating the range value 
range = max(mba['gmat'])-min(mba['gmat']) # max(mba.gmat)-min(mba.gmat)
range

# calculating the population standard deviation and variance 
np.var(mba.gmat) # population variance 
np.std(mba.gmat)  # population standard deviation


import scipy.stats as stats
# ppf => Percent point function 
stats.norm.ppf(0.975,0,1)# similar to qnorm in R

# cdf => cumulative distributive function 
stats.norm.cdf(740,711,29) # similar to pnorm in R 

# cummulative distribution function
help(stats.norm.cdf)
#Q-Q plot

import pylab          
import scipy.stats as st

# Checking Whether data is normally distributed
stats.probplot(mba['gmat'], dist="norm",plot=pylab)

stats.probplot(mba.workex,dist="norm",plot=pylab)

mtcars = pd.read_csv("mtcars.csv")

st.probplot(mtcars.mpg,dist="norm",plot=pylab)
help(st.probplot)


# t distribution 

# Finding qnorm,qt  for 90%,95%,99% confidence level

import scipy.stats as stats
# percentage point function 
stats.norm.ppf(0.975,0,1)# similar to qnorm in R
stats.norm.ppf(0.995,0,1)
stats.norm.ppf(0.950,0,1)
stats.t.ppf(0.975, 139) # similar to qt in R
stats.t.ppf(0.995,139)
stats.t.ppf(0.950,139)
help(stats.t.ppf) 
