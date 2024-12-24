"""Solution for day 16 part 1."""

import dataclasses
import heapq
from typing import List, Optional, Set, Tuple

import node as node_module

_MOVE_COST = 1
_ORIENTATION_COST = 1000

_START_CHAR = 'S'
_GOAL_CHAR = 'E'
_INITIAL_ORIENTATION = node_module.Orientation.east

_MAP_FILE = 'map.txt'


@dataclasses.dataclass
class State:
    node: node_module.Node
    cost: int

def get_neighboring_states(
        node: node_module.Node, node_cost: int, maze: List[str]) -> (
            List['State']):
    neighbors: List['State'] = []
    if valid_position(node.next_position, maze):
        new_node = node_module.Node(node.next_position, node.orientation)
        neighbors.append(State(new_node, node_cost + _MOVE_COST))
    for new_orientation in node.single_turn_orientations:
        new_node = node_module.Node(node.position, new_orientation)
        neighbors.append(State(new_node, node_cost + _ORIENTATION_COST))
    for new_orientation in node.double_turn_orientations:
        new_node = node_module.Node(node.position, new_orientation)
        neighbors.append(
            State(new_node, node_cost + 2 * _ORIENTATION_COST))
    return neighbors


def read_maze(map_file: str) -> List[str]:
    with open(map_file, 'r') as f:
        return [line.rstrip() for line in f]

def valid_position(position: Tuple[int, int], maze: List[str]) -> bool:
    n_row = len(maze)
    n_col = len(maze[0])
    if position[0] < 0 or position[0] >= n_row:
        return False
    if position[1] < 0 or position[1] >= n_col:
        return False
    return maze[position[0]][position[1]] != '#'

def extract_initial_state(maze: List[str]) -> State:
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == _START_CHAR:
                position = (i, j)
                initial_node = node_module.Node(
                    position, _INITIAL_ORIENTATION)
                initial_cost = 0
                return State(initial_node, initial_cost)

def extract_final_position(maze: List[str]) -> Tuple[int, int]:
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == _GOAL_CHAR:
                return (i, j)

def get_patched_maze(maze: List[str]) -> List[str]:
    patched_maze: List[str] = []
    for row in maze:
        patched_maze.append(
            row.replace(_START_CHAR, '.').replace(_GOAL_CHAR, '.'))
    return patched_maze

def solve(map_file: Optional[str] = None) -> int:
    map_file = map_file or _MAP_FILE
    maze = read_maze(map_file)
    initial_state = extract_initial_state(maze)
    goal_position = extract_final_position(maze)
    maze = get_patched_maze(maze)

    priority_queue: List[Tuple[int, node_module.Node]] = []
    visited_nodes: Set[node_module.Node] = set()
    heapq.heappush(priority_queue, (initial_state.cost, initial_state.node))
    min_cost_nodes = {initial_state.node: initial_state.cost}

    while len(priority_queue) > 0:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node.position == goal_position:
            return current_cost
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            for neighboring_state in get_neighboring_states(
                    current_node, current_cost, maze):
                existing_cost = min_cost_nodes.get(
                    neighboring_state.node, float('inf'))
                if neighboring_state.cost < existing_cost:
                    min_cost_nodes[neighboring_state.node] = (
                        neighboring_state.cost)
                    heapq.heappush(
                        priority_queue,
                        (neighboring_state.cost, neighboring_state.node))
    raise ValueError(f'Unable to reach end position: {goal_position}.')


if __name__ == '__main__':
    print(f'Minimum cost: {solve(_MAP_FILE)}.')

