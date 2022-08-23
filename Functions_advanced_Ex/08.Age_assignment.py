def age_assignment(*args, **kwargs):
    names = {}
    for name in args:
        names[name] = kwargs.get(name[0])
    return names
