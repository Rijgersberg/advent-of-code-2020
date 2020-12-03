from pathlib import Path
import requests

with open('sessioncookie.txt') as f:
    SESSION_COOKIE = f.read().strip()


def get_input(day):
    filepath = Path(f'./input/{day}.txt')

    if not filepath.is_file():
        print(f'Fetching input file for day {day} from AdventOfCode.com...')
        inpt = requests.get(f'https://adventofcode.com/2020/day/{day}/input',
                            cookies={'session': SESSION_COOKIE}).text
        with open(filepath, 'w') as ipt_file:
            ipt_file.write(inpt)

    with open(filepath) as f:
        return f.read().splitlines()
