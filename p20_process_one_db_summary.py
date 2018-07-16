#!/usr/bin/env python
"""Parse summary html of individual DB summary page
"""

from p0_read_html import read_html, read_html_file
from p0_re_pdb_keywords import re_1, re_2, re_3
from p0_html_parsers import LinkParser, DescriptionParser
import re

def find_match(re_n, text):
    l_ = []
    for re_ in re_n:
        re_result = re_.search(text)
        if re_result:
            match = " ".join(re_result.groups())
            if match not in l_:
                l_.append(match)
    return l_


def processOneSummary(url):
    d_summary = {}
    s_html = read_html(url)
    ## s_html = read_html_file(html_file)
    if not s_html.strip():
        return {}

    parser = LinkParser()
    parser.feed(s_html)
    re_http = re.compile(r'^\s*http')
    re_doi = re.compile(r'doi\.org')
    
    re_skip1 = re.compile(r'oup\.com')
    re_skip2 = re.compile(r'oxfordjournals\.org')
    re_skip3 = re.compile(r'oed\.com')
    re_skip4 = re.compile(r'ox\.ac\.uk')
    re_skip = [re_skip1, re_skip2, re_skip3, re_skip4]
   
    d_summary['url_abstract'] = ''
    d_summary['url_db'] = ''
    d_summary['length_description'] = ''
    d_summary['keywords_t1'] = []
    d_summary['keywords_t2'] = []
    d_summary['keywords_t3'] = []
    for url, name in parser.links:
        if name.strip().lower() == "abstract":
            d_summary['url_abstract'] = url
        elif re_http.search(name):
            if re_doi.search(name):
                if d_summary['url_abstract']:
                    pass
                else:
                    d_summary['url_abstract'] = url
            elif not d_summary['url_db']:
                for re_each in re_skip:
                    if re_each.search(url):
                        d_summary['url_db'] = ""
                        break
                else:
                    d_summary['url_db'] = url

    parser2 = DescriptionParser()
    parser2.feed(s_html)
    description = parser2.description
    d_summary['length_description'] = len(description.strip())
    d_summary['keywords_t1'] = find_match(re_1, description)
    d_summary['keywords_t2'] = find_match(re_2, description)
    d_summary['keywords_t3'] = find_match(re_3, description)

    return d_summary

def main():
    ## url = "http://www.oxfordjournals.org/our_journals/nar/database/summary/615"
    ## d_summary = processOneSummary(url)
    ## print d_summary
    ## url = "http://www.oxfordjournals.org/our_journals/nar/database/summary/456"
    ## d_summary = processOneSummary(url)
    ## print d_summary
    ## url = "http://www.oxfordjournals.org/our_journals/nar/database/summary/840"
    ## d_summary = processOneSummary(url)
    ## print d_summary
    url = "http://www.oxfordjournals.org/our_journals/nar/database/summary/1340"
    d_summary = processOneSummary(url)
    print d_summary
    
if __name__ == "__main__":
    main()
