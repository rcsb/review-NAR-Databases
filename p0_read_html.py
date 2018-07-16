#!/usr/bin/env python
"""Utitlity to read url or html file.
"""

import urllib2

def read_html(url):
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError, msg:
        print msg
        return ''
    else:
        s_html = response.read()
        response.close()
        return s_html


def read_html_file(html_file):
    response = open(html_file)
    s_html = response.read()
    response.close()
    return s_html


def main():
    url = "http://www.oxfordjournals.org/our_journals/nar/database/cap/"
    s_html = read_html(url)
    ## html_file = "nar.html"
    ## s_html = read_html_file(html_file)
    print s_html

if __name__ == "__main__":
    main()
