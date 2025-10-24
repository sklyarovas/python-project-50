def format_val(val, spaces=2):
    if val is None:
        return "null"
    if isinstance(val, bool):
        return str(val).lower()
    if isinstance(val, dict):
        indent = ' ' * (spaces + 4)
        result = []
        for key, inner_val in val.items():
            end_indent = ' ' * (spaces + 2)
            formated_val = format_val(inner_val, spaces + 4)
            result.append(f'{indent}  {key}: {formated_val}\n')
        return f'{{\n{''.join(result)}{end_indent}}}'
    return f'{val}'


def stylish_diff(diff, space_count=2):
    formated_diff = []
    indent = ' ' * space_count
    plus = '+ '
    minus = '- '
    for item in diff:
        key = item['key']
        result = item['result']
        val = format_val(item.get('val'), space_count)
        old_val = format_val(item.get('old_val'), space_count)
        new_val = format_val(item.get('new_val'), space_count)

        if result == 'saved':
            formated_diff.append(f'{indent}  {key}: {val}\n')
        elif result == 'modified':
            formated_diff.append(f'{indent}{minus}{key}: {old_val}\n')
            formated_diff.append(f'{indent}{plus}{key}: {new_val}\n')
        elif result == 'removed':
            formated_diff.append(f'{indent}{minus}{key}: {val}\n')
        elif result == 'added':
            formated_diff.append(f'{indent}{plus}{key}: {val}\n')
        elif result == 'parent':
            children = stylish_diff(item.get('children'), space_count + 4)
            formated_diff.append(f'{indent}  {key}: {children}\n')

    end_indent = ' ' * (space_count - 2)

    return f'{{\n{''.join(formated_diff)}{end_indent}}}'
