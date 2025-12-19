[![Paper](https://img.shields.io/badge/paper-arXiv%3AXXXX.YYYYY-B31B1B.svg)](https://arxiv.org/abs/XXXX.YYYYY)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://zenodo.org/badge/latestdoi/XXXXYYYYY)

# Paper Title

Author 1, Author 2, Author 3

[arXiv:XXXX.YYYYY](https://arxiv.org/abs/XXXX.YYYYY)

### Abstract
Physical properties and functionalities of materials are dictated by global crystal structures as well as local defects. To establish a structure-property relationship, not only the crystallographic symmetry but also quantitative knowledge about defects are required. Here we present a hybrid Machine Learning (ML) framework that integrates a physically-constrained variational autoencoder (pc-VAE) with different Bayesian Optimization (BO) methods to systematically accelerate and improve crystal structure refinement with resolution of defects. We chose the pyrochlore structured Ho$_2$Ti$_2$O$_7$ as a model system and employed GSAS-II package for benchmarking crystallographic parameters from Rietveld refinement and for training data generation. However, the function space of these material systems are highly non-linear, which can limit the performance of the optimizer such as traditional Reitveld refinement to get trapped at local regions. Also, these naive methods do not provide an extensive learning about the overall function space which is essential for large space, large time consuming explorations to identify various potential regions of interest. Thus, we present the approach of exploring the high-D structure parameters of defect-sensitive systems via pretrained physically constrained variational autoencoder (pc-VAE) assisted Bayesian optimization (BO) and Sparse Axis Aligned Bayesian Optimization (SAASBO). The pc-VAE,designed and trained on physically plausible Ho$_2$Ti$_2$O$_7$ structure models, projects high-D diffraction data consisting of thousands of independently measured diffraction orders into a low-D latent space while enforcing scaling invariance and physical relevance of the latent space. In this proposed design of closed-loop autonomous exploration, we aim to minimize the chi-square errors (chisq), also known as L2 norm, in the real and latent spaces separately between experimental and simulated diffraction patterns, thereby steering the refinement towards potential optimum in the parameter space of crystal structures. We investigated and compared the results among different methods such as pc-VAE assisted BO, non pc-VAE assisted BO, and Rietveld refinement. The result shows that the methodology can be generaled to other complex materials where ultra-precise determination of structural defects is needed to reveal subtle structure–property relationships, highlighting a new paradigm for integrating crystallography with machine learning to accelerate discoveries and characterizations of magnetic materials.

### Description
This repository includes links, code, scripts, and data to generate the figures in a paper.

### Requirements
The data in this project was generated via ...  Processed data is included in the [data](https://github.com/DelMaestroGroup/papers-code-template/tree/main/data) directory and the full raw simulation data set is available online at [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXXX)

1. A minimal environment to execute these notebooks can be installed via `pip install -r requirements.txt`
2. [Dependency Name](https://dependencelink)
3. ...

### Support


The creation of these materials was <mark>primarily/partially</mark> supported by the National Science Foundation Materials Research Science and Engineering Center program through the UT Knoxville Center for Advanced Materials and Manufacturing [DMR-2309083](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2309083&HistoricalAwards=false).

<img width="400px" src="https://mrsec.org/sites/default/files/MRSEC%20logo_clear%20background.png">


### Figures

#### Figure 01: Figure Name
<img src="https://github.com/CAMM-UTK/papers-code-template/blob/main/figures/figure01.svg" width="400px">

This figure is relesed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) and can be freely copied, redistributed and remixed.

