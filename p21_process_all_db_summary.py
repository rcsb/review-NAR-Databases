#!/usr/bin/env python
"""Parse all html summary pages of individual DB.
Use output from process p1
"""

from p20_process_one_db_summary import processOneSummary

def readAllSummary(filepath_list):
    file = open(filepath_list)
    l_db = []
    d_db = {}
    for line in file:
        l_line = line.strip("\n").split("\t")
        [db, url_summary, cat, subcat] =  l_line

        if subcat.strip():
            cats = cat + "|" + subcat
        else:
            cats = cat
            
        if db not in l_db:
            l_db.append(db)
            d_db[db] = {}
            d_db[db]['url_summary'] = url_summary
            d_db[db]['cats'] = cats
        else:
            d_db[db]['cats'] += ";" + cats
    file.close()
    return (l_db, d_db)

def processAllSummary(filepath_list):
    filename_out="p2_db_summary_review.tsv"
    
    (l_db, d_db) = readAllSummary(filepath_list)
    ## l_db = ['ValidatorDB', 'PDB-Ligand', 'FANTOM', 'MODOMICS', 'EBI patent sequences'] ## For testing

    l_strs = ['cats', 'url_summary', 'url_abstract', 'url_db', 'length_description']
    l_keywords = ['keywords_t1', 'keywords_t2', 'keywords_t3']

    for db in l_db:
        url_summary = d_db[db]['url_summary']
        d_summary = processOneSummary(url_summary)
        if d_summary:
            d_db[db]['url_abstract'] = d_summary['url_abstract']
            d_db[db]['url_db'] = d_summary['url_db']
            d_db[db]['length_description'] = d_summary['length_description']
            d_db[db]['keywords_t1'] = d_summary['keywords_t1']
            d_db[db]['keywords_t2'] = d_summary['keywords_t2']
            d_db[db]['keywords_t3'] = d_summary['keywords_t3']
        else:
            d_db[db]['url_abstract'] = ''
            d_db[db]['url_db'] = ''
            d_db[db]['length_description'] = ''
            d_db[db]['keywords_t1'] = []
            d_db[db]['keywords_t2'] = []
            d_db[db]['keywords_t3'] = []

    file=open(filename_out,'w')
    for db in l_db:
        l_line = []
        l_line.append(db)
        for item in l_strs:
            l_line.append(str(d_db[db][item]))
        for keyword in l_keywords:
            keywords = ";".join(d_db[db][keyword])
            l_line.append(keywords)
        file.write("\t".join(l_line))
        file.write("\n")
    file.close()

def main():
    processAllSummary("p1_db_summary.tsv")

if __name__ == "__main__":
    main()
