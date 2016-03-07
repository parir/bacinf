import urllib.request

from bs4 import BeautifulSoup
import codecs

BASE_URL = "https://microbewiki.kenyon.edu/index.php/"
tag = "mwiki"


def open(org):
    response = urllib.request.urlopen(BASE_URL + org)
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    txt = soup.get_text()

    filename = org.replace(" ", "_") + "_" + tag
    file = codecs.open("dat/" + filename, "w", "utf-8")
    file.write(txt)
    file.close()
