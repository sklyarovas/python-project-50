from gendiff import make_diff, prepare_collections
from gendiff.formatters.stylish import stylish_diff


def core(format, *filepaths):
    coll1, coll2 = prepare_collections(*filepaths)
    diff = make_diff(coll1, coll2)
    formated_diff = stylish_diff(diff)

    print(formated_diff)
    return formated_diff
