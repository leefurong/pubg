def _preceedKey(k, d):
    result = {}
    for childKey in d:
        result[k+'.'+childKey] = d[childKey]
    return result


def _flatternDict(d):
    result = {}
    for k in d:
        v = d[k]
        if type(v) is dict:
            childDict = _preceedKey(k, _flatternDict(v))
            result = {**result, **childDict}
        else:
            result[k] = v

    return result


def flattern(d):
    '''flattern a dict'''
    if type(d) is dict:
        return _flatternDict(d)
    else:
        return d
