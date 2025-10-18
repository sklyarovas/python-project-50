import json


def open_file(filepath):
    return json.load(open(filepath))


def parse_files(*filepaths):
    coll1, coll2 = [open_file(filepath) for filepath in filepaths]
    print(coll1, coll2)

    return coll1, coll2