"""Solution for day 5 part 2."""

import ast
from typing import Dict, List, Optional, Sequence, Tuple

ORDER_RULES_FILE = 'rules.txt'
UPDATES_FILE = 'updates.txt'


def read_order_rules(order_rules_file: str) -> List[str]:
    with open(order_rules_file, 'r') as rules_file:
        return [line.rstrip() for line in rules_file]

def read_updates(updates_file: str) -> List[Tuple[int]]:
    with open(updates_file, 'r') as updates_file_obj:
        return [ast.literal_eval(line.rstrip()) for line in updates_file_obj]

def parse_order_rules(order_rules: Sequence[str]) -> Tuple[Dict[int, List[int]]]:
    before_dict: Dict[int, List[int]] = {}
    after_dict: Dict[int, List[int]] = {}
    for rule in order_rules:
        before_number, after_number = tuple(map(int, rule.split('|')))
        before_dict[after_number] = (
            before_dict.get(after_number, []) + [before_number])
        after_dict[before_number] = (
            after_dict.get(before_number, []) + [after_number])
    return before_dict, after_dict

def dictionary_violations(
        number: int,
        update_numbers: Sequence[int],
        order_dict: Dict[int, Sequence[int]]) -> int:
    excluded_numbers = order_dict.get(number, [])
    return sum(
        update_number in excluded_numbers for update_number in update_numbers)

def validate_update(
        update_sequence: Sequence[int],
        before_dict: Dict[int, Sequence[int]],
        after_dict: Dict[int, Sequence[int]]) -> bool:
    for i, number in enumerate(update_sequence):
        before_numbers = update_sequence[:i]
        after_numbers = update_sequence[i+1:]
        if (dictionary_violations(number, before_numbers, after_dict) or
                dictionary_violations(number, after_numbers, before_dict)):
            return False
    return True

def swap_in_place(update: List[int], idx1: int, idx2: int) -> None:
    val1 = update[idx1]
    val2 = update[idx2]
    update[idx1] = val2
    update[idx2] = val1

def reorder_update(
        update_sequence: Sequence[int],
        before_dict: Dict[int, Sequence[int]],
        after_dict: Dict[int, Sequence[int]]):
    update = [update_number for update_number in update_sequence]
    while not validate_update(update, before_dict, after_dict):
        for i in range(len(update) - 1):
            left_number = update[i]
            right_number = update[i+1]
            excluded_right_numbers = before_dict.get(left_number, [])
            excluded_left_numbers = after_dict.get(right_number, [])
            if (right_number in excluded_right_numbers or
                    left_number in excluded_left_numbers):
                swap_in_place(update, i, i + 1)
    return update

def score_update(
        update: Sequence[int],
        before_dict: Dict[int, Sequence[int]],
        after_dict: Dict[int, Sequence[int]]) -> int:
    update_len = len(update)
    if not update_len % 2:
        raise ValueError(f'Update {update} has undetermined middle.')
    if validate_update(update, before_dict, after_dict):
        return 0
    reordered_update = reorder_update(update, before_dict, after_dict)
    return reordered_update[update_len // 2]

def solve(
        order_rules_file: Optional[str] = None,
        updates_file: Optional[str] = None) -> int:
    order_rules_file = order_rules_file or ORDER_RULES_FILE
    updates_file = updates_file or UPDATES_FILE
    order_rules = read_order_rules(order_rules_file)
    updates = read_updates(updates_file)
    before_dict, after_dict = parse_order_rules(order_rules)
    cum_sum = sum(
        score_update(update, before_dict, after_dict) for update in updates)
    print(f'Cumulative sum: {cum_sum}.')
    return cum_sum

if __name__ == '__main__':
    solve()

