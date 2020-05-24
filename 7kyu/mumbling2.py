def accum(s):
    return '-'.join(c.upper() + i * c.lower() for i, c in enumerate(s))