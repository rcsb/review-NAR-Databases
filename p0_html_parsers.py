#!/usr/bin/env python
"""Utility to parse html file.
Specially designed for parsing NAR pages.
"""

from sgmllib import SGMLParser
from p0_read_html import read_html, read_html_file
import re

class LinkParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.links = []
        self.currentLink = None
        self.currentLinkText = []

    def start_a(self, attrs):
        if self.currentLink != None:
            self.end_a()
        for attr, value in attrs:
            if attr == 'href':
                self.currentLink = value
                break
            if self.currentLink == None:
                self.currentLink = ''

    def handle_data(self, data):
        if self.currentLink != None:
            self.currentLinkText.append(data)

    def end_a(self):
        self.links.append([self.currentLink, "".join(self.currentLinkText)])
        self.currentLink = None
        self.currentLinkText = []


class DescriptionParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tf_summary = False
        self.tf_description_header = False
        self.tf_description_text = False
        self.l_data = []
        self.description = ''

    def start_h3(self, attrs):
        for attr, value in attrs:
            if attr == 'class' and value == 'summary':
                self.tf_summary = True
                break

    def end_h3(self):
        self.tf_summary = False

    def start_div(self, attrs):
        if self.tf_description_header:
            self.tf_description_text = True
            self.tf_description_header = False

    def end_div(self):
        self.tf_description_text = False
        if self.l_data:
            self.description = ' '.join(self.l_data)

    def handle_data(self, data):
        if self.tf_summary:
            if data.strip() == "Database Description":
                self.tf_description_header = True
        if self.tf_description_text:
            self.l_data.append(data)


class AbstractParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tf_h2 = False
        self.tf_p = False
        self.tf_abstract = False
        self.l_data = []
        self.abstract = ''

    def start_h2(self, attrs):
        self.tf_h2 = True
    
    def end_h2(self):
        self.tf_h2 = False

    def start_p(self, attrs):
        self.tf_p = True
    
    def end_p(self):
        self.tf_p = False
        if self.l_data:
            self.abstract = ' '.join(self.l_data)
            self.tf_abstract = False

    def handle_data(self, data):
        if self.tf_h2:
            if data.strip() == "Abstract":
                self.tf_abstract = True
        if self.tf_abstract and self.tf_p:
            self.l_data.append(data)

class TitleParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tf_title = False
        self.l_data = []
        self.title = ''

    def start_title(self, attrs):
        self.tf_title = True
    
    def end_title(self):
        self.tf_title = False
        if self.l_data:
            self.title = ' '.join(self.l_data)

    def handle_data(self, data):
        if self.tf_title:
            self.l_data.append(data)

class DateParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.tf_date = False
        self.l_data = []
        self.date = ''

    def start_div(self, attrs):
        for attr, value in attrs:
            if attr == 'class' and value == 'citation-date':
                self.tf_date = True
                break

    def end_div(self):
        self.tf_date = False
        if self.l_data:
            self.date = ' '.join(self.l_data)

    def handle_data(self, data):
        if self.tf_date:
            self.l_data.append(data)


def main():
    ## Test on local files
############################ parse main page
    ## url = "http://www.oxfordjournals.org/our_journals/nar/database/cap/"
    ## s_html = read_html(url)
    ## html_file = "nar.html"
    ## s_html = read_html_file(html_file)
    
    ## parser = LinkParser()
    ## parser.feed(s_html)
    ## for url, name in parser.links:
    ##     print url, name

############################ parse each db's description page
    ## html_file = "onedb2.html"
    ## s_html = read_html_file(html_file)
    ## re_http = re.compile(r'^\s*http')
    ## re_doi = re.compile(r'doi\.org')
    ## parser = LinkParser()
    ## parser.feed(s_html)
    ## for url, name in parser.links:
    ##     if name.strip().lower() == "abstract":
    ##         print url, name
    ##     if re_http.search(name) and not re_doi.search(name):
    ##         print url, name

    ## parser2 = DescriptionParser()
    ## parser2.feed(s_html)
    ## description = parser2.description
    ## print description
############################ parse each db's abstract page
    ## html_file = "abstract.html"
    ## s_html = read_html_file(html_file)
    ## parser3 = AbstractParser()
    ## parser3.feed(s_html)
    ## abstract = parser3.abstract
    ## print abstract
    
    ## html_file = "abstract.html"
    ## s_html = read_html_file(html_file)
    ## parser4 = TitleParser()
    ## parser4.feed(s_html)
    ## title = parser4.title
    ## print title
## Test on url
    url_abstract = "https://academic.oup.com/nar/article-lookup/43/D1/D369"
    s_html = read_html(url_abstract)
    parser = DateParser()
    parser.feed(s_html)
    print parser.date
         
if __name__ == "__main__":
    main()

## <div class="citation-date">27 November 2013</div>
