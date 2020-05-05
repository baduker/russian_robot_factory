import json
import random


def random_hex_id() -> str:
    return ''.join(random.choice('0123456789abcdef') for _ in range(5))


def random_robot() -> list:
    robot_parts = json.loads(open("robot_parts.json").read())
    robot = [
        robot_parts[random_hex_id()[1]].split("\n")[:3],  # :3 -> HEAD
        robot_parts[random_hex_id()[2]].split("\n")[3:5],  # 3:5 -> TRUNK
        robot_parts[random_hex_id()[3]].split("\n")[5:7],  # 5:7 -> LEGS
    ]
    return [part for module in robot for part in module]


def load_names(file_name: str = "LAST_NAMES.txt") -> list:
    with open(file_name, "r") as f:
        return [line[:-1] for line in f]


def pick_name() -> str:
    names = load_names()
    random.shuffle(names)
    return random.choice(names)


def label_robot() -> str:
    letters = ''.join(chr(i) for i in range(65, 91))
    digits = ''.join(str(j) for j in range(0, 11))

    while True:
        label = [letters] * 3 + [digits] * 3
        return f"{pick_name()} {''.join(random.choice(char) for char in label)}"


def build_robot(no_label: bool = False) -> str:
    robot = '\n'.join(random_robot())
    if no_label:
        return robot

    return f"{robot}\n{label_robot()}"


if __name__ == "__main__":
    build_robot()
