#!/usr/bin/env python
"""Parse html of individual DB abstract page
"""

from p0_read_html import read_html, read_html_file
from p0_re_pdb_keywords import re_1, re_2, re_3
from p0_html_parsers import AbstractParser, TitleParser, DateParser
from p20_process_one_db_summary import find_match

def processOneAbstract(url_abstract):
    if not url_abstract.strip():
        return ()
    s_html = read_html(url_abstract)

    parser3 = AbstractParser()
    parser3.feed(s_html)
    abstract = parser3.abstract.strip()
    len_abstract = len(abstract)

    parser4 = TitleParser()
    parser4.feed(s_html)
    title = parser4.title.strip()
    text = title + " " + abstract

    parser5 = DateParser()
    parser5.feed(s_html)
    date = parser5.date

    l_1 = []
    l_2 = []
    l_3 = []
    if text.strip():
        l_1 = find_match(re_1, text)
        l_2 = find_match(re_2, text)
        l_3 = find_match(re_3, text)
    return (len_abstract, date, l_1, l_2, l_3)

def main():
    url_abstract = "https://academic.oup.com/nar/article-lookup/43/D1/D369"
    (len_abstract, date, l_1, l_2, l_3)=processOneAbstract(url_abstract)
    print len_abstract, date, l_1, l_2, l_3
    ## url_abstract = ""
    ## processOneAbstract(url_abstract)
    ## url_abstract = "https://academic.oup.com/nar/article-lookup/45/D1/D737"
    ## processOneAbstract(url_abstract)
    ## url_abstract = "https://academic.oup.com/nar/article-lookup/37/suppl_1/D118"
    ## processOneAbstract(url_abstract)

if __name__ == "__main__":
    main()
