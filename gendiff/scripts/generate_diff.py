from gendiff.formatters.json import json_diff
from gendiff.formatters.plain import plain_diff
from gendiff.formatters.stylish import stylish_diff
from gendiff.scripts.make_diff_view import make_diff_view
from gendiff.scripts.prepare import prepare_collections

OUTPUT_FORMATS = ['stylish', 'plain', 'json']
OUTPUT_ERROR = f'Unknown output format, expected: {', '.join(OUTPUT_FORMATS)}'
INPUT_FORMATS = ['json', 'yaml', 'yml']
INPUT_ERROR = f'Unknown input format, expected: {', '.join(INPUT_FORMATS)}'


def generate_diff(file1_path, file2_path, format='stylish'):
    prepared = prepare_collections(file1_path, file2_path)
    if prepared == 'input_format_error':
        result = INPUT_ERROR
    else:
        view = make_diff_view(*prepared)
        try:
            if format == 'plain':
                result = plain_diff(view)
            elif format == 'stylish':
                result = stylish_diff(view)
            elif format == 'json':
                result = json_diff(view)
            else:
                raise ValueError
        except ValueError:
            result = OUTPUT_ERROR

    print(result)
    return result
