
    #Gas Solubility Package for R
    #    Version 1.0 Feb 16, 2016
    #    Author:  Christiane Uhlig, Graduate School of Oceanography, URI.
    #    Email: cuhlig@uri.edu
    #
    # ch4_solubility   Solubility of Methane in sea water
	
    #=========================================================================
    # - Calculate solubility (Bunsen Coefficient) of methane in sea water.
	# Inputs: 
	#   T: temperature in degress celsius
	#   S: salinity in PSU
	#	# Output:
	# bunsen.coeff: bunsen coefficient at given T and S in vol/vol
    #
    #
    #- SOURCE:  Yamamoto, S. et al. (1976) Solubility of Methane in Distilled 
    #- Water and Seawater, Journal of Chemical Engineering Data, Vol. 21(1).
    # DISCLAIMER:
    #    This software is provided "as is" without warranty of any kind.  
    #=========================================================================


bunsen <- function(T, S){
  
  A1 <- -67.1962
  A2 <- 99.1624
  A3 <- 27.9015
  B1 <- -0.072909
  B2 <- 0.041674
  B3 <- -0.0064603
  
  T.K <- temp + 273.15
  
  bunsen.coeff.L.L.x <- exp(A1 + A2*(100/T.K) + A3*(log(T.K/100)) + S*(B1 + B2*(T.K/100) + B3*((T.K/100)^2)))
      
  bunsen.coeff.L.L <- c(bunsen.coeff.L.L.x)
    
  return(bunsen.coeff)
}

# bunsen.coeff <- bunsen(0, 34.8)
# bunsen.coeff
