"Solution for day 13 part 2."""

import dataclasses
import re
from typing import List, Optional, Sequence, Tuple, Union
import numpy as np

_Number = Union[int, float]

_RULES_FILE = 'rules.txt'
_A_COST = 3
_B_COST = 1
_POSITION_OFFSET = 10000000000000


def invert_matrix(mat: List[List[_Number]]) -> List[List[_Number]]:
    det = mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    return [[mat[1][1] / det, -1 * mat[0][1] / det],
            [-1 * mat[1][0] / det, mat[0][0] / det]]

def mat_mul(mat: List[List[_Number]], vec: List[_Number]) -> List[_Number]:
    return [mat[0][0] * vec[0] + mat[0][1] * vec[1],
            mat[1][0] * vec[0] + mat[1][1] * vec[1]]


@dataclasses.dataclass
class Prize:
    A_movement: Tuple[int, int]
    B_movement: Tuple[int, int]
    prize_location: Tuple[int, int]

    def _is_integer_solution(self, vec: List[_Number]) -> bool:
        x_position = (round(vec[0]) * self.A_movement[0] +
                      round(vec[1]) * self.B_movement[0])
        y_position = (round(vec[0]) * self.A_movement[1] +
                      round(vec[1]) * self.B_movement[1])
        return ((x_position == round(self.prize_location[0])) and
                (y_position == round(self.prize_location[1])))

    def solve(self) -> Optional[int]:
        movement_matrix = [[self.A_movement[0], self.B_movement[0]],
                           [self.A_movement[1], self.B_movement[1]]]
        position_vector = list(self.prize_location)
        presses = mat_mul(invert_matrix(movement_matrix), position_vector)
        if self._is_integer_solution(presses):
            return round(presses[0] * _A_COST + presses[1] * _B_COST)
        return None


def read_rules_file(rules_file: str) -> List[Prize]:

    def parse_match(match_obj: re.Match) -> Tuple[int, int]:
        return (int(match_obj.group(1)), int(match_obj.group(2)))

    A_regex = r'Button A: X\+(\d+), Y\+(\d+)'
    B_regex = r'Button B: X\+(\d+), Y\+(\d+)'
    prize_regex = r'Prize: X=(\d+), Y=(\d+)'

    A_values: List[Tuple[int, int]] = []
    B_values: List[Tuple[int, int]] = []
    prize_values: List[Tuple[int, int]] = []
    with open(rules_file, 'r') as f:
        for line in f:
            A_match = re.match(A_regex, line)
            if A_match:
                A_values.append(parse_match(A_match))
                continue
            B_match = re.match(B_regex, line)
            if B_match:
                B_values.append(parse_match(B_match))
                continue
            prize_match = re.match(prize_regex, line)
            if prize_match:
                raw_position = parse_match(prize_match)
                prize_values.append(
                    (_POSITION_OFFSET + raw_position[0],
                     _POSITION_OFFSET + raw_position[1]))
    return [
        Prize(A_value, B_value, prize_value)
        for A_value, B_value, prize_value
        in zip(A_values, B_values, prize_values)]

def solve(rules_file: Optional[str] = None) -> int:
    rules_file = rules_file or _RULES_FILE
    prizes = read_rules_file(rules_file)
    token_costs = [prize.solve() for prize in prizes]
    return sum(cost for cost in token_costs if cost is not None)


if __name__ == '__main__':
    print(f'Token cost: {solve()}.')

