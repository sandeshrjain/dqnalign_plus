# dqnalign_plus
Modified DQNAlign algorithm and related experiments 

 **# Sequence Data for HEV Family and Escherichia coli Strains**

**This repository contains sequence data for HEV family and Escherichia coli strains.**

## Contents

* **Sequence Types**
    * **Short:** 47 genome sequences from the HEV family (listed in `hev_gen_table.txt`)
    * **Long:** 2 genome sequences from Escherichia coli strains
* **Data Access**
    * **Short Sequences:** 
        * Accession numbers listed in `hev_gen_table.txt`
        * Python script to pull sequences from NCBI: `hev_fill_txt.py`
    * **Long Sequences:**
        * Direct links to NCBI:
            * Escherichia coli O157:H7 str. TW14359: [https://www.ncbi.nlm.nih.gov/nuccore/NC_013008.1?report=fasta](https://www.ncbi.nlm.nih.gov/nuccore/NC_013008.1?report=fasta)
            * Escherichia coli str. K-12 substr. MG1655: [https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3?report=fasta](https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3?report=fasta)

## Usage

1. **Obtain Short Sequences:**
    * Run the Python script `hev_fill_txt.py` to download sequences from NCBI using the accession numbers in `hev_gen_table.txt`.
2. **Access Long Sequences:** 
    * Follow the direct links provided above to access the FASTA files from NCBI.

## Additional Information

* **Source:** NCBI Nucleotide Database ([https://www.ncbi.nlm.nih.gov/nuccore/](https://www.ncbi.nlm.nih.gov/nuccore/))
* **Python Script:** ncbi_accessor.py (requires installation of Biopython library)

**Please note:** 

* The files in this repository do not contain the actual sequence data but rather provide instructions and links to access them.
