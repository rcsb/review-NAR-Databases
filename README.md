# Review Nucleic Acid Research (NAR) publications of databases for PDB-releated databases
The program searches database publication at NAR to find any database that uses PDB data. The program look for PDB keywords in the summary and abstract of each database published at NAR and measure PDB relation in three tiers:
* Tier 1 uses PDB data
* Tier 2 likely uses PDB data
* Tier 3 may use PDB data

The results searve as a guide for next-step manual review

## How to run the program
The scripts are to be run in 3 steps:
### Step 1: Find all databases to be searched.
Run p1_parse_main.py to parse databases from [NAR database summary](http://www.oxfordjournals.org/our_journals/nar/database/cap/), plus the category, the summary page etc. Give output file "p1_db_summary.tsv" of tabular form of databases' name, summary link, category, subcategory.
### Step 2: Review summary pages of each database:
Run p21_process_all_db_summary.py, look for PDB keywords. Give output file "p2_db_summary_review.tsv" of tabular form of db name, categories, db url, year, abstract url, length description, keywords t1/t2/t3.
### Step 3: Review abstract of each database:
Run p31_process_all_nar_abstract.py, look for PDB keywords and test accessibility of the url of each database. Give output file "p3_db_abstract_review.tsv" of tabular form of db name, categories, db url, year, abstract url, length description, keywords t1/t2/t3, and database url accessibility. 
### Notes:
Other python scripts such as those state with "p0" are utility scripts. 
