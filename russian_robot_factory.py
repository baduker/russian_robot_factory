import json
import random


def load_parts() -> dict:
    return json.loads(open("robot_parts.json").read())


PARTS = load_parts()
DIGITS = "012345678910"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def random_hex_id():
    return ''.join(random.choice('0123456789abcdef') for _ in range(5))


def random_robot() -> list:
    hex_id = random_hex_id()
    robot_parts = PARTS["templates"]
    robot = [
        robot_parts[hex_id[0]].split("\n")[:3],  # :3 -> HEAD
        robot_parts[hex_id[1]].split("\n")[3:5],  # 3:5 -> TRUNK
        robot_parts[hex_id[2]].split("\n")[5:7],  # 5:7 -> LEGS
    ]
    return [part for module in robot for part in module]


def load_names(file_name: str = "LAST_NAMES.txt") -> list:
    with open(file_name) as f:
        return [line[:-1] for line in f]


def pick_name() -> str:
    names = load_names()
    random.shuffle(names)
    return random.choice(names)


def label_robot() -> str:
    while True:
        label = [LETTERS] * 3 + [DIGITS] * 3
        return f"{pick_name()} {''.join(random.choice(char) for char in label)}"


def replacer(body: list):
    hex_id = random_hex_id()

    eyes = 1
    new_eyes = PARTS["eyes"][hex_id[3]]
    # swap eyes
    body[eyes] = body[eyes][:6] + new_eyes + body[eyes][6+len(new_eyes):]

    mouth = 2
    new_mouth = PARTS["mouths"][hex_id[4]]
    # swap mouth
    body[mouth] = body[mouth][:7] + new_mouth + body[mouth][7+len(new_mouth):]
    return body


def build_robot(no_label: bool = False) -> str:
    robot = '\n'.join(replacer(random_robot()))
    if no_label:
        return robot

    return f"{robot}\n{label_robot()}"


if __name__ == "__main__":
    build_robot()
