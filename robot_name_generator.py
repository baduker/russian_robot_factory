import random


HEAD = """ 
 ..............
 .  *      *  .
[.      '     .]
 .            .
 .     ~~     .
 ..............
"""


SOURCE = "LAST_NAMES.txt"


def read_it(file_name):
    with open(file_name, "r") as f:
        return [line[:-1] for line in f]


def gen_random_russian_name(last_names):
    random.shuffle(last_names)
    return random.choice(last_names)


def gen_random_robot_name():
    letters = ''.join(chr(i) for i in range(65, 91))
    digits = ''.join(str(j) for j in range(0, 11))
    
    while True:
        random_name = [letters] * 3 + [digits] * 3
        return ''.join(random.choice(part_of_name) for part_of_name in random_name)


def build_russion_robot():
    #batch_num = random.randint(1, 10000)
    name = gen_random_russian_name(read_it(SOURCE))
    robot_id = gen_random_robot_name()
    return name, robot_id


print(HEAD)
print("{} {}".format(*build_russion_robot()))