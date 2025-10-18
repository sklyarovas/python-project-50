from gendiff import prepare_collections, generate_diff


def core(format, *filepaths): # format пока что не используется
    coll1, coll2 = prepare_collections(*filepaths)
    diff = generate_diff(coll1, coll2)
    print(diff)

    return diff
