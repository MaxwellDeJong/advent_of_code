"""Solution for day 14 part 1."""

import collections
import dataclasses
import re
from typing import List, Optional, Tuple

_WIDTH = 101
_HEIGHT = 103

_INITIAL_CONDITIONS_FILE = 'initial_conditions.txt'


def read_robot_initial_conditions(initial_conditions_file: str) -> (
        List[Tuple[Tuple[int, int], Tuple[int, int]]]):
    initial_conditions: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []
    position_regex = r'p=(\d+),(\d+)'
    velocity_regex = r'v=(-?\d+),(-?\d+)'
    with open(initial_conditions_file, 'r') as f:
        for line in f:
            position_match = re.search(position_regex, line)
            velocity_match = re.search(velocity_regex, line)
            if position_match is not None and velocity_match is not None:
                position_x = int(position_match.group(1))
                position_y = int(position_match.group(2))
                velocity_x = int(velocity_match.group(1))
                velocity_y = int(velocity_match.group(2))
                initial_conditions.append(
                    ((position_x, position_y), (velocity_x, velocity_y)))
    return initial_conditions

def initialize_robots(
        initial_conditions: List[Tuple[Tuple[int, int], Tuple[int, int]]],
        bathroom_width: int = _WIDTH,
        bathroom_height: int = _HEIGHT) -> List['Robot']:
    robots: List[Robot] = []
    for initial_position, initial_velocity in initial_conditions:
        robots.append(
            Robot(initial_position,
                  initial_velocity,
                  bathroom_width,
                  bathroom_height))
    return robots

@dataclasses.dataclass
class Robot:
    position: Tuple[int, int]
    velocity: Tuple[int, int]
    bathroom_width: int
    bathroom_height: int

    def update_position(self, n_steps: int) -> None:
        delta = [self.velocity[0] * n_steps, self.velocity[1] * n_steps]
        self.position = ((self.position[0] + delta[0]) % self.bathroom_width,
                         (self.position[1] + delta[1]) % self.bathroom_height)

    def assign_quadrant(self) -> Optional[int]:
        middle_x = self.bathroom_width // 2
        middle_y = self.bathroom_height // 2
        x, y = self.position
        if x > middle_x and y < middle_y:
            return 1
        if x < middle_x and y < middle_y:
            return 2
        if x < middle_x and y > middle_y:
            return 3
        if x > middle_x and y > middle_y:
            return 4
        return None

def get_evolved_quadrants(
        robots: List['Robot'], time_steps: int) -> List[int]:
    quadrants: List[int] = []
    for robot in robots:
        robot.update_position(time_steps)
        quadrants.append(robot.assign_quadrant())
    return [quadrant for quadrant in quadrants if quadrant is not None]

def calculate_safety_score(quadrants: List[int]) -> int:
    if quadrants == []:
        return 0
    quadrant_counter = collections.Counter(quadrants)
    cum_prod = 1
    for count in quadrant_counter.values():
        cum_prod *= count
    return cum_prod

def solve(
        initial_conditions_file: Optional[str] = None,
        bathroom_width: int = _WIDTH,
        bathroom_height: int = _HEIGHT,
        time_steps: int = 100) -> int:
    initial_conditions_file = (
        initial_conditions_file or _INITIAL_CONDITIONS_FILE)
    initial_conditions = read_robot_initial_conditions(
        initial_conditions_file)
    robots = initialize_robots(
        initial_conditions, bathroom_width, bathroom_height)
    evolved_quadrants = get_evolved_quadrants(robots, time_steps)
    return calculate_safety_score(evolved_quadrants)


if __name__ == '__main__':
    safety_score = solve()
    print(f'Safety score: {safety_score}.')

