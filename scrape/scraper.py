import requests, pprint
from bs4 import BeautifulSoup
import sys

# keywords: 
# lease break, leasebreak, lease break* (regex), lease transfer* (lease transferring), my lease, our lease, moving, takeover lease,
# current tenant, lease reassignment, lease assignment

def fetch_search_results(query=None, minAsk=None, maxAsk=None, bedrooms=None):
    search_params = {
        key: val for key, val in locals().items() if val is not None #locals() returns dictionary of current namespaces
    }
    if not search_params:
        raise ValueError("No valid keywords")

    base = 'http://newyork.craigslist.org/search/abo'
    resp = requests.get(base, params=search_params, timeout=3)
    resp.raise_for_status()  # <- no-op if status==200
    return resp.content, resp.encoding

def parse_source(html, encoding='utf-8'):
    parsed = BeautifulSoup(html, from_encoding=encoding)
    return parsed

def extract_listings(parsed): 
    """Returning a list of individual listings
    """
    #location_attrs = {'data-latitude': True, 'data-longitude': True} --- CL no longer has attrs lat/long
    listings = parsed.find_all('p', class_='row') #find_all is a beautifulsoup method
    extracted = []
    for listing in listings:
        #location = {key: listing.attrs.get(key, '') for key in location_attrs}
        link = listing.find('span', class_='pl').find('a')
        this_listing = {
            #'location': location,
            'link': link.attrs['href'],
            'description': link.string.strip()
        }
        extracted.append(this_listing)
    return extracted


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test': #sys.argv[1] is first argument after the script
        html, encoding = read_search_results()
    else:
        html, encoding = fetch_search_results(
            minAsk=1500, maxAsk=6000, bedrooms=2
        )
    doc = parse_source(html, encoding)
    listings = extract_listings(doc)
    print len(listings)
    print listings
    pprint.pprint(listings)
    #print doc.prettify(encoding=encoding)









