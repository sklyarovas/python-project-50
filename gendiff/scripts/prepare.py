import json

import yaml

INPUT_FORMATS = ['json', 'yaml', 'yml']

def open_file(filepath):
    try:
        if '.json' in filepath:
            return json.load(open(filepath))
        if '.yml' in filepath or '.yaml' in filepath:
            return yaml.safe_load(open(filepath))
        else: 
            raise ValueError
    except ValueError:
        print(f'Unknown input format, expected: {', '.join(INPUT_FORMATS)}')
        exit()


def prepare_collections(*filepaths):
    return [open_file(filepath) for filepath in filepaths]
