"""Solution for day 7 part 1."""

import itertools
from typing import List, Optional, Tuple

_OPERATORS = ['+', '*']
_FILE_PATH = 'submission_file.txt'


def parse_file_line(line: str) -> Tuple[int, List[str]]:
    splits = line.split(': ')
    answer = int(splits[0])
    numbers = splits[1].split()
    return (answer, numbers)

def read_file(file_path: str) -> Tuple[List[int], List[List[str]]]:
    with open(file_path, 'r') as f:
        lines = [line.rstrip() for line in f]
    parsed_lines = [parse_file_line(line) for line in lines]
    answers, number_lists = zip(*parsed_lines)
    return list(answers), list(number_lists)

def check_numbers(numbers: List[str], answer: int) -> bool:
    number_operators = len(numbers) - 1
    operator_tuples = itertools.product(_OPERATORS, repeat=number_operators)
    for operator_tuple in operator_tuples:
        if valid_expression(numbers, operator_tuple, answer):
            return True
    return False

def valid_expression(
        numbers: List[str], operators: Tuple[str], answer: int) -> bool:
    cum_result: Optional[int] = None
    initial_number = numbers[0]
    for number, operator in zip(numbers[1:], operators):
        if cum_result is None:
            cum_result = eval(f'{initial_number}{operator}{number}')
        else:
            cum_result = eval(f'{cum_result}{operator}{number}') 
        if cum_result > answer:
            return False
    return cum_result == answer

def solve(file_path: Optional[str] = None) -> int:
    file_path = file_path or _FILE_PATH
    answers, number_lists = read_file(file_path)
    cum_sum = 0
    for answer, number_list in zip(answers, number_lists):
        if check_numbers(number_list, answer):
            cum_sum += answer
    print(f'Cumulative sum: {cum_sum}.')
    return cum_sum


if __name__ == '__main__':
    solve()

