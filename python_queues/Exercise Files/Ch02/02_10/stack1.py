def pairs_stack(string, pairs = {'[': ']', '{': '}', '(': ')'}):

    opening = pairs.keys()

    closing = pairs.values()

    match = list()

    for s in string:
        if s in opening:
            match.insert(0, s)
        elif s in closing:
            if len(match) == 0:
                return False
            if match[0] == opening[closing.index(s)]:
                match.pop(0)
            else:
                return False

    if len(match) == 0:
        return True

    return False