"""Solution for day 14 part 2."""

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
        self.position = ((self.position[0] + delta[0]) % _WIDTH,
                         (self.position[1] + delta[1]) % _HEIGHT)

    def get_triangle_coordinates(self) -> List[Tuple[int, int]]:
        return [(self.position[0] - 1, self.position[1] + 1),
                (self.position[0], self.position[1] + 1),
                (self.position[0] + 1, self.position[1] + 1)]


def count_triangles(robots: List['Robot']) -> int:
    n_triangles = 0
    coordinates = [robot.position for robot in robots]
    for robot in robots:
        triangle_coordinates = robot.get_triangle_coordinates()
        n_triangles += all(
            coordinate in coordinates for coordinate in triangle_coordinates)
    return n_triangles

def render_map(robots: List['Robot']) -> None:
    locations = [robot.position for robot in robots]
    for i in range(_HEIGHT):
        x_values = [location[0] for location in locations if location[1] == i]
        chars = ''
        for j in range(_WIDTH):
            if j in x_values:
                chars += 'x'
            else:
                chars += '.'
        print(chars)

def solve(
        initial_conditions_file: Optional[str] = None,
        bathroom_width: int = _WIDTH,
        bathroom_height: int = _HEIGHT,
        max_time_steps: int = 20000) -> int:
    initial_conditions_file = (
        initial_conditions_file or _INITIAL_CONDITIONS_FILE)
    initial_conditions = read_robot_initial_conditions(
        initial_conditions_file)
    robots = initialize_robots(
        initial_conditions, bathroom_width, bathroom_height)
    max_triangles = 0
    for i in range(1, max_time_steps):
        for robot in robots:
            robot.update_position(1)
        n_triangles = count_triangles(robots)
        if n_triangles > max_triangles:
            print(f'===========Iteration {i}===========')
            render_map(robots)
            max_triangles =  n_triangles
    return i


if __name__ == '__main__':
    max_triangle_iteration = solve()
    print(f'Suspected tree iteration: {max_triangle_iteration}.')

