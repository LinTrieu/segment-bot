from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import re
import urllib.request

def collect(url):

    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )

    html = urlopen(req).read().decode("utf-8")

    sibling_soup = BeautifulSoup(html, 'html.parser')
    for script in sibling_soup(["script", "style"]):
        script.extract()
    text = sibling_soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines()
             )
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

