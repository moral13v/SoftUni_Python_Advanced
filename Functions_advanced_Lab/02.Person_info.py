def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


info = {"name": "George", "age": 51, "town": "Sofia"}

print(get_info(**info))

