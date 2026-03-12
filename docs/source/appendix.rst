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
- **gene1_gene2_id**: ID of 1st target KO gene and 2nd target KO gene, separated by “_“. Any combination with 0 indicates it is SKO. For example,”1_2” indicates we are knocking out gene-pair targeting gene#1 and gene#2; and “1_0” indicates we knockout out gene#1 only.
- **guide1_id**: ID of 1st target KO gene with corresponding guide, separated by “_“.
- **guide2_id**: ID of 2st target KO gene with corresponding guide, separated by “_“.
- **construct_id**: ID of constructs, containing information for both DKO gene and guide; 1st and 2nd KO target are separated by “__“. For example,”1_2__6_3” indicates a construct with 1st target on gene#1 and its second guide targeting it, combined with 2nd target on gene#6 and its third guide targeting it.
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