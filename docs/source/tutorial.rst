DKOsimR Tutorial
================

How to generate synthetic CRISPR data using DKOsimR?

Introduction
------------

DKOsimR is an R package designed for generating synthetic CRISPR double-knockout
screening data. It allows researchers to simulate cell growth dynamics and
genetic interactions between gene pairs under controlled experimental conditions.

This tutorial demonstrates:

- the list of tunable parameters
- default workflow for generating synthetic data
- simulation approximating laboratory data patterns
- an example genetic interaction (GI) detection workflow
- guidance on choosing suitable parameters

Installation
------------

Install DKOsimR from GitHub.

.. code-block:: r

   if(!requireNamespace("devtools", quietly = TRUE))
       install.packages("devtools")

   devtools::install_github("yuegu-phd/DKOsimR", quiet = TRUE)

   library(DKOsimR)

List of Tunable Parameters
--------------------------

Key parameters controlling DKOsim simulation include:

- **sample_name** : name of simulation run
- **coverage** : cell representation per guide
- **n** : number of unique single genes
- **n_guide_g** : number of guides per gene
- **moi** : multiplicity of infection
- **sd_freq0** : dispersion of initial counts distribution
- **p_gi** : proportion of interacting gene pairs
- **p_high** : proportion of high-efficacy guides
- **n_e** : number of passages
- **n_b** : bottleneck size

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