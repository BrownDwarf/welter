## Outline


- Introduction
	- Pre main-sequence HR diagram spread
	- Previous studies of Starspots
	- Previous studies of LkCa4
- Methodology
	- Full-spectrum fitting framework
		- Motivation for sampling- the questions we want to answer
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
		- Mixture model definitions
		- TABLE: Parameter definitions
		- FIGURE: New PGM(s)
		- FIGURE: Mixture model spectrum
- Observations
	- IGRINS spectroscopy
	- ESPaDOnS archival
	- Where in the phase of variability were the spectra taken?
- Results
	- Result 11
	- Result 12
	- Result 22
- Discussion
	- Interpretation of distribution of stellar properties
	- Longitudinal/latitudinal spot distributions and phase
	- Address limitations of assumptions made in Methodology section
- Appendix
	- Testing and tuning the mixture model

## Stretch goals

- Predicted limit for how small a signal we could detect
