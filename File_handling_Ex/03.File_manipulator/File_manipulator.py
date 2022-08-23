import os

line = input()

while line != "End":

    command_args = line.split('-')
    command = command_args[0]
    file_name = command_args[1]

    if command == "Create":
        with open(f"{file_name}", "w") as file:
            pass
    elif command == "Add":
        text = command_args[2]
        with open(f"{file_name}", "a") as file:
            file.write(f"{text}\n")
    elif command == "Replace":
        old_string = command_args[2]
        new_string = command_args[3]
        try:
            with open(f"{file_name}", "r") as file:
                new_content = file.read().replace(old_string, new_string)
            with open(f"{file_name}", "w") as file:
                file.write(new_content)
        except FileNotFoundError:
            print("An error occurred")
    elif command == "Delete":
        if os.path.exists(f"{file_name}"):
            os.remove(f"{file_name}")
        else:
            print("An error occurred")

    line = input()
