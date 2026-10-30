import json
import os


def save_log(data):

    file_name = "logs.json"

    if os.path.exists(file_name):

        with open(file_name, "r") as file:

            logs = json.load(file)

    else:

        logs = []

    logs.append(data)

    with open(file_name, "w") as file:

        json.dump(
            logs,
            file,
            indent=4
        )