"""Json utility functions."""
import os
import json

from . import markdown as md
from . import constants as cts


def get_json_files(dir_path):
    """Get JSON files in a directory."""
    json_files = [
        os.path.join(dir_path, js)
        for js in os.listdir(dir_path)
        if js.endswith(cts.JSON_EXT)
    ]
    raw_json_lst = []
    for json_file in json_files:
        with open(json_file) as file:
            raw_json_lst.append(json.load(file))
    return raw_json_lst


def clean_report(raw_json_lst):
    """Filter out unwanted key items and updated with md parsing."""
    clean_json = []
    for item in raw_json_lst:
        filtered = {
            k.lower(): v for k, v in item.items() if k in cts.REPORT_KEYS}
        md_dict = md.md_parser(filtered[cts.REPORT_REFLECTION.lower()])
        filtered.update(md_dict)
        del filtered[cts.REPORT_REFLECTION]
        clean_json.append(filtered)
    return clean_json