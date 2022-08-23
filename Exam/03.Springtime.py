def start_spring(**kwargs):
    spring_objects = {}

    for item, type_of_item in kwargs.items():
        if type_of_item not in spring_objects:
            spring_objects[type_of_item] = []
        spring_objects[type_of_item].append(item)

    result = ""

    sorted_spring_objects = sorted(spring_objects.items(), key= lambda kvp: (-len(kvp[1]), (kvp[0])))

    for key, flowers in sorted_spring_objects:
        result += f"{key}:\n"
        sorted_flowers = sorted(flowers)
        for flower in sorted_flowers:
            result += f"-{flower}\n"

    return result

