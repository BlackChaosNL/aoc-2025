
def rotate_right(score: int, start: int, rotation: str):
    n = int(rotation)
    while n > 0:
        if n > 99:
            rest = 99 + start - 100
            start = 0 + rest
        
            n = n - 99
        else:
            rest = n + start - 100
            start = 0 + rest

            n = 0

    if start == 0:
        score = score + 1
    return score, start

def rotate_left(score: int, start: int, left_boundry: int, rotation: str):
    n = int(rotation)
    while n > 0:
        if n > 99:
            rest = start - 99
            start = 100 - rest
            
            n = n - 99
        else:
            rest = n - start + 99
            start = 100 + rest

            n = 0

    if start == 0:
        score = score + 1

    # if start - int(rotation) < left_boundry:
    #     rest = int(rotation) - start
    #     start = 100 - rest
    # else:
    #     start = start - int(rotation)

    return score, start

def algorithm_part_one(input: list[str]):
    score = 0
    start = 50
    left_boundry = 0
    for cypher in input:
        direction, rotation = cypher[0], cypher[1:]
        if 'R' in direction:
            score, start = rotate_right(score, start, rotation)
        if 'L' in direction:
            score, start = rotate_left(score, start, left_boundry, rotation)
        print(start, cypher, direction, rotation)
    print(score)





def algorithm_part_two(input: list[str]):
    pass

def main(input: list[str] = [], part: int = 1):
    print(input)
    if part == 1:
        return algorithm_part_one(input=input)
    else:
        return algorithm_part_two(input=input)
