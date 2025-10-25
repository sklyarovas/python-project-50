import json

import yaml


def open_file(filepath):
    if '.json' in filepath:
        return json.load(open(filepath))
    if '.yml' in filepath or '.yaml' in filepath:
        return yaml.safe_load(open(filepath))
    else: 
        raise ValueError


def prepare_collections(*filepaths):
    try:
        return [open_file(filepath) for filepath in filepaths]
    except ValueError:
        return 'input_format_error'
