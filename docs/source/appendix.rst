Appendix
========

We detail the descriptions to each column of the simulated output datasets on this page.

.. admonition:: Abbreviations

   **KO**, knockout; **SKO**, single knockout; **DKO**, double knockout; **%**, percentage;
   **GI**, genetic interaction; **std. dev.**, standard deviation.

Column descriptions of Simulated Datasets
-----------------------------------------

- **guide_id**: Unique guide ID by numerical order.
- **gene_pair_id**: Target gene-pair ID.
- **gene1_gene2_id**: ID of 1st target KO gene and 2nd target KO gene, separated by "_". Any combination with 0 indicates it is SKO. For example,"1_2" indicates we are knocking out gene-pair targeting gene#1 and gene#2; and "1_0" indicates we knockout out gene#1 only.
- **guide1_id**: ID of 1st target KO gene with corresponding guide, separated by "_".
- **guide2_id**: ID of 2st target KO gene with corresponding guide, separated by "_".
- **construct_id**: ID of constructs, containing information for both DKO gene and guide; 1st and 2nd KO target are separated by "__". For example,"1_2__6_3" indicates a construct with 1st target on gene#1 and its second guide targeting it, combined with 2nd target on gene#6 and its third guide targeting it.
- **gene1**: ID of 1st target KO gene.
- **gene2**: ID of 2nd target KO gene.
- **guide1_eff**: Guide-Efficacy of the guide targeting 1st KO gene.
- **guide2_eff**: Guide-Efficacy of the guide targeting 2nd KO gene.
- **p1**: Theoretical phenotype of 1st KO gene.
- **p2**: Theoretical phenotype of 2nd KO gene.
- **p1i**: Theoretical phenotype of 1st KO gene, with GI effects.
- **p2i**: Theoretical phenotype of 2nd KO gene, with GI effects.
- **p1p**: Theoretical phenotype of 1st KO gene, with guide-efficacy effects.
- **p2p**: Theoretical phenotype of 2nd KO gene, with guide-efficacy effects.
- **p1ip**: Theoretical phenotype of 1st KO gene, with both GI and guide-efficacy effects.
- **p2ip**: Theoretical phenotype of 2nd KO gene, with both GI and guide-efficacy effects.
- **KO_type**: Knockout type, whether this construct is SKO or DKO.
- **gene1_behavior**: Gene class category for 1st KO gene.
- **gene2_behavior**: Gene class category for 2nd KO gene.
- **i_interaction**: Indicator for GI presence, 1 indicates there is GI, 0 indicates not.
- **interaction_gene**: Gene-level interaction values. (simulated GI truth)
- **interaction_guide**: Guide-level interaction values. (for records only, not practically used)
- **interaction_gene_type**: Category of GI on whether there is none, negative, or positive GI presence.
- **interaction_guide_type**: Category of GI on whether there is none, negative, or positive GI presence, on guide-level. (for records only, not practically used)
- **p0y_0**: Probability of cell with no division and dies, without considering GI effects.
- **p1y_0**: Probability of cell with 1 division, without considering GI effects.
- **p2y_0**: Probability of cell with 2 divisions, without considering GI effects.
- **p3y_0**: Probability of cell with 3 divisions, without considering GI effects.
- **p0y**: Probability of cell with no division and dies, with GI effects.
- **p1y**: Probability of cell with 1 division, with GI effects.
- **p2y**: Probability of cell with 2 divisions, with GI effects.
- **p3y**: Probability of cell with 3 divisions, with GI effects.
- **p0y_p0**: Probability of cell with no division and dies, with guide-efficacy effects but not GI.
- **p1y_p0**: Probability of cell with 1 division, with guide-efficacy effects but not GI.
- **p2y_p0**: Probability of cell with 2 divisions, with guide-efficacy effects but not GI.
- **p3y_p0**: Probability of cell with 3 divisions, with guide-efficacy effects but not GI.
- **p0y_p**: Probability of cell with no division and dies, with both GI and guide-efficacy effects.
- **p1y_p**: Probability of cell with 1 division, with both GI and guide-efficacy effects.
- **p2y_p**: Probability of cell with 2 divisions, with both GI and guide-efficacy effects.
- **p3y_p**: Probability of cell with 3 divisions, with both GI and guide-efficacy effects.
- **freq_t0**: Frequency of the target gene-pair at initial timepoint.
- **rel_freq_t0**: Relative abundance (frequency) of the target gene-pair at initial timepoint.
- **guide1_type**: Indicator on type of the guide for 1st KO gene. (1 indicates high-efficacy guides, 0 indicates low-efficacy guides).
- **guide2_type**: Indicator on type of the guide for 2nd KO gene. (1 indicates high-efficacy guides, 0 indicates low-efficacy guides).
- **freq_guide_t0**: Frequency of the construct at initial timepoint.
- **counts_guide_t0**: Counts of the construct at initial timepoint.
- **counts_guide_t1**: Counts of the construct at the intermediate stage of cell growth and selection.
- **rel_freq_guide_t0**: Relative abundance (frequency) of the construct at initial timepoint.
- **counts_guide_t2**: Counts of the construct at final timepoint.
- **rel_freq_guide_t2**: Relative abundance (frequency) of the construct at final timepoint.
- **LFC**: Log2-Fold-Change of relative abundance from the construct at final vs. initial timepoint.