import os
import json


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

