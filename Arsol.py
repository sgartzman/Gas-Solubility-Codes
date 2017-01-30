# -*- coding: utf-8 -*-
"""
    Gas Solubility Package for Python
        Version 1.0 Feb 16, 2016
        Author:  Brice Loose, Graduate School of Oceanography, URI.
        Email: bloose@uri.edu

    Many of the functions included here were ported from Roberta Hamme's
    Matlab Solubility functions. Roberta Hamme (rhamme@uvic.ca)
    
    % Arsol   Solubility of Ar in sea water
    %=========================================================================
    % Arsol Version 1.2 4/4/2005
    %          Author: Roberta C. Hamme (Scripps Inst of Oceanography)
    %
    % USAGE:  concAr = Arsol(S,T)
    %
    % DESCRIPTION:
    %    Solubility (saturation) of argon (Ar) in sea water
    %    at 1-atm pressure of air including saturated water vapor
    %
    % INPUT:  (if S and T are not singular they must have same dimensions)
    %   S = salinity    [PSS]
    %   T = temperature [degree C]
    %
    % OUTPUT:
    %   concAr = solubility of Ar  [umol/kg] 
    % 
    % AUTHOR:  Roberta Hamme (rhamme@ucsd.edu)
    %
    % REFERENCE:
    %    Roberta Hamme and Steve Emerson, 2004.
    %    "The solubility of neon, nitrogen and argon in distilled water and seawater."
    %    Deep-Sea Research I, 51(11), p. 1517-1528.
    %
    % DISCLAIMER:
    %    This software is provided "as is" without warranty of any kind.  
    %=========================================================================

"""
def Arsol(S, T):

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
        print "Arsol: S & T must have same dimensions or be singular"
        return

    #------
    # BEGIN
    #------
    
    # convert T to scaled temperature
    temp_S = np.log(np.subtract(298.15,T) / np.add(273.15,T))
    
    # constants from Table 4 of Hamme and Emerson 2004
    A0_ar = 2.79150
    A1_ar = 3.17609
    A2_ar = 4.13116
    A3_ar = 4.90379
    B0_ar = -6.96233e-3
    B1_ar = -7.66670e-3
    B2_ar = -1.16888e-2

    # Eqn (1) of Hamme and Emerson 2004
    conc_Ar = np.exp(A0_ar + A1_ar * temp_S + A2_ar * np.power(temp_S,2) + A3_ar*np.power(temp_S,3) + S * (B0_ar + B1_ar * temp_S + B2_ar * np.power(temp_S,2)))

    return conc_Ar

    