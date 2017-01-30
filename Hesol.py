# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.0 Feb 16, 2016
        Author:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    Many of the functions included here were ported from Roberta Hamme's
    Matlab Solubility functions. Roberta Hamme (rhamme@uvic.ca)
    
    #=========================================================================
    # Hesol   Solubility of He in sea water
    #=========================================================================
    # Hesol Version 1.0 4/4/2005
    #          Author: Roberta C. Hamme (Scripps Inst of Oceanography)
    #
    # USAGE:  concHe = Hesol(S,T)
    #
    # DESCRIPTION:
    #    Solubility (saturation) of helium (He) in sea water 
    #    at 1-atm pressure of air including saturated water vapor
    #
    # INPUT:  (if S and T are not singular they must have same dimensions)
    #   S = salinity    [PSS]
    #   T = temperature [degree C]
    #
    # OUTPUT:
    #   concHe = solubility of He  [umol/kg] 
    # 
    # AUTHOR:  Roberta Hamme (rhamme@ucsd.edu)
    #
    # REFERENCE:
    #    Ray F. Weiss (1971)
    #       "Solubility of Helium and Neon in Water and Seawater"
    #       Journal of Chemical and Engineering Data, 16(2), 235-241.
    #
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================
"""


def Hesol(S, T):

    import numpy as np

    #----------------------
    # Check input parameters
    #----------------------
    #Python Takes care of this...

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
        print "Hesol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------

    # convert T to scaled temperature
    temp_abs = np.add(T,273.15)

    A1_helium = -167.2178
    A2_helium = 216.3442
    A3_helium = 139.2032
    A4_helium = -22.6202
    B1_helium = -0.044781
    B2_helium = 0.023541
    B3_helium = -0.0034266

    # Eqn (2) of Weiss and Kyser
    conc_He = np.exp(A1_helium + (A2_helium * 100. / temp_abs) + (A3_helium * np.log(temp_abs / 100)) + (A4_helium * temp_abs / 100) + S*(B1_helium + (B2_helium * temp_abs / 100) + (B3_helium * np.power((temp_abs/ 100),2))))

    # Convert concentration from mL/kg to umol/kg
    # Molar volume at STP is calculated from Dymond and Smith (1980) "The virial coefficients of pure gases and mixtures", Clarendon Press, Oxford.
    conc_He = conc_He / 22.44257e-3

    return conc_He

    