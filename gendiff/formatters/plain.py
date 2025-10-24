def format_val(val):
    if val is None:
        return 'null'
    elif isinstance(val, bool):
        return str(val).lower()
    elif isinstance(val, str):
        return f"'{val}'"
    elif isinstance(val, dict):
        return '[complex value]'
    else:
        return str(val)


def plain_diff(diff, parents=''):
    formated_diff = []

    for item in diff:
        key = item['key']
        result = item['result']
        val = format_val(item.get('val'))
        old_val = format_val(item.get('old_val'))
        new_val = format_val(item.get('new_val'))
        path = f'{parents}.{key}' if parents else key

        if result == 'modified':
            formated_diff.append(
                f"Property '{path}' was updated. From {old_val} to {new_val}")

        if result == 'removed':
            formated_diff.append(
                f"Property '{path}' was removed")

        if result == 'added':
            formated_diff.append(
                f"Property '{path}' was added with value: {val}")

        if result == 'parent':
            formated_diff.append(plain_diff(item.get('children'), path))

    return '\n'.join(formated_diff)
