import os
from src.input_output import read_urls
from src.html_resources import fetch_html, extract_resources
from src.screenshot_base64 import take_screenshot, encode_image_to_base64
from src.save_to_json import save_to_json


def main():
    # get the URL from the file
    urls = read_urls("urls.input")

    # create a folder for each url (optional: currently not used for JSON)

    output_dirs = [f'output/{url}' for url in urls]

    # processing each of the links
    for url, _ in zip(urls, output_dirs):
        print(f"Processing {url} ...")
        html = fetch_html(url)
        resources = extract_resources(html, url)

        screenshot_path = take_screenshot(url)
        screenshot_b64 = encode_image_to_base64(screenshot_path)

        # <<< key fix: save JSON to the SAME folder as the screenshot >>>
        json_dir = os.path.dirname(screenshot_path)
        save_to_json(json_dir, html, resources, screenshot_b64)

if __name__ == "__main__":
    main()
