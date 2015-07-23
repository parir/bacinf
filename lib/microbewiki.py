from bs4 import BeautifulSoup
import codecs



tag = "mwiki"
url = "http://microbewiki.kenyon.edu/index.php/MicrobeWiki"

def open(br, org):
    br.open(url)
    br.select_form(nr=0)
    br.form['search'] = org
    br.submit("go")
    #br.submit("fulltext") # there are two options!!

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

