import mechanize
#import html2text
import re
import codecs
import os
from bs4 import BeautifulSoup

import lib.microbewiki as mwiki
import lib.wikipedia as wikiped


# check data dir
if not os.path.exists("dat"):
    os.makedirs("dat")

# browser
br = mechanize.Browser()

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)


org = "Escherichia coli"
doc_count = 0
print "Processing:", org

# searching
mwiki.open(br, org)
wikiped.open(br, org)

