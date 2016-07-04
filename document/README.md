# Outline

Below is the outline for the paper.  This is a fusion between Greg's outline and my outline.

- **Introduction**

	- Pre main-sequence HR diagram spread in age/mass
	- Magnetic field and convection
	- Spots as a possible solution e.g., Stauffer Pleaides, recent Covey, Somers
	- Previous studies/techniques of Starspots
	- Motication for LkCa4- biased selection as proof-of-concept, no disk
- **Methodology**
	- :white_check_mark: Simple description of two major changes to C15, point to detailed appendix
- **Observations**
	- :white_check_mark: IGRINS spectroscopy
	- :white_check_mark: ESPaDOnS archival
	- :white_check_mark: Photometry
		- ASASSN
		- Grankin
	- :white_check_mark: Where in the phase of variability were the spectra taken?
	- :white_check_mark: **Table 1-** Dates and inferred V
	- :white_check_mark: **Figure 1** Overview of 17 seasons of photometry with observing epochs
	- :white_check_mark: **Figure 2** Phase-folded 17 seasons plus observing epochs
- **Results from spectral fitting**
	- :soon: Result from single-temperature fitting
	- :white_check_mark: **Figure 3** Teff vs. Wavelength for single temp
	- Result from two-temperature fitting
	- :white_check_mark: **Figure 4** Teff1, Teff 2 vs. Wavelength for two temp
	- :white_check_mark: **Figure 5** Joint-plot of Teff2 vs Fill Factor
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

1. :white_check_mark: Grankin and ASASSN photometric overview
2. :white_check_mark: ASAS-SN rotation, long-term consistency, precession
3. :white_check_mark: Single Temperature Fit Results: Teff vs. Wavelength
4. :white_check_mark: Two Temperature Fit Results: Teff1, Teff2 vs Wavelength
5. :white_check_mark: Teff2 vs fill factor for all orders
6. Example spectra, data compared to model in cherry picked regions
7. :white_check_mark: Synthetic SED versus flux-calibrated spectra
8. :white_check_mark: TiO variability
9. Colors versus rotation phase (V-R vs. V)
10. :grey_question: Low-res spectral convolution
11.  HR diagram
12. :white_check_mark: All the spectra, one panel per order


# Table Summary

Table:
---------

1. :white_check_mark: Estimated V photometry from phased light-curve analysis
2. :white_check_mark: Teff vs. spectral order for all orders
3. Final (best fit) Results:  v sin i, RV, T1, T2, A2, Av, L, M, age, etc....
