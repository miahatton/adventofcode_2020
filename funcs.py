from typing import List

def read_input(file_loc: str, convert_to_int = False) -> List[str]:
    with open(file_loc, 'r') as f:
        if not convert_to_int:
            input_lines = f.read().splitlines()
        else:
            input_lines = [int(x) for x in f.read().splitlines()]
    return input_lines
