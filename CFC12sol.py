#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Gas Solubility Package for Python
        Version 1.0 Feb 6, 2017
        Author:  Samuel Gartzman, Graduate School of Oceanography, URI.
        Email: sgartzman@uri.edu

    #=========================================================================
    # CFC12sol   Solubility of CFC-12 in sea water
    #=========================================================================         
    # USAGE:  concCFC12 = CFC12sol(S,T, Moist)
    #
    # DESCRIPTION:
    #    Solubility (saturation) of Dichlorodifluoromethane (CFC-12) in sea water 
    #    at 1-atm pressure of air including saturated water vapor
    #
    # INPUT:  (if S and T are not singular they must have same dimensions)
    #   S = salinity    [PSS]
    #   T = temperature [degree C]
    #   Moist = Boolean. If True, concCFC12 will include moist air.
    #
    # OUTPUT:
    #   concCFC12 = solubility of CFC-12  [umol/Kg]
    # 
    #
    # REFERENCE:
    #Warner, M. J. and Weiss, R.F.
    #Solubilities of Chlorofluorocarbons 11 and 12 in Watter and Seawater,
    #DEEP-SEA RES., 1985, Vol32, 1485-1497.
    #
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================
"""

def CFC12sol(S, T, Moist):

    import numpy as np

    #----------------------
    # Check input parameters
    #----------------------

    # CHECK S,T dimensions and verify consistent
    if np.size(np.shape(T))>1:
        mt,nt=np.shape(T)
    else:
        mt = np.size(T)
        nt = 0
    if np.size(np.shape(S))>1:
        ms,ns=np.shape(S)
    else:
        ms = np.size(S)
        ns = 0

    # Check that T&S have the same shape or are singular
    if (ms != mt) or (ns != nt):
        print "CFC12sol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    # convert T to scaled temperature
    T = np.add(T,273.15)
    
    if Moist == True:
        a1 = -220.2120000
        a2 = 301.8695000
        a3 = 114.8533000
        a4 = -1.3916500
    
        b1 = -0.1477180
        b2 = 0.0931750
        b3 = -0.0157340
    
        lnC = a1 + a2*(100/T) + a3*np.log(T/100) + a4*np.power((T/100),2) + S*(b1 + b2*(T/100) + (b3*np.power((T/100),2)))
    elif Moist == False:
        a1 = -124.4395
        a2 = 185.4299
        a3 = 51.6383
    
        b1 = -0.149779
        b2 = 0.094668
        b3 = -0.0160043
    
        lnC = a1 + a2*(100/T) + a3*np.log(T/100) + (S*(b1 + b2*(T/100) + b3*np.power((T/100),2)))

    sol = np.exp(lnC)
    return sol
