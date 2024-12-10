"""Solution for day 9 part 1."""

from typing import List, Optional

_DENSE_DISK_MAP_FILE = 'disk_map.txt'


def uncompress_disk_map(disk_map: str) -> List[str]:
    uncompressed_disk_map: List[str] = []
    for i, digit_str in enumerate(disk_map):
        digit = int(digit_str)
        if not i % 2:
            char = str(i // 2)
        else:
            char = '.'
        for _ in range(digit):
            uncompressed_disk_map.append(char)
    return uncompressed_disk_map

def defragment(uncompressed_disk_map: List[str]) -> List[str]:
    free_blocks = uncompressed_disk_map.count('.')
    l_ptr = 0
    r_ptr = len(uncompressed_disk_map) - 1
    disk_map_list = list(uncompressed_disk_map)
    while r_ptr >= len(disk_map_list) - free_blocks:
        while disk_map_list[l_ptr] != '.':
            l_ptr += 1
        if disk_map_list[r_ptr] == '.':
            r_ptr -= 1
        else:
            disk_map_list[l_ptr] = disk_map_list[r_ptr]
            disk_map_list[r_ptr] = '.'
            l_ptr += 1
            r_ptr -= 1
    return disk_map_list

def calc_checksum(defragged_disk_map: str, verbose: bool = False):
    cum_sum = 0
    for i, digit_str in enumerate(defragged_disk_map):
        if digit_str == '.':
            return cum_sum
        cum_sum += i * int(digit_str)
        if verbose:
            if i % 500 == 0:
                print(f'Running cum sum: {cum_sum / 1e9}.')
    return cum_sum

def solve(dense_disk_map_file: Optional[str] = None) -> int:
    dense_disk_map_file = dense_disk_map_file or _DENSE_DISK_MAP_FILE
    with open(dense_disk_map_file, 'r') as f:
        dense_disk_map = f.read().rstrip()
    uncompressed_disk_map = uncompress_disk_map(dense_disk_map)
    defragged_disk_map = defragment(uncompressed_disk_map)
    checksum = calc_checksum(defragged_disk_map)
    print(f'Calculated checksum: {checksum}.')
    return checksum


if __name__ == '__main__':
    solve()

