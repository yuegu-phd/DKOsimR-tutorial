Laboratory Data Pattern Approximation
=====================================

To utilize the simulation framework in approximating actual laboratory data pattern, ``dkosim_lab`` was
designed to include three initialized gene class. You may specify the percentage of essential genes by `pt_neg`,
unknown by `pt_unknown`, and non-targeting controls by `pt_ctrl` accordingly. In our designed framework,
essential genes is defined by negative genes; unknown genes might compose of genes with theoretical phenotype
in either negative, positive, wild-type, or non-targeting control gene class.


.. admonition:: Abbreviations

   **KO**, knockout; **SKO**, single knockout; **DKO**, double knockout; **%**, percentage;
   **GI**, genetic interaction; **std. dev.**, standard deviation.

Default Lab Mode
----------------

By default, ``dkosim_lab`` run simulation with following parameter:

Initialized Library Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **coverage**: 100
- **n_guide_g**: 3
- **moi**: 0.3
- **sd_freq0**: 1/2.56 (chosen by setting a 10-fold difference between 90th and 10th percentiles of SKO counts distribution)

GI Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **p_gi** : 0.03
- **sd_gi** : 1.5

Gene Class Parameters
~~~~~~~~~~~~~~~~~~~~~

% of theoretical phenotype to each gene class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **pt_neg**: 0.15
   - **pt_unknown**: 0.80
   - **pt_ctrl**: 0.05

Mean and std. dev. of theoretical phenotype
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **mu_neg**: -0.03
   - **sd_neg**: 0.25
   - **sd_unknown**: 0.25

Guide Parameters
~~~~~~~~~~~~~~~~

High-efficacy guides proportion and CRISPR mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   - **p_high** : 0.75
   - **mode**: `CRISPRn`

Mean and std. dev. of guide-efficacy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

An example running code is as follows:

.. code-block:: R

   dkosim_lab(sample_name="test_lab", n=20)

Customized Lab Mode
-------------------

Alternatively, you may adjust values to any tunable parameters as desired, or using the parameters described 
in the full article to approximate actual lab data pattern in double CRISPR screens. For example, use the following code and 
parameters to simulate Fong-2024 :cite:p:`fong2024multilineage` laboratory screens:

.. code-block:: R

   dkosim_lab(sample_name="sim_fong2024",
              n = 246,
              coverage=1000,
              n_guide_g=3,
              moi = 0.3,
              sd_freq0 = 1/2.56,
              p_gi=0.03,
              sd_gi=1.5,
              pt_neg=64/246,
              pt_unknown=178/246,
              pt_ctrl=4/246,
              mu_neg=-0.03,
              sd_neg=0.25,
              sd_unknown=0.2,
              p_high = 0.75,
              mode="CRISPRn",
              mu_high=0.9,
              sd_high=0.1,
              mu_low=0.05,
              sd_low=0.07,
              size.bottleneck = 2,
              n.bottlenecks= 1,
              n.iterations = 30)

Check more details in the full article and example output in the pre-built DKOsimR vignettes (:download:`PDF <files/DKOsimR_vignettes.pdf>`) Section 5.

References
----------

.. bibliography::
