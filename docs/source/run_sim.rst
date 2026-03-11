Running Simulation
==================

.. admonition:: Abbreviations

   **KO**, knockout; **SKO**, single knockout; **DKO**, double knockout; **%**, percentage;
   **GI**, genetic interaction; **std. dev.**, standard deviation.

To generate synthetic double knockout data, **by default, the simulated datasets would be stored
under data/ in the current directory, use ``getwd()`` to navigate your current working directory.**
The default values for parameters of simulated CRISPR screens are set based on empirical assumptions as
follows:

Default Values of Tunable Parameters
------------------------------------

Initialized Library Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **coverage**: 100
- **n_guide_g**: 3
- **moi**: 0.3
- **sd_freq0**: 1/3.29 (chosen by setting a 10-fold di"erence between 95th and 5th percentiles of SKO
counts distribution)

Genetic Interaction (GI) Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **p_gi** : 0.03
- **sd_gi** : 1.5

Gene Class Parameters
~~~~~~~~~~~~~~~~~~~~~

1. % of theoretical phenotype to each gene class

   - **pt_neg**: 0.15
   - **pt_pos**: 0.05
   - **pt_wt**: 0.75
   - **pt_ctrl**: 0.05

2. Mean and std. dev. of theoretical phenotype

   - **mu_neg**: -0.75
   - **sd_neg**: 0.1
   - **mu_pos**: 0.75
   - **sd_pos**: 0.1
   - **sd_wt**: 0.25

Guide Parameters
~~~~~~~~~~~~~~~~

1. high-efficacy guides proportion and CRISPR mode

   - **p_high** : 1
   - **mode**: `CRISPRn-100%Eff`

2. Mean and std. dev. of guide-efficacy

   - **mu_high**: 0.9
   - **sd_high**: 0.1
   - **mu_low**: 0.05
   - **sd_low**: 0.07

Cell Doublings Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

   - **size.bottleneck**: 2
   - **n.bottlenecks**: 1
   - **n.iterations**: 30

Randomization Parameter
~~~~~~~~~~~~~~~~~~~~~~~

   - **rseed**: NULL

Miscellaneous
~~~~~~~~~~~~~

   - **path**: current working directory
   - **cores_free**: 1

Run Simulation by Default
-------------------------

To run simulation by default, simply name your simulation by sample_name and specify the number of single
genes by n. Be cautious that number of genes in each gene class should be an integer to optimize
simulation run. A quick Simulation Settings Summary would be returned for each run. Additionally,
number of cores used for parallel computing, Run Time in unit of hours would be collected after one successful
run. An example running code is as follows:

.. code-block:: r

   dkosim(sample_name = "test", n = 40)


Run Customized Simulation
-------------------------

Alternatively, you may adjust values to any tunable parameters as desired, but please make sure your input
on percentage of each gene class add up to 1 for all classes, and each initialized number of genes is an
integer. **You may also change the output directory using path in the function; by default, the
output simulated data and log is under the same directory of current project workspace.** The
randomization seed can also be specified by rseed to ensure same subsets of gene-pairs has GI in multiple
run.

An example running code is

.. code-block:: r

   dkosim(sample_name="test",
          coverage=10,
          n=60,
          n_guide_g=2,
          sd_freq0 = 1/3.29,
          moi = 0.3,
          p_gi=0.03,
          sd_gi=1.5,
          pt_neg=0.15,
          pt_pos=0.05,
          pt_wt=0.75,
          pt_ctrl=0.05,
          mu_neg=-0.75,
          sd_neg=0.1,
          mu_pos=0.75,
          sd_pos=0.1,
          sd_wt=0.25,
          p_high=0.8,
          mode="CRISPRn",
          mu_high=0.8,
          sd_high=0.2,
          mu_low=0.1,
          sd_low=0.08,
          size.bottleneck = 3,
          n.bottlenecks= 2,
          n.iterations = 30,
          rseed = 111,
          path = ".",
          cores_free = 2)

