"""Solution for day 9 part 2."""

from typing import Dict, List, Optional, Tuple

_DENSE_DISK_MAP_FILE = 'disk_map.txt'


def uncompress_disk_map(
        disk_map: str) -> Tuple[List[str], Dict[str, Tuple[int, int]]]:
    uncompressed_disk_map: List[str] = []
    files: Dict[str, Tuple[int, int]] = {}
    for i, digit_str in enumerate(disk_map):
        count = int(digit_str)
        if not i % 2:
            char = str(i // 2)
            initial_idx = len(uncompressed_disk_map)
            files[char] = (initial_idx, count)
        else:
            char = '.'
        for _ in range(count):
            uncompressed_disk_map.append(char)
    return uncompressed_disk_map, files

def find_first_free_block(disk_map_list: List[str], offset: int = 0) -> int:
    for i, e in enumerate(disk_map_list[offset:]):
        if e == '.':
            return i + offset

def find_sufficient_free_block_initial_index(
        l_ptr: int,
        file_size: int,
        disk_map_list: List[str]) -> Optional[int]:
    free_count = 0
    for idx in range(l_ptr, len(disk_map_list)):
        if disk_map_list[idx] == '.':
            free_count += 1
            if free_count == file_size:
                return idx - free_count + 1
        else:
            free_count = 0
    return None

def defragment(
        uncompressed_disk_map: List[str],
        files: Dict[str, Tuple[int, int]]) -> List[str]:
    disk_map_list = list(uncompressed_disk_map)
    l_ptr = find_first_free_block(disk_map_list)
    count = 0
    for file_id in list(files.keys())[::-1]:
        str_index, file_size = files[file_id]
        initial_block_idx = find_sufficient_free_block_initial_index(
            l_ptr, file_size, disk_map_list)
        if initial_block_idx is not None:
            if initial_block_idx < str_index:
                for i in range(
                        initial_block_idx, initial_block_idx + file_size):
                    disk_map_list[i] = file_id
                for i in range(str_index, str_index + file_size):
                    disk_map_list[i] = '.'
                count += 1
            l_ptr = find_first_free_block(disk_map_list, l_ptr)
    return disk_map_list

def calc_checksum(defragged_disk_map: str, verbose: bool = False):
    cum_sum = 0
    for i, digit_str in enumerate(defragged_disk_map):
        if digit_str != '.':
            cum_sum += i * int(digit_str)
        if verbose:
            if i % 500 == 0:
                print(f'Running cum sum: {cum_sum / 1e9}.')
    return cum_sum

def solve(dense_disk_map_file: Optional[str] = None) -> int:
    dense_disk_map_file = dense_disk_map_file or _DENSE_DISK_MAP_FILE
    with open(dense_disk_map_file, 'r') as f:
        dense_disk_map = f.read().rstrip()
    uncompressed_disk_map, files = uncompress_disk_map(dense_disk_map)
    defragged_disk_map = defragment(uncompressed_disk_map, files)
    checksum = calc_checksum(defragged_disk_map)
    print(f'Calculated checksum: {checksum}.')
    return checksum


if __name__ == '__main__':
    solve()

