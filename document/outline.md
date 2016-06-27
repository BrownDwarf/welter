# Outline

Below is the outline for the paper.  This is a fusion between Greg's outline and my outline.

- **Introduction**

	- Pre main-sequence HR diagram spread in age/mass
	- Magnetic field and convection
	- Spots as a possible solution e.g., Stauffer Pleaides, recent Covey, Somers
	- Previous studies/techniques of Starspots
	- Motication for LkCa4- biased selection as proof-of-concept, no disk
- **Methodology**
	- Simple description of two major changes to C15, point to detailed appendix
- **Observations**
	- IGRINS spectroscopy
	- ESPaDOnS archival
	- Photometry
		- ASASSN
		- Grankin
	- Where in the phase of variability were the spectra taken?
	- **Table 1-** Dates and inferred V
	- **Figure 1** Overview of 17 seasons of photometry with observing epochs
	- **Figure 2** Phase-folded 17 seasons plus observing epochs
- **Results from spectral fitting**
	- Result from single-temperature fitting
	- **Figure 3** Teff vs. Wavelength for single temp
	- Result from two-temperature fitting
	- **Figure 4** Joint-plot of Teff2 vs Fill Factor
	- **Figure 5** Teff as a function of order (i.e. wavelength)
- **Confirmation of results from other methods**
	- Reproduce colors, photometry
		 -- Common sense of large covering fraction
	- Reproduce TiO variability
	- Reproduce low-res broadband spectra
- **Discussion/Implications**
	- Interpretation of distribution of stellar properties
	- Longitudinal/latitudinal spot distributions and phase
	- Address limitations of assumptions made in Methodology section


- **Appendix**

- **Methodological Details**
	- Full-spectrum fitting framework
		- Motivation for sampling- the questions we want to answer
		- Uncertain stellar parameters can be marginalized out
		- Overview and summary of existing model
	- Tradeoffs in wavelength coverage and number of stellar components.
		- Approach 11: Whole spectrum with a single-component (Czekala et al. 2015)
			- Bad model for *all* the data, doomed to have a bad fit.
		- Approach 12: Order-by-order with a single-component
			- Teff would vary with wavelength
		- Approach 21: Whole spectrum with two components
			- Curse of dimensionality + tuning parameters
		- Approach 22: Order-by-order with two components
			- What we actually did
		- FIGURE: Flux ratio of photospheric components- Phoenix, BB.	 
	- Implementation
		- FIGURE: New PGM(s)
		- FIGURE: Mixture model spectrum



# Plot Summary

1. Grankin and ASASSN photometric overview
2. ASAS-SN rotation, long-term consistency, precession
3. Single Temperature Fit Results: Teff vs. Wavelength
4. Two-temperature fit plots:
   - Triangle plot for one order
   - Teff2 vs fill factor for all orders
   - Example spectra, data compared to model, cherry picked regions
5. Confirmation of results  
	- Synthetic SED versus photometry  
	- Colors versus rotation phase (V-R vs. V)
  - TiO variability?
  - Low-res spectral convolution
6.  HR diagram


# Table Summary

Table:
---------

1. Estimated V photometry from phased light-curve analysis
2. Teff vs. spectral order for all orders
3. Final (best fit) Results:  v sin i, RV, T1, T2, A2, Av, L, M, age, etc....
