from bs4 import BeautifulSoup
import codecs

url = "http://en.wikipedia.org"
tag = "wikiped"

wiki_ignore = [ "Main page", "Contents", "Featured content", "Current events", 
                "Random article", "Help", "About Wikipedia", "Community portal",
                "Recent changes", "Upload file", "Special pages", "About Wikipedia"
                "Disclaimers", "Help:Searching", "Disclaimers", ""]

def open(br, org):
    br.open(url)
    br.select_form(nr=0)
    #print br.form
    br.form['search'] = org
    br.submit("go")
    html_doc = br.response().read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # kill all script and style elements
    for script in soup(["script", "style"]):
            script.extract()    # rip it out
    txt = soup.get_text()

    filename = org.replace(" ","_") + "_" + tag
    file = codecs.open("dat/"+filename, "w", "utf-8")
    file.write(txt)
    file.close()



# TODO 
def fulltext():
    br.open(url)
    br.select_form(nr=0)
    #print br.form
    br.form['search'] = org
    br.submit("fulltext") # TODO add fulltext search if nothing found
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
            html_doc = br.response().read()
            
            soup = BeautifulSoup(html_doc, 'html.parser')
            # kill all script and style elements
            for script in soup(["script", "style"]):
                    script.extract()    # rip it out
            txt = soup.get_text()

            txt = h.handle(html.decode('utf8'))
            filename = org.replace(" ","_") + tag + "_" + str(i)
            file = codecs.open("dat/"+filename, "w", "utf-8")
            file.write(txt)
            file.close()
