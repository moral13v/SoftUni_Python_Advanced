class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


line = input()
domains = ['com', 'bg', 'org', 'net']

while line != "End":
    if '@' not in line:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(line.split('@')[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    elif line.split('.')[-1] not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print("Email is valid")

    line = input()

