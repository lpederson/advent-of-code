
import re

from util import get_input


def day_one():
    sum = 0
    for line in get_input("day_one"):
        digits = [x for x in line if x.isdigit()]
        sum += int(digits[0] + digits[-1])
    print(sum)


names = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def day_one_part_2():
    s = '|'.join(names.keys())
    reg = re.compile(rf'(?=(\d|{s}))')

    sum = 0
    for line in get_input("day_one"):
        first_hit = re.findall(reg, line)[0]
        last_hit = re.findall(reg, line)[-1]

        first_hit = coerce(first_hit)
        last_hit = coerce(last_hit)

        combined = first_hit + last_hit
        sum += int(combined)

    print(sum)


def coerce(v: str) -> str:
    if not v.isdigit():
        return names[v]
    return v


if __name__ == "__main__":
    day_one()
    day_one_part_2()
