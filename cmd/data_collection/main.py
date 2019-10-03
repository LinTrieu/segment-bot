from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import re

def collect(url):
    html = urlopen(url).read().decode("utf-8")

    sibling_soup = BeautifulSoup(html)
    for script in sibling_soup(["script", "style"]):
        script.extract()
    text = sibling_soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

