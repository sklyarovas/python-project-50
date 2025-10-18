def decorated_diff(coll):
    diff = '{\n'
    for item in coll:
        if item[0] in ['+', '-']:
            diff += f'  {item}\n'
        else:
            diff += f'    {item}\n'
    diff += '}'
    return diff


def generate_diff(coll1, coll2):
    joined_coll = {**coll1, **coll2}
    sorted_coll = dict(sorted(joined_coll.items()))
    diff = []
    for key in sorted_coll:
        if key in coll1 and key in coll2 and coll1[key] == coll2[key]:
            diff.append(f'{key}: {coll1[key]}')

        if key in coll1 and key in coll2 and coll1[key] != coll2[key]:
            diff.append(f'- {key}: {coll1[key]}')
            diff.append(f'+ {key}: {coll2[key]}')

        if key in coll1 and key not in coll2:
            diff.append(f'- {key}: {coll1[key]}')

        if key in coll2 and key not in coll1:
            diff.append(f'+ {key}: {coll2[key]}')

    return decorated_diff(diff)