[![Paper](https://img.shields.io/badge/paper-arXiv%3A2503.08735-B31B1B.svg)](https://arxiv.org/abs/XXXX)

# Physically-Constrained Autoencoder-Assisted Bayesian Optimization for Refinement of High-Dimensional Defect-Sensitive Single Crystalline Structure

**Joseph Oche Agada**, **Andrew McAninch**, *Haley Day*, *Yasemin Tanyu*, **Ewan McCombs**, Seyed M. Koohpayeh, Brian H. Toby, **Yishu Wang**, **Arpan Biswas**

-Authors in BOLD are corresponding authors and afflifated at UTK-CAMM.

-Authors in ITALICS were REU worked as Summer Intern at UTK-CAMM.

[arXiv:XXXX.YYYYY](https://arxiv.org/abs/XXXX.YYYYY)

### Abstract
Physical properties and functionalities of materials are dictated by global crystal structures as well as local defects. To establish a structure-property relationship, not only the crystallographic symmetry but also quantitative knowledge about defects are required. Here we present a hybrid Machine Learning (ML) framework that integrates a physically-constrained variational autoencoder (pc-VAE) with different Bayesian Optimization (BO) methods to systematically accelerate and improve crystal structure refinement with resolution of defects. We chose the pyrochlore structured Ho$_2$Ti$_2$O$_7$ as a model system and employed GSAS-II package for benchmarking crystallographic parameters from Rietveld refinement and for training data generation. However, the function space of these material systems are highly non-linear, which can limit the performance of the optimizer such as traditional Reitveld refinement to get trapped at local regions. Also, these naive methods do not provide an extensive learning about the overall function space which is essential for large space, large time consuming explorations to identify various potential regions of interest. Thus, we present the approach of exploring the high-D structure parameters of defect-sensitive systems via pretrained physically constrained variational autoencoder (pc-VAE) assisted Bayesian optimization (BO) and Sparse Axis Aligned Bayesian Optimization (SAASBO). The pc-VAE,designed and trained on physically plausible Ho$_2$Ti$_2$O$_7$ structure models, projects high-D diffraction data consisting of thousands of independently measured diffraction orders into a low-D latent space while enforcing scaling invariance and physical relevance of the latent space. In this proposed design of closed-loop autonomous exploration, we aim to minimize the chi-square errors (chisq), also known as L2 norm, in the real and latent spaces separately between experimental and simulated diffraction patterns, thereby steering the refinement towards potential optimum in the parameter space of crystal structures. We investigated and compared the results among different methods such as pc-VAE assisted BO, non pc-VAE assisted BO, and Rietveld refinement. The result shows that the methodology can be generaled to other complex materials where ultra-precise determination of structural defects is needed to reveal subtle structure–property relationships, highlighting a new paradigm for integrating crystallography with machine learning to accelerate discoveries and characterizations of magnetic materials.

<img width="912" height="652" alt="image" src="https://github.com/user-attachments/assets/de96fccc-336b-4e1a-a788-dbacef26007d" />

Proposed architecture of the pc-VAE assisted BO and SAASBO exploration for crystalline structure refinement of pyrochlore model Ho2Ti2O7. The yellow arrows are the additional steps for the pc-VAE BO while the green arrows are the steps for traditional BO. The orange arrows are the common steps for the BO and the pc-VAE-BO.

### Description
This repository includes links, code, scripts, and data to generate the figures in a paper. All the required installation and import of python packages are provided at the top of each notebooks. If you are using Colab, please !pip install the required packages first. 

### Data
Information on the dataset is provided in the main paper and notebook. The dataset used to train pcVAE and BO analysis are provided in **Data** folder [here](https://github.com/arpanbiswas52/Stitching_AFMimage/tree/main/data). 

### Support

This work (J.A) was supported by the University of Tennessee startup funding of A.B. The authors (J.A. and A.B.) acknowledge the use of facilities and instrumentation at the UT Knoxville Institute for Advanced Materials and Manufacturing (IAMM) and the Shull Wollan Center (SWC) supported in part by the National Science Foundation Materials Research Science and Engineering Center program through the UT Knoxville Center for Advanced Materials and Manufacturing [DMR-2309083](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2309083&HistoricalAwards=false). This research (Y.W and A.M) was partially supported by the National Science Foundation Materials Research Science and Engineering Center program through the UT Knoxville Center for Advanced Materials and Manufacturing [DMR-2309083](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2309083&HistoricalAwards=false). This work (H.D and Y.T) was performed during the Student Mentoring and Research Training (SMaRT) program, jointly supported by the U.S. Department of Energy's Office of Energy Efficiency and Renewable Energy (EERE) through award number DE-EE0009177 provided to the University of Tennessee-Oak Ridge Innovation Institute. This work (S.M.K.) was supported as part of the Institute for Quantum Matter, an Energy Frontier Research Center funded by the U.S. Department of Energy, Office of Science, Basic Energy Sciences under award no. DE-SC0019331. The collection of X-ray data was supported by Prof. Collin Broholm and was performed at the X-ray Crystallography Facility of Johns Hopkins University (JHU) under the help of Maxime A. Siegler. 

<img width="400px" src="https://mrsec.org/sites/default/files/MRSEC%20logo_clear%20background.png">



