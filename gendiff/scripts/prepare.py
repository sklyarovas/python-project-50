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
    except FileNotFoundError as e:
        return {
            'error_type': 'file_not_found_error', 
            'description': f'File not found: {e.filename}'
        }

    except ValueError:
        return {
            'error_type': 'input_format_error', 
            'description': ''
        }
