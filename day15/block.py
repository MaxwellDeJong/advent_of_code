import dataclasses
from typing import Tuple

import movement_utils


@dataclasses.dataclass
class Block:
    left: Tuple[int, int]
    right: Tuple[int, int]

    def get_next_left_position(self, move_char: str) -> Tuple[int, int]:
        return movement_utils.get_next_position(self.left, move_char)

    def get_next_right_position(self, move_char: str) -> Tuple[int, int]:
        return movement_utils.get_next_position(self.right, move_char)

    def update(self, move_char: str) -> None:
        self.left = self.get_next_left_position(move_char)
        self.right = self.get_next_right_position(move_char)

    def gps_score(self) -> int:
        return 100 * self.left[0] + self.left[1]

