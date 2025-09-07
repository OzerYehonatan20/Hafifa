import os
import json
import requests
from pathlib import Path
import base64
from bs4 import BeautifulSoup
from htmlwebshot import WebShot
from urllib.parse import urljoin
from pathlib import Path


def read_urls(file_path: str) -> list[str]:
    # read the file urls.input and return a list of urls
    urls = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            url = line.strip()
            if url:
                urls.append(url)
    return urls


def create_output_dir(base_path: str, urls: list[str]) -> list[str]:
    # create subfolders for each url, at this point the folder is empty
    os.makedirs(base_path, exist_ok=True)
    created_dirs = []
    for i, url in enumerate(urls, start=1):
        # according to i on loop, names the folders- url_1,url_2...
        folder_name = f"url_{i}"
        folder_path = os.path.join(base_path, folder_name)

        # Create the folder for the specific url
        os.makedirs(folder_path, exist_ok=True)

        # define the path of the file inside the folder
        json_path = os.path.join(folder_path, "browse.json")

        # Create an empty JSON file with html,resources and  a screenshot
        empty_data = {
            "html": "",
            "resources": [],
            "screenshot": ""
        }

        #open the filr for writing, saves empty data in json format
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(empty_data, f)

        # adds the folder's path to the folders list
        created_dirs.append(folder_path)
    return created_dirs



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


from htmlwebshot import WebShot


def take_screenshot(url: str, output_path: str) -> str:
#take a screenshot of the given url and save it as screenshot.png
    shot = WebShot()

    #this function build the full file name
    image_path = f"{output_path}/screenshot.png"

    # Create the screenshot
    shot.create_pic(url=url, output=image_path)

# returns the path of the file
    return image_path


def encode_image_to_base64(image_path: str) -> str:
    # open the  file in binary mode ("rb" = read binary)
    with open(image_path, "rb") as image_file:
        # read all the bites from the file
        image_bites = image_file.read()

        # encode the bites into base64 (binary -> text)
        encoded_string = base64.b64encode(image_bites)

        # decode to normal string (utf-8) so we can put it in a JSON FILES
        return encoded_string.decode("utf-8")

def save_to_json(output_path: str, html: str, resources: list[str], screenshot_b64: str) -> None:
    # put all the  names into a dictionary
    data = {
        "html": html,
        "resources": resources,
        "screenshot": screenshot_b64
    }
    # build the file path to browse.json
    file_path = os.path.join(output_path, "browse.json")

    # open the file for writing ("w"), and save the dictionary as JSON filee
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


