import math

from util import get_input

key = {'red': 12, 'green': 13, 'blue': 14}


def day_two():
    game_ids = []
    for line in get_input("day_two"):
        game_id, game = parse_line(line)
        if not any_roll_out_of_bounds(game):
            game_ids.append(int(game_id))
    print(sum(game_ids))


def any_roll_out_of_bounds(game: list) -> bool:
    for rolls in game:
        for roll in rolls:
            color, amt = roll
            if amt > key[color]:
                return True
    return False


def parse_line(line: str) -> (str, dict):
    game_id = line.split(':')[0].split(' ')[1]
    roll_strs = line.split(':')[1].split(';')

    games = []
    for roll in roll_strs:
        cubes = [s.strip() for s in roll.split(',')]
        rolls = []
        for cube in cubes:
            amt, color = cube.split(' ')[0], cube.split(' ')[1]
            roll = (color, int(amt))
            rolls.append(roll)
        games.append(rolls)

    return game_id, games


def day_two_part_two():
    sum = 0
    for line in get_input("day_two"):
        _, game = parse_line(line)
        maxs = get_max_by_color(game)
        pow = 1
        for v in maxs.values():
            pow *= v
        sum += pow
    print(sum)


def get_max_by_color(game) -> dict:
    maxs = {
        'blue': 0,
        'red': 0,
        'green': 0,
    }
    for rolls in game:
        for roll in rolls:
            color, amt = roll
            if amt > maxs[color]:
                maxs[color] = amt
    return maxs


if __name__ == "__main__":
    day_two()
    day_two_part_two()
