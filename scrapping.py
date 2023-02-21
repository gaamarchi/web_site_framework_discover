import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://wiki.owasp.org/index.php/OWASP_favicon_database')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

# Getting the title tag
raw_input = soup.pre
framework  = str(raw_input).replace("<pre>","").replace("</pre>","")

with open("frameworkRaw.txt","w") as arquivo:
    arquivo.write(framework)
