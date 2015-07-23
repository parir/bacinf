import mechanize
#import html2text
import re
import codecs
import os
from bs4 import BeautifulSoup


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



#
# select organism
#

org = "Escherichia coli"
doc_count = 0
print "Processing:", org


#
# 2) microbewiki
#

url = "http://microbewiki.kenyon.edu/index.php/MicrobeWiki"
print "\tsearching:", url
br.open(url)
br.select_form(nr=0)
br.form['search'] = org
print br.form
br.submit("go")
#br.submit("fulltext") # there are two options!!

html_doc = br.response().read()
soup = BeautifulSoup(html_doc, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out
txt = soup.get_text()

file = codecs.open("dat/"+org+str(doc_count), "w", "utf-8")
doc_count += 1
file.write(txt)
file.close()

quit()

h = html2text.HTML2Text()
txt = h.handle(html.decode('utf8'))
file = codecs.open("dat/"+org+str(doc_count), "w", "utf-8")
doc_count += 1
file.write(txt)
file.close()




#
# 1) wikipedia
#

url = "http://en.wikipedia.org"
print "\tsearching:", url
br.open(url)

br.select_form(nr=0)
#print br.form
br.form['search'] = org
br.submit()

wiki_ignore = [ "Main page", "Contents", "Featured content", "Current events", 
                "Random article", "Help", "About Wikipedia", "Community portal",
                "Recent changes", "Upload file", "Special pages", "About Wikipedia"
                "Disclaimers", "Help:Searching", "Disclaimers", ""]

wiki_links = []
for l in br.links():
    if l.url[:6] == "/wiki/" and l.text not in wiki_ignore:
        print "\t\t...got link:", l.text
        wiki_links.append(l)

# follow first link
if len(wiki_links) > 0:
    for i,link in enumerate(wiki_links):
        #br.follow_link(wiki_links[0])
        br.follow_link(link)
        #br.open("https://en.wikipedia.org/w/index.php?title="+wiki_links[0].url.replace("/wiki/","")+"&printable=yes")
        html = br.response().read()
        h = html2text.HTML2Text()
        txt = h.handle(html.decode('utf8'))
        file = codecs.open("dat/"+org+str(doc_count+i), "w", "utf-8")
        doc_count += 1
        file.write(txt)
        file.close()
