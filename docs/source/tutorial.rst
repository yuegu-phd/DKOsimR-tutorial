DKOsimR Tutorial
================

How to generate synthetic CRISPR data using DKOsimR?

Introduction
------------

DKOsimR is an R package designed for generating synthetic CRISPR double-knockout
screening data. It allows researchers to simulate cell growth dynamics and
genetic interactions between gene pairs under controlled library setup and 
experimental conditions.

This tutorial demonstrates:

- list of tunable parameters
- default workflow for generating synthetic data
- simulation setup to approximate laboratory data patterns
- an example of applying genetic interaction (GI) detection method on simulated data
- guidance on picking suitable parameters

Installation
------------

To start running simulation, simply download and install R/RStudio as the first step. You may then install DKOsimR with following commands:

.. code-block:: r

   if(!requireNamespace("devtools", quietly = TRUE))
       install.packages("devtools")

   devtools::install_github("yuegu-phd/DKOsimR", quiet = TRUE)
   devtools::install(dependencies = TRUE)


Then you may simply load the package:

.. code-block:: r

   library(DKOsimR)
   

List of Tunable Parameters
--------------------------

Initialized Library Parameters:

Genetic Interaction (GI) Parameters:

- **p_gi** : proportion of interacting gene pairs
- **sd_gi** : std. dev. of re-sampled phenotype with GI presence

Gene Class Parameters:

1. Percentage (%) of theoretical phenotype to each gene class

   - **pt_neg**: % negative
   - **pt_pos**: % positive
   - **pt_wt**: % wild-type
   - **pt_ctrl**: % non-targeting control

2. Mean and std. dev. of theoretical phenotype

   - **mu_neg**: mean of negative genes
   - **sd_neg**: std. dev. of negative genes
   - **mu_pos**: mean of positive genes
   - **sd_pos**: std. dev. of positive genes
   - **sd_wt**: std. dev. of wild-type genes

Guide Parameters:

1. high-efficacy guides proportion and CRISPR mode

   - **p_high** : proportion of high-efficacy guides
   - **mode**: CRISPR mode:

      - use CRISPRn-100%Eff if need 100% effcient guides without randomization
      - use CRISPRn if need high-efficient guides drawn from distribution

2. Mean and std. dev. of guide-efficacy

   - **mu_high**: mean of high-efficacy guides
   - **sd_high**: std. dev of high-efficacy guides
   - **mu_low**: mean of low-efficacy guides
   - **sd_low**: std. dev of low-efficacy guides

Cell Doublings Parameters:

   - **size.bottleneck**: bottleneck size - threshold indicating the ceiling of cell growth
   - **n.bottlenecks**: number of bottleneck encounters - how many times do we encountering bottle-
necks?
   - **n.iterations**: number of maximum doubling cycles, by default, we assume a maximum of 30
doublings if we didn't encounter bottleneck

Randomization Parameter:

   - **rseed**: values used for random number generator - use same number to control same sets of genes
having GI

Miscellaneous:

   - **path**: path to directory to save outputs of data and logs from simulation
   - **cores_free**: number of cores that are left to be free in parallel computing


Running a Simulation
--------------------

Example simulation using default parameters.

.. code-block:: r

   dkosim(sample_name = "test", n = 40)

Output files will be generated in the working directory.

Simulation Approximating Laboratory Data
----------------------------------------

DKOsimR also provides a wrapper function to simulate data that resembles
observed CRISPR screening experiments.

.. code-block:: r

   dkosim_lab(sample_name = "test_lab", n = 20)

This function applies parameter settings that approximate realistic laboratory
data distributions.

Applying Genetic Interaction Detection Methods
-----------------------------------------------

Once simulated count data are generated, users can apply GI detection methods.

Example workflow using differential log-fold change (dLFC):

.. code-block:: r

   library(DKOsimR)

   data(example_data_repA)

   head(example_data_repA)

Users may apply several GI detection algorithms including:

- dLFC
- GEMINI
- CTG
- π-score

These methods evaluate interaction effects between gene pairs based on
log-fold changes observed in double knockout screens.

Choosing Suitable Parameters
----------------------------

Recommended parameter choices for typical simulations:

- **coverage** : 100
- **n_guide_g** : 2 or 3
- **p_gi** : 0.03
- **p_high** : 1
- **moi** : ~0.3

These settings generally produce simulation outputs resembling realistic
CRISPR screening experiments.

Summary
-------

DKOsimR enables researchers to:

- generate reproducible synthetic CRISPR screening datasets
- benchmark genetic interaction detection methods
- evaluate experimental design parameters

For further information, please refer to the API documentation.