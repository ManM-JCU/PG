import sys
import requests
import re
from urllib.parse import urljoin

def download_url_and_get_all_hrefs(url):
    """
    Stáhne obsah zadané url a vrátí seznam všech odkazů (href) nalezených v <a ... href="...">.
    - stáhne stránku pomocí requests.get()
    - zkontroluje response.status_code (resp. použije raise_for_status())
    - vyhledá href atributy (podporuje " i ')
    - relativní odkazy převede na absolutní pomocí urljoin
    - vyfiltruje mailto:, javascript:, tel: a čisté kotvy (#something)
    - vrátí seznam unikátních URL (ponechá pořadí prvního výskytu)
    """
    hrefs = []

    # stáhnout stránku
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # vyhodí výjimku pro chybové kódy

    text = response.text

    # regulární výraz, který najde href v <a ... href="..."> nebo <a ... href='...'>
    # zachytí druhý skupinou skutečnou hodnotu href
    pattern = re.compile(r'<a\s+(?:[^>]*?\s)?href=(["\'])(.*?)\1', re.IGNORECASE | re.DOTALL)

    for match in pattern.finditer(text):
        raw_href = match.group(2).strip()
        if not raw_href:
            continue

        # přeskočit ne-URL schémata
        low = raw_href.lower()
        if low.startswith('mailto:') or low.startswith('javascript:') or low.startswith('tel:'):
            continue
        if raw_href.startswith('#'):
            continue

        # převést relativní URL na absolutní
        absolute = urljoin(url, raw_href)

        # zachovat pořadí, ale pouze unikátní položky
        if absolute not in hrefs:
            hrefs.append(absolute)

    return hrefs


if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Použití: python sixth.py <url>")
            sys.exit(1)

        url = sys.argv[1]
        result = download_url_and_get_all_hrefs(url)
        for r in result:
            print(r)
    except Exception as e:
        print(f"Program skončil chybou: {e}")
        sys.exit(1)
