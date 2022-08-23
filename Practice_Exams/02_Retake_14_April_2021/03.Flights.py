def flights(*args):
    destination_passengers = {}

    for i in range(0, len(args), 2):
        if args[i] == "Finish":
            return destination_passengers
        try:
            if args[i] not in destination_passengers:
                destination_passengers[args[i]] = 0
            destination_passengers[args[i]] += args[i + 1]
        except IndexError:
            pass

    return destination_passengers
