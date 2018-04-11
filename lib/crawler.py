from urllib.request import urlopen
import gzip
import re

def crawl_race_stats(zipcode):
    url='https://statisticalatlas.com/zip/'+str(zipcode)+'/Race-and-Ethnicity'
    html = urlopen(url)
    stream = html.read()
    
    source = str(gzip.decompress(stream))[2:-1]
    race_figure=source.split('<a href="#figure/race-and-ethnicity"')[1].split('<h4 class="figure-title">')[0]
    races=re.findall('<text f[^>]+>([A-Z][^<]+)<\/text>', race_figure, re.DOTALL)
    percent=re.findall('<text f[^>]+>([^>]+%)<\/text>', race_figure, re.DOTALL)
    return dict(zip(races, percent))