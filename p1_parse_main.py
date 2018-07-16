#!/usr/bin/env python
"""Parse the summary page of all published NAR databases at
http://www.oxfordjournals.org/our_journals/nar/database/cap/
Output file contains database name, each individual database's summary url, and category name
"""

from p0_html_parsers import LinkParser
from p0_read_html import read_html, read_html_file
import re

def get_db_list():
    ## url of overall summary, url header of individual DB, and output file are hard-coded here.
    url = "http://www.oxfordjournals.org/our_journals/nar/database/cap/"
    url_header = "http://www.oxfordjournals.org/our_journals"
    filename_out="p1_db_summary.tsv"
    
    s_html = read_html(url)
    ## html_file = "nar.html"
    ## s_html = read_html_file(html_file)
    
    parser = LinkParser()
    parser.feed(s_html)

    re_cat = re.compile(r'/nar/database/cat/(\d{1,2})')
    re_subcat = re.compile(r'/nar/database/subcat/(\d{1,2})/(\d{1,2})')
    re_summary = re.compile(r'/nar/database/summary/(\d+)')
    
    d_cat = {}
    for url, name in parser.links:
        if re_cat.search(url):
            cat_name = name.strip()
            index_cat = re_cat.search(url).groups()[0]
            d_cat[index_cat] = {}
            d_cat[index_cat][0] = cat_name
        if re_subcat.search(url):
            cat_name = name.strip()
            index_cat = re_subcat.search(url).groups()[0]
            index_subcat = re_subcat.search(url).groups()[1]
            d_cat[index_cat][index_subcat] = cat_name

    l_db = []
    d_db = {}
    index_current_cat = -1
    index_current_subcat = -1
    for url, name in parser.links:
        if re_cat.search(url):
            index_current_cat = re_cat.search(url).groups()[0]
            index_current_subcat = -1
        if re_subcat.search(url):
            index_current_subcat = re_subcat.search(url).groups()[1]

        if re_summary.search(url):
            db = name.strip()
            l_db.append(db)
            d_db[db] = {}
            d_db[db]['url'] = url_header + url
            d_db[db]['cat'] = d_cat[index_current_cat][0]
            if index_current_subcat > 0:
                d_db[db]['subcat'] = d_cat[index_current_cat][index_current_subcat]
            else:
                d_db[db]['subcat'] = ''

    file=open(filename_out,'w')
    for db in l_db:
        l_line = [db, d_db[db]['url'], d_db[db]['cat'], d_db[db]['subcat']]
        file.write("\t".join(l_line))
        file.write("\n")
    file.close()

def main():
    get_db_list()
         
if __name__ == "__main__":
    main()

