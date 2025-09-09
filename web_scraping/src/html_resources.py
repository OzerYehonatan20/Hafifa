import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def fetch_html(url: str) -> str:
# takes out the html content from each url, returns html as a string

        # asks an access request to the urls
        response = requests.get(url)

        # Return the html text of  page
        return response.text


def extract_resources(html: str, base_url: str) -> list[str]:
    #extract all the resources
    resources = []
    soup = BeautifulSoup(html, "html.parser")

    # Find tags that usually contain resource URLs
    for tag in soup.find_all(["a", "img", "link", "script"]):
        # Check for both "href" and "src" attributes
        url = tag.get("href") or tag.get("src")
        if url:
            # combine relative URLs with the base URL (for exemple "/logo.png" becomes "http://example.com/logo.png")
            full_url = urljoin(base_url, url)
            resources.append(full_url)

# a lst of all the  resources of the urls that you load
    return resources
