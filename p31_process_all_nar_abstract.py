#!/usr/bin/env python
"""Parse all html abstract pages of individual DB
Use output from process p2
"""

from p30A_process_one_nar_abstract import processOneAbstract
from p30B_check_one_db_url import checkOneDB


def processAllDB(filepath_list):
    filename_out="p3_db_abstract_review.tsv"
    
    l_items = ['db', 'cats', 'url_summary', 'url_abstract', 'url_db', 'length_description', 'keywords_t1', 'keywords_t2', 'keywords_t3']
    l_db = []
    d_db = {}
    file = open(filepath_list)
    for line in file:
        l_line = line.strip("\n").split("\t")
        db = l_line[0]
        l_db.append(db)
        d_db[db] = {}
        for i in range(len(l_items)):
            d_db[db][l_items[i]] = l_line[i]
    file.close()
    ## l_db=["RCSB Protein Data Bank","PDB-Ligand"] # Test
    
    file=open(filename_out,'w')
    for db in l_db:
        d_db[db]['keywords_t1'] = d_db[db]['keywords_t1'].split(";")
        d_db[db]['keywords_t2'] = d_db[db]['keywords_t2'].split(";")
        d_db[db]['keywords_t3'] = d_db[db]['keywords_t3'].split(";")
        
        url_abstract = d_db[db]['url_abstract']
        url_db = d_db[db]['url_db']

        abstract = processOneAbstract(url_abstract)
        if abstract:
            (len_abstract, date, l_1, l_2, l_3) = abstract
            d_db[db]['len_abstract'] = len_abstract
            d_db[db]['date'] = date
            if l_1:
                d_db[db]['keywords_t1'].extend(l_1)
            if l_2:
                d_db[db]['keywords_t2'].extend(l_2)
            if l_3:
                d_db[db]['keywords_t3'].extend(l_3)
        else:
            d_db[db]['len_abstract'] = 0
            d_db[db]['date'] = 0
        
        code = checkOneDB(url_db)
        if code:
            d_db[db]['access'] = code
        else:
            d_db[db]['access'] = 0

        l_items_new = ['db', 'cats', 'url_summary', 'url_abstract', 'url_db', 'length_description', 'len_abstract', 'date', 'access']
        l_keywords = ['keywords_t1', 'keywords_t2', 'keywords_t3']

        l_line_new = []
        for item in l_items_new:
            l_line_new.append(str(d_db[db][item]))
        for keyword in l_keywords:
            keywords = ";".join(d_db[db][keyword])
            l_line_new.append(keywords)
        file.write("\t".join(l_line_new))
        file.write("\n")
    file.close()

def main():
    filepath_list = "p2_db_summary_review.tsv"
    processAllDB(filepath_list)

if __name__ == "__main__":
    main()

