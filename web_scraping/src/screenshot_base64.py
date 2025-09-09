import base64
from playwright.sync_api import sync_playwright

def take_screenshot(url: str) -> str:
    # take a screenshot of the given url and save it as screenshot.png
    image_path = f"output/{url.split('://')[-1]}/screenshot.png"

    # create the screenshot using Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # set headless=False to see the browser window
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(url)  # wait until network is idle to ensure page load
        page.screenshot(path=image_path, full_page=True)  # capture full page screenshot
        browser.close()

    # return the path of the file
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