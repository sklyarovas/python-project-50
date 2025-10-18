import json


def open_file(filepath):
    return json.load(open(filepath))


def prepare_collections(*filepaths):
    return [open_file(filepath) for filepath in filepaths]
