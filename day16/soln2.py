"""Solution for day 16 part 2."""

import dataclasses
import heapq
from typing import Dict, List, Optional, Set, Tuple

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

def djikstra(
        initial_state: State,
        goal_position: Tuple[int, int],
        maze: List[str]) -> (Tuple[Dict[node_module.Node, node_module.Node],
                                   node_module.Node]):
    priority_queue: List[Tuple[int, node_module.Node]] = []
    visited_nodes: Set[node_module.Node] = set()
    heapq.heappush(priority_queue, (initial_state.cost, initial_state.node))
    min_cost_nodes = {initial_state.node: initial_state.cost}
    parent_nodes: Dict[node_module.Node, node_module.Node] = {}

    while len(priority_queue) > 0:
        current_cost, current_node = heapq.heappop(priority_queue)
        if current_node.position == goal_position:
            return parent_nodes, current_node
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
                    parent_nodes[neighboring_state.node] = [current_node]
                elif neighboring_state.cost == existing_cost:
                    parent_nodes[neighboring_state.node].append(current_node)
    raise ValueError(f'Unable to reach end position: {goal_position}.')

def find_all_positions(
        current_node: node_module.Node,
        initial_node: node_module.Node,
        parent_nodes: Dict[node_module.Node, node_module.Node],
        positions: Set[Tuple[int, int]]):
    positions.add(current_node.position)
    if current_node == initial_node:
        return
    for parent_node in parent_nodes.get(current_node, []):
        find_all_positions(
            parent_node, initial_node, parent_nodes, positions)

def extract_path_positions(
        parent_nodes: Dict[node_module.Node, node_module.Node],
        initial_node: node_module.Node,
        goal_node: node_module.Node) -> List[Tuple[int, int]]:
    path: List[Tuple[int, int]] = []
    current_node = goal_node
    while current_node != initial_node:
        path.append(current_node.position)
        current_node = parent_nodes[current_node]
    path.append(current_node.position)
    return path[::-1]

def solve(map_file: Optional[str] = None, verbose: bool = False):
    map_file = map_file or _MAP_FILE
    maze = read_maze(map_file)
    initial_state = extract_initial_state(maze)
    goal_position = extract_final_position(maze)
    maze = get_patched_maze(maze)

    parent_nodes, goal_node = djikstra(initial_state, goal_position, maze)
    positions: Set[Tuple[int, int]] = set()
    find_all_positions(goal_node, initial_state.node, parent_nodes, positions)
    if verbose:
        visited_map = []
        for i, row in enumerate(maze):
            new_row = list(row)
            for j, char in enumerate(row):
                if (i, j) in positions:
                    new_row[j] = 'O'
            visited_map.append(''.join(new_row))
        for row in visited_map:
            print(row)
    return len(positions)


if __name__ == '__main__':
    print(f'Number of unique positions: {solve()}.')

