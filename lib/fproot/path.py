def test_path(path):
    """
    Takes a path and checks if it resolves to "/"

    /           -> True
    /./         -> True
    /<dir>/../  -> True
    /<anything> -> False
    """

    length = len(path)

    # Handle single slash
    if length == 1 and path == "/":
        return True

    # Strip trailing slash
    if path[-1] == "/":
        path = path[:-1]

    # Not portable to non-unix
    split = path.split("/")[1:]
    loc = 0

    for thing in split:
        if thing == ".":
            # Same directory
            continue
        elif thing == "..":
            # One level up
            loc -= 1
        else:
            loc += 1

    if loc == 0:
        return True

    return False

