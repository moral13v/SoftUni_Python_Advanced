def even_odd(*args):
    if args[-1] == "even":
        return [int(x) for x in args[:-1] if int(x) % 2 == 0]
    elif args[-1] == "odd":
        return [int(x) for x in args[:-1] if int(x) % 2 != 0]


