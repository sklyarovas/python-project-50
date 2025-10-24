def make_diff_view(coll1, coll2):
    joined_keys = coll1.keys() | coll2.keys()
    added_keys = coll2.keys() - coll1.keys()
    removed_keys = coll1.keys() - coll2.keys()
    view = []

    for key in joined_keys:
        val1 = coll1.get(key)
        val2 = coll2.get(key)

        if key in added_keys:
            view.append({
                'result': 'added',
                'key': key, 
                'val': val2
                })
        elif key in removed_keys:
            view.append({
                'result': 'removed',
                'key': key,
                'val': val1
                })
        elif isinstance(val1, dict) and isinstance(val2, dict):
            view.append({
                'result': 'parent',
                'key': key,
                'children': make_diff_view(val1, val2)
                })
        elif val1 != val2:
            view.append({
                'result': 'modified',
                'key': key,
                'old_val': val1,
                'new_val': val2
                })
        else:
            view.append({
                'result': 'saved',
                'key': key,
                'val': val1
                })

    sorted_view = sorted(view, key=lambda val: val['key'])

    return sorted_view
