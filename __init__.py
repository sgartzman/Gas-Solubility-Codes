# -*- coding: utf-8 -*-
"""
Gas Solubility Package for Python
    Version 1.0 Feb 16, 2016
    Author:  Brice Loose, Graduate School of Oceanography, URI.
    Email: bloose@uri.edu
    #
    # USAGE:  import Solubility as S
    #         S.Hesol(33,0) gives solubility at S = 33, T = 0  
    #
    #
    # 
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind. 
    #    Many of the functions included here were ported from Roberta Hamme's
    #    Matlab Solubility functions. Roberta Hamme (rhamme@ucsd.edu)
    #=========================================================================      
"""

#import numpy as np
from .Hesol import *
from .Arsol import *
from .O2sol import *
from .ch4_solubility import *  
  
__all__ = ['Hesol','Arsol','O2sol','ch4_solubility']