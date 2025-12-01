import argparse
from puzzles.day_one.main import main as day_one

def puzzle_dict(file: list[str], part: int, day: int=1):
    switch = {
        1: day_one(file, part),
        2: None,
        3: None,
        4: None,
        5: None,
        6: None,
        7: None,
        8: None,
        9: None,
        10: None,
        11: None,
        12: None,
    }
    return switch.get(day)

def handle_input() -> list[int]:
    exc = 0
    prt = 0
    while exc == 0:
        try:
            temp = int(input('Which AoC day would you like to see? [1-12]: '))
            if temp not in [1,2,3,4,5,6,7,8,9,10,11,12]:
                print("Not a number in the applicable range, defaulting to 1")
                exc = 1
            exc = temp
        except ValueError:
            print("Not a number, choose a number between 1-12")

    while prt == 0:
        try:
            temp = int(input(f'Which part of AoC day {exc} would you like to see? [1-2]: '))
            if temp not in [1, 2]:
                print("Not a number in the applicable range, defaulting to 1")
                prt = 1
            prt = temp
        except ValueError:
            print("Not a number, choose a number between 1-2")
    return [exc, prt]

def load_file(loc: str, example: int=0) -> list[str]:
    path = ""
    if example:
        path = "./examples/"
    else:
        path = './puzzle_inputs/'
    with open(path + loc, 'r') as file:
        c = file.read().split()
    return c

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-test', help='Uses example files for testing puzzle output.', type=bool)
    args = parser.parse_args()
    
    excersize, part = handle_input()
    fc = load_file(f'day_{excersize}_part_{part}{"" if not args.test else "_example"}.txt', args.test)
    puzzle_dict(fc, part, excersize)
    return 0
    

    

main()