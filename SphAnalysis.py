#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 01:11:25 2020

@author: dexter
"""


import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii
import pandas as pd
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches
import scipy as scipy
from scipy import stats

from astropy.table import Table, Column, MaskedColumn
import matplotlib.patches as mpatches


import SphRead as SRead

class AnalyticFunctions(object):
    """
    """
    def __init__(self,Re):
        self.Re = Re
        
        
    def sersic(mu_e,r_e,n):
        return None
    
    def exp():
        return None
    
    def broken_exp():
        return None

#%%    
class PlotProfile(AnalyticFunctions):
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
#%%
def 
#class 2Dplot(object)