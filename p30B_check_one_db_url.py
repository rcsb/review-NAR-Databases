#!/usr/bin/env python
"""Check url of individual DB reported in NAR publication.
"""

import urllib

def checkOneDB(url_db):
    if not url_db.strip():
        return False
    try:
        code = urllib.urlopen(url_db).getcode()
    except IOError, msg:
        return False
    else:
        return code

def main():
    url_db = "http://ncbr.muni.cz/ValidatorDB"
    print url_db
    print checkOneDB(url_db)
    
    url_db = "http://www.idrtech.com/PDB-Ligand/"
    print url_db
    print checkOneDB(url_db)
    
    ## url_db = "http://fantom.gsc.riken.jp/"
    ## print url_db
    ## print processOneAbstract(url_db)
    
    ## url_db = "http://genesilico.pl/modomics/"
    ## print url_db
    ## print processOneAbstract(url_db)

if __name__ == "__main__":
    main()
