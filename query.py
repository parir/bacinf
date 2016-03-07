import re
import codecs
import os
from bs4 import BeautifulSoup

import lib.microbewiki as mwiki
import lib.wikipedia as wikiped


# check data dir
if not os.path.exists("dat"):
    os.makedirs("dat")

org = "Escherichia_coli"
doc_count = 0
print("Processing:", org)

# searching
mwiki.open(org)
wikiped.open(org)
