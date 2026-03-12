Summary Guidance in Picking Suitable Parameters
===============================================

In this section, from empirical DKO simulation runs, we provide a summary guidance on picking suitable
parameters to run your simulated CRISPR screens in practice. **Please note that this section is mainly for
a general suggestion to pick hyperparameters that could efficiently run simulations in practice,
adjust the choice of parameters based on your desires and purpose when using DKOsimR, and
check reference article for more detailed info.** 

.. admonition:: Abbreviations

   **KO**, knockout; **SKO**, single knockout; **DKO**, double knockout; **%**, percentage;
   **GI**, genetic interaction; **std. dev.**, standard deviation.

How should I choose parameters?
------------------------------------

Following the :ref:`list of tunable parameters <list-parameters>`:

Initialized Library Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **sample_name**: name simulation with number of genes, number of guides per gene, number of initialized gene classes, and coverage, seperated by “_“. For example, ”DKOsimR_120x3x4_100x_run1” indicates the 1st run for DKO simulation run with 120 genes, 3 guides per genes, and all 4 initialized gene classes (negative, wild-type, positive, non-targeting control), with 100x coverage.
- **coverage**: 100 would be sufficient for most cases, set lower to shorten running time but simulated data might have weaker reproducibility.
- **n**: put the number of unique single gene by desire. 100 would be sufficient for most cases.
- **n_guide_g**: set as 2 or 3.
- **moi**: keep unchanged. Default value is 0.3.
- **sd_freq0**: 1/3.29 by default, chosen by setting a 10-fold difference between 95th and 5th percentiles of SKO counts distribution. Set to 1/2.56, 1/2.07, 1/1.68, 1/1.35, 1/1.05, if you want a 10-fold difference between 90th and 10th, 85th and 15th, 80th and 20th, 75th and 25th, 70th and 30th percentiles, respectively.

GI Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **p_gi**: 0.03 by default, chosen by empirical assumption on the presence of GI in real lab that are close to 3%. Can be tuned higher if want higher presence of GIs.
- **sd_gi**: 1.5 by default and would be sufficient for most cases. This directly affects GI magnitude, and can be tuned lower for smaller GI magnitude.

Gene Class Parameters
~~~~~~~~~~~~~~~~~~~~~

Percentage (%) of theoretical phenotype to each gene class - make sure the add up to 1
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **pt_neg**: set to values from 0.15 to 0.3 as desired.
   - **pt_pos**: set to values from 0 to 0.05 as desired.
   - **pt_wt**: set to values from 0.7 to 0.9 as desired.
   - **pt_ctrl**: set to values from 0.05 to 0.1 as desired.

Mean and std. dev. of theoretical phenotype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **mu_neg**: set to values from -0.01 to -0.8 as desired.
   - **sd_neg**: set to values from 0.1 to 0.5 as desired.
   - **mu_pos**: set to values from 0.01 to 0.8 as desired.
   - **sd_pos**: set to values from 0.1 to 0.5 as desired.
   - **sd_wt**: set to values from 0.1 to 0.5 as desired.

Guide Parameters
~~~~~~~~~~~~~~~~

High-efficacy guides proportion and CRISPR mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **p_high** : proportion of high-efficacy guides
   - **mode**: CRISPR mode:

      - use CRISPRn-100%Eff if need 100% effcient guides without randomization
      - use CRISPRn if need high-efficient guides drawn from distribution

Mean and std. dev. of guide-efficacy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **mu_high**: mean of high-efficacy guides
   - **sd_high**: std. dev of high-efficacy guides
   - **mu_low**: mean of low-efficacy guides
   - **sd_low**: std. dev of low-efficacy guides

Cell Doublings Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

   - **size.bottleneck**: bottleneck size - threshold indicating the ceiling of cell growth
   - **n.bottlenecks**: number of bottleneck encounters - how many times do we encountering bottlenecks?
   - **n.iterations**: number of maximum doubling cycles, by default, we assume a maximum of 30 doublings if we didn't encounter bottleneck

Randomization Parameter
~~~~~~~~~~~~~~~~~~~~~~~

   - **rseed**: values used for random number generator - use same number to control same sets of genes having GI

Miscellaneous
~~~~~~~~~~~~~

   - **path**: path to directory to save outputs of data and logs from simulation
   - **cores_free**: number of cores that are left to be free in parallel computing

Run Simulation by Default
-------------------------

To run simulation by default, simply name your simulation by sample_name and specify the number of single
genes by `n`. **Be cautious that number of genes in each gene class should be an integer to optimize
simulation run.** A quick Simulation Settings Summary would be returned for each run. Additionally,
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

Check example output in the pre-built DKOsimR vignettes (:download:`PDF <files/DKOsimR_vignettes.pdf>`) Section 4.