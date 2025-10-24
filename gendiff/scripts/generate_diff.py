from gendiff.scripts.make_diff_view import make_diff_view
from gendiff.scripts.prepare import prepare_collections
from gendiff.formatters.stylish import stylish_diff


def generate_diff(format, *filepaths):
    coll1, coll2 = prepare_collections(*filepaths)
    view = make_diff_view(coll1, coll2)
    if format == 'stylish':
        result = stylish_diff(view)
    else:
        return

    print(result)
    return result
