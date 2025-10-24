from gendiff.formatters.plain import plain_diff
from gendiff.formatters.stylish import stylish_diff
from gendiff.scripts.make_diff_view import make_diff_view
from gendiff.scripts.prepare import prepare_collections

OUTPUT_FORMATS = ['stylish', 'plain']


def generate_diff(format='stylish', *filepaths):
    coll1, coll2 = prepare_collections(*filepaths)
    view = make_diff_view(coll1, coll2)
    try:
        if format == 'plain':
            result = plain_diff(view)
        elif format == 'stylish':
            result = stylish_diff(view)
        else:
            raise ValueError
    except ValueError:
        print(f'Unknown output format, expected: {', '.join(OUTPUT_FORMATS)}')
        exit()

    print(result)
    return result
