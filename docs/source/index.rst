Welcome to DKOsimR Documentation!
=================================

**DKOsimR** is an R package for running Double-CRISPR Knockout Simulation (DKOsim). 
DKOsim is a simulation framework designed to simulate growth-based dual knockout CRISPR screens. 
It allows users and investigators to efficiently reproduce synthetic data where both the single gene fitness effect and the interaction of gene pairs can be pre-specified.

Quick start
------------

This page introduces DKOsimR package for generating synthetic CRISPR double knockout data. See :doc:`Tutorial <tutorial>` for a quickstart on installation and run simulations. A vignettes file
of DKOsimR is available in the R package, and a pre-built output preview (PDF) can be downloaded :download:`here <files/DKOsimR_vignettes.pdf>`.

For more details to tune and customize your CRISPR simulation, check :doc:`Running Simulation <run_sim>` and :doc:`Laboratory Data Approximation <lab_approx>`.

:doc:`Applying GI Detection Methods on Simulated Data <dlfc_apply>` provides a quick guide and example on how to apply GI detection method on simulated output data, and how to visualize the results.

Finally, we supply the :doc:`Appendix <appendix>` for columns description of the simulated dataset.

.. admonition:: Paper References

   Gu, Y., Hart, T. Leon-Novelo, L., & Shen, J.P. (2025). **Double-CRISPR Knockout Simulation (DKOsim): 
   A Monte-Carlo Randomization System to Model Cell Growth Behavior 
   and Infer the Optimal Library Design for Growth-Based Double Knockout Screens.**
   *Under Revision*. https://doi.org/10.1101/2025.09.11.675497

   Shen, J., Zhao, D., Sasik, R. et al (2017). **Combinatorial CRISPR-Cas9 screens for de novo mapping 
   of genetic interactions.** 
   *Nature Methods* 14, 573-576 (2017). https://doi.org/10.1038/nmeth.4225


.. note::

   The simulation and documentations are under active development. 


.. toctree::
   :maxdepth: 2
   :caption: Contents

   tutorial
   run_sim
   lab_approx
   dlfc_apply
   summary_guide
   appendix

