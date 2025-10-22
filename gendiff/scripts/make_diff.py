def make_diff(coll1, coll2):
    joined_keys = coll1.keys() | coll2.keys()
    added_keys = coll2.keys() - coll1.keys()
    removed_keys = coll1.keys() - coll2.keys()
    diff = []

    for key in joined_keys:
        val1 = coll1.get(key)
        val2 = coll2.get(key)

        if key in added_keys:
            diff.append({
                'result': 'added',
                'key': key, 
                'val': val2
                })
        elif key in removed_keys:
            diff.append({
                'result': 'removed',
                'key': key,
                'val': val1
                })
        elif isinstance(val1, dict) and isinstance(val2, dict):
            diff.append({
                'result': 'parent',
                'key': key,
                'children': make_diff(val1, val2)
                })
        elif val1 != val2:
            diff.append({
                'result': 'modified',
                'key': key,
                'old_val': val1,
                'new_val': val2
                })
        else:
            diff.append({
                'result': 'saved',
                'key': key,
                'val': val1
                })

    sorted_diff = sorted(diff, key=lambda val: val['key'])

    print(sorted_diff)
    return sorted_diff