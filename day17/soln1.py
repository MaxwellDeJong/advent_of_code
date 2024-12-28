"""Solution for day 17 part 1."""

from typing import List, Optional


def get_combo_operand(operand: int, registers: List[int]) -> int:
    if operand <= 3:
        return operand
    if operand == 7:
        raise ValueError('Invalid combo operand')
    return registers[operand % 4]

def adv(operand: int, registers: List[int]) -> None:
    numerator = registers[0]
    denominator = 2**get_combo_operand(operand, registers)
    registers[0] = numerator // denominator

def bxl(operand: int, registers: List[int]) -> None:
    registers[1] = registers[1] ^ operand

def bst(operand: int, registers: List[int]) -> None:
    registers[1] = get_combo_operand(operand, registers) % 8

def jnz(operand: int, registers: List[int]) -> Optional[int]:
    if not registers[0]:
        return None
    return operand

def bxc(operand: int, registers: List[int]) -> None:
    registers[1] = registers[1] ^ registers[2]

def out(operand: int, registers: List[int]) -> int:
    return get_combo_operand(operand, registers) % 8

def bdv(operand: int, registers: List[int]) -> None:
    numerator = registers[0]
    denominator = 2**get_combo_operand(operand, registers)
    registers[1] = numerator // denominator

def cdv(operand: int, registers: List[int]) -> None:
    numerator = registers[0]
    denominator = 2**get_combo_operand(operand, registers)
    registers[2] = numerator // denominator

opcode_map = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv}

def run_program(program: List[int], registers: List[int]) -> List[int]:
    pointer = 0
    outputs: List[int] = []
    while pointer < len(program):
        print(f'Pointer={pointer}. Registers={registers}.')
        opcode = program[pointer]
        operand = program[pointer+1]
        if opcode == 3:
            result = opcode_map[opcode](operand, registers)
            if result is not None:
                pointer = result
                continue
        elif opcode == 5:
            result = opcode_map[opcode](operand, registers)
            outputs.append(result)
        else:
            opcode_map[opcode](operand, registers)
        pointer += 2
    return outputs


if __name__ == '__main__':
    registers = [64012472, 0, 0]
    program = [2,4,1,7,7,5,0,3,1,7,4,1,5,5,3,0]
    outputs = run_program(program, registers)
    print(f"Final output string: {','.join(map(str, outputs))}.")

