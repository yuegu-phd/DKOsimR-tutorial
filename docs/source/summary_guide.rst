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

% of theoretical phenotype to each gene class - make sure the add up to 1
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

   - **p_high**: 1 by default, set from 0.75 to 0.8 to resemble real lab data.
   - **mode**: CRISPR mode:

      - use `CRISPRn-100%Eff` if need 100% efficient guides without randomization (theoretical case), ensure `p_high` is 1 when using this mode (default mode)
      - use `CRISPRn` if need high-efficacy guides drawn from distribution (practical case for actual lab setting)

Mean and std. dev. of guide-efficacy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **mu_high**: keep unchanged with default value of 0.9.
   - **sd_high**: keep unchanged with default value of 0.1.
   - **mu_low**: keep unchanged with default value of 0.05.
   - **sd_low**: keep unchanged with default value 0.07.

Cell Doublings Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~

   - **size.bottleneck**: 2 would be sufficient for most cases. Set it with values of at least 2 to let the simulated cells have chance to grow before reaching the first bottleneck.
   - **n.bottlenecks**: 1 by default would be sufficient for most cases. This value directly represents the number of passaging, considering use 2 or 3 if want more passages, but might dramatically decrease the cell population diversity as a result.
   - **n.iterations**: keep unchanged with default value of 30.

Randomization Parameter
~~~~~~~~~~~~~~~~~~~~~~~

   - **rseed**: use a same number to control same sets of genes having GI.

Miscellaneous
~~~~~~~~~~~~~

   - **path**: keep default or change to path to your project folder.
   - **cores_free**: keep default for shortest running time, but increase the number to avoid hard coding issues.

Suggestions on laboratory data approximation
--------------------------------------------

**To approximate patterns from actual laboratory DKO screens.** We suggest using ``dkosim_lab()`` by inputting 
the same number of genes in each gene class as the laboratory settings. A case example in mimicking 
Fong-2024 A549[1] has been described in the second major results section of DKOsim article[2]. Here, 
we provide a list of input parameters for DKOsim (mimicking Fong-2024 A549). Empirically, it took 
around 2 hours to finish running this approximation with 14 cores enabled for parallel computing.

Codes for the mimicking are provided below:

.. code-block:: r

   dkosim_lab(sample_name="DKOsimR_246x3x3_1000x_mFong_run1",
              coverage=1000,
              n=246,
              n_guide_g=3,
              sd_freq0 = 1/2.56,
              moi = 0.3,
              p_gi=0.03,
              sd_gi=1.5,
              pt_neg=64/246,
              pt_unknown=178/246,
              pt_ctrl=4/246,
              mu_neg=-0.03,
              sd_neg=0.25,
              sd_unknown=0.2,
              p_high=0.75,
              mode="CRISPRn",
              mu_high=0.9,
              sd_high=0.1,
              mu_low=0.05,
              sd_low=0.07,
              size.bottleneck = 2,
              n.bottlenecks= 1,
              n.iterations = 30)

Check relevant descriptions in the pre-built DKOsimR vignettes (:download:`PDF <files/DKOsimR_vignettes.pdf>`) Section 7.

References
----------

[1] Fong, S.H., Kuenzi, B.M., Mattson, N.M. et al. A multilineage screen identifies actionable synthetic lethal interactions in human cancers. Nat Genet 57, 154–164 (2025). https://doi.org/10.1038/s41588-024-01971-9.
[2] Gu, Y., Hart, T. Leon-Novelo, L., & Shen, J.P. (2025). Double-CRISPR Knockout Simulation (DKOsim): A Monte-Carlo Randomization System to Model Cell Growth Behavior and Infer the Optimal Library Design for Growth-Based Double Knockout Screens. Under Revision. https://doi.org/10.1101/2025.09.11.675497.