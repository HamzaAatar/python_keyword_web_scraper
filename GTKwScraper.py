import codecs
import os
import urllib.request
from xml.etree import ElementTree

url = 'https://trends.google.com/trends/trendingsearches/daily/rss?geo=FR'
keywords_filename = './keywords.txt'
tmp_filename = './keywords_tmp.xml'
urllib.request.urlretrieve(url, tmp_filename)
if os.path.isfile(keywords_filename):
    with open(keywords_filename, 'r') as f:
        old_list = f.read().splitlines()
else:
    old_list = []
tree = ElementTree.parse(tmp_filename)
root = tree.getroot()
fresh_list = [title.text.lower()
              for title in root.iter('title')]
try:
    fresh_list.remove('daily search trends')
except ValueError:
    pass
output = '\n'.join(a for a in list(set(old_list + fresh_list)))
with codecs.open('./keywords.txt', 'w+', "utf-8") as f:
    f.write(output)
os.remove(tmp_filename)
