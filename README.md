# STRIDE: Species Tree Root Inference from Gene Duplication Events


The correct interpretation of a phylogenetic tree is dependent on it being correctly rooted. STRIDE takes an unrooted species tree and a set of unrooted gene trees and identifies well-supported gene duplication events within the gene trees to infer the root of the species tree. 

A gene duplication event at the base of a clade of species is synapamorphic, and thus excludes the root of the species tree from that clade. STRIDE is a fast, effective, and outgroup-free method for species tree root inference from gene duplication events. On test datasets on a typical 4 core desktop it analysed 14,454 gene trees covering 47 species in ~25s.

Test datasets together with a script to run all the datasets can be downloaded from [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.581360.svg)](https://doi.org/10.5281/zenodo.581360). 

Usage:
`stride.py -s gene_to_species_conversion -S Species_tree.tre -d gene_trees/`
