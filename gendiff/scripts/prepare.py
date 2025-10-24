import json
import yaml


def open_file(filepath):
    if '.json' in filepath:
        return json.load(open(filepath))
    if '.yml' or '.yaml' in filepath:
        return yaml.safe_load(open(filepath))
    raise ValueError(f'Unknown format')


def prepare_collections(*filepaths):
    return [open_file(filepath) for filepath in filepaths]
