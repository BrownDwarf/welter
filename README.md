# welter
#### Inferring starspot properties in the IGRINS spectrum of LkCa 4

[![arXiv status](https://img.shields.io/badge/arXiv-to%20appear%20Jan%2023rd-orange.svg)](https://arxiv.org/archive/astro-ph/Astrophysics)
[![Talk Slides](https://img.shields.io/badge/talk%20slides-Speakerdeck-brightgreen.svg)](https://speakerdeck.com/gully/measuring-fundamental-properties-of-young-stars)

In this project we extended the **[Starfish spectral inference framework](http://iancze.github.io/Starfish/)** to include an emission spectrum arising from **starspots** or starspot groups.  We successfully detected spectral features attributable to both hot and cool portions of the stellar photosphere.

![LkCa 4 starspot violin plot](http://i.imgur.com/YcvDOjB.png)

This repository includes almost all of the configuration files, Jupyter notebooks, manuscript and figures with complete revision history, Issues, the pipeline-reduced IGRINS spectrum of LkCa 4, batch analysis files for configuring and running extended compute jobs on a server, deprecated attempts at spectral inference with multiple orders, selected posterior MCMC chains, and other miscellaneous files used in the production of the scientific paper.  

*With that said*, the layout and documentation is limited, and not all data files are public, so making good use of this repo will require non-negligible data forensics and experimentation.

## Paper Authors

+ **[Michael Gully-Santiago](https://gully.github.io/) (Kavli Institute for Astronomy and Astrophysics)**
+ [Gregory J. Herczeg](http://kiaa.pku.edu.cn/faculty/gregory-j-herczeg) (Kavli Institute for Astronomy and Astrophysics)
+ [Ian Czekala](https://iancze.github.io/) (KIPAC, Stanford)
+ [Garrett Somers](http://www.astronomy.ohio-state.edu/~somers/) (Vanderbilt)
+ [Konstantin Grankin](http://stars.craocrimea.ru/index.php?option=com_content&view=article&id=89&Itemid=190&lang=en) (Crimean Astrophysical Observatory)
+ [Kevin Covey](http://myweb.facstaff.wwu.edu/~coveyk/) (Western Washington)
+ [J.F Donati](http://www.ast.obs-mip.fr/article454.html) (CNRS / Toulouse)
+ Silvia Alencar (ICEx UFMG, Brazil)
+ [Gaitee Hussain](http://www.eso.org/~ghussain/) (ESO / Toulouse)
+ [Benjamin Shappee](https://users.obs.carnegiescience.edu/bshappee/) (Carnegie)
+ [Greg Mace](http://www.as.utexas.edu/astronomy/people/people.html?u=276) (UT Austin)
+ [Jae-Joon Lee](https://github.com/leejjoon) (KASI)
+ [T. Holoien](http://www.astronomy.ohio-state.edu/~tholoien/index.html) (OSU)
+ [Jessy Jose](http://kiaa.pku.edu.cn/people/jessy-jose) (Kavli Institute for Astronomy and Astrophysics)
+ [Chun-Fan Liu](http://www.asiaa.sinica.edu.tw/~cfliu/) (ASIAA)



## Dependencies:
To run portions of the Jupyter Notebooks you will probably need:

- python 3
- jupyter-notebook
- scipy
- numpy
- pandas
- seaborn
- aplpy
- Starfish
