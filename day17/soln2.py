"""Solution for day 17 part 2."""

from typing import List, Tuple


def get_next_output(A_value: int) -> Tuple[int, bool]:
    output = ((((A_value % 8) ^ 7) ^ 7) ^ (
        A_value // (2**((A_value % 8) ^ 7)))) % 8
    terminate = A_value // 8 == 0
    return output, terminate

def get_outputs(A: int) -> List[int]:
    outputs: List[int] = []
    terminate = False
    while not terminate:
        output, terminate = get_next_output(A)
        outputs.append(output)
        A //= 8
    return outputs

def find_next_digit(
        prev_A_values: List[int],
        program: List[int],
        iteration: int) -> List[int]:
    next_A_values: List[int] = []
    for prev_A in prev_A_values:
        for digit in range(8):
            new_A = prev_A * 8 + digit
            outputs = get_outputs(new_A)
            expected_outputs = program[-iteration:]
            if outputs == expected_outputs:
                next_A_values.append(new_A)
    return list(set(next_A_values))

def solve(program: List[int]) -> int:
    prev_A_values: List[str] = [0]
    for i in range(len(program)):
        prev_A_values = find_next_digit(prev_A_values, program, i + 1)
    return min(prev_A_values)


if __name__ == '__main__':
    program = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]
    print(f'Minimum initial A value: {solve(program)}.')

