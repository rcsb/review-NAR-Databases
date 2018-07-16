#!/usr/bin/env python
"""Regular Expression patterns of PDB keywords.
"""

import re

#1st tier
re_1 = []
re_1.append(re.compile(r'(protein data bank)', re.IGNORECASE))
re_1.append(re.compile(r'(nucleic acid database)', re.IGNORECASE))

#2nd tier
re_2 = []
re_2.append(re.compile(r'\b(pdb)\b', re.IGNORECASE))
re_2.append(re.compile(r'\b(wwpdb)\b', re.IGNORECASE))
re_2.append(re.compile(r'\b(rcsb)\b', re.IGNORECASE))
re_2.append(re.compile(r'\b(pdbe)\b', re.IGNORECASE))
re_2.append(re.compile(r'\b(pdbj)\b', re.IGNORECASE))
re_2.append(re.compile(r'\b(ndb)\b', re.IGNORECASE))

#3rd tier
re_3 = []
re_3.append(re.compile(r'(protein) (databank|database|data base)', re.IGNORECASE))  #alternate name of PDB
re_3.append(re.compile(r'(nucleic acid) (data bank|databank|data base)', re.IGNORECASE))  #alternate name of NDB
re_3.append(re.compile(r'\b(bmrb)\b', re.IGNORECASE)) #BMRB
re_3.append(re.compile(r'(coordinates)', re.IGNORECASE))
re_3.append(re.compile(r'\b(3d|3-d|3 dimensional|3-dimensional|three dimensional|three-dimensional) (structure|structural|model|data|folding|analysis)', re.IGNORECASE))
re_3.append(re.compile(r'(structure|structural) (model|data|folding|analysis)', re.IGNORECASE))
re_3.append(re.compile(r'(protein|peptide|nucleic acid|molecule|molecular) (structure|structural|model|folding)', re.IGNORECASE))
re_3.append(re.compile(r'\b(x-ray|xray|crystal)', re.IGNORECASE))
re_3.append(re.compile(r'\b(nmr|nuclear magnetic resonance)\b', re.IGNORECASE))
re_3.append(re.compile(r'\b(em|electron microscope|electron microscopy)\b', re.IGNORECASE))

def main():
    test = """
    The Conserved Domain Database (CDD) is a compilation of multiple sequence alignments representing protein domains conserved in molecular evolution. It has been populated with alignment data from the public collections Pfam ( 1) and Smart ( 2), as well as with contributions from colleagues at NCBI. The current version of CDD (v1.53) contains 3551 such models. CDD alignments are linked to protein sequence and structure data in Entrez (3 ). The molecular structure viewer Cn3D (4 ) serves as a tool to interactively visualize alignments and three-dimensional structure, and to annotate three-dimensional residue coordinates with evolutionarily conserved features. CDD can be accessed on the world-wide-web at the URL http://www.ncbi.nlm.nih.gov/Structure/cdd/cdd.shtml. Protein query sequences may be compared against databases of position-specific score matrices (PSSMs) derived from alignments in CDD, using a service named CD-Search, which can be found at http://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi. CD-Search runs reverse position-specific BLAST (RPS-BLAST), a variant of the widely used PSI-BLAST algorithm ( 5). CD-Search is run by default for protein-protein queries submitted to NCBI's BLAST-service at http://www.ncbi.nlm.nih.gov/BLAST. 
    """
    for re_ in re_3:
        print re_
        if re_.search(test):
            print re_.search(test).groups()
            print " ".join(re_.search(test).groups())

if __name__ == "__main__":
    main()
