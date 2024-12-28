# Day 17

## Part 1
The first part was simply translating the text description of the operands and operators into code.

## Part 2
I decided that a general solution for an arbitrary program seemed computationally infeasible, so I started by decompiling the specific program for my input. I realized that there were three parts of the program:
  1. A series of operations that determines the register values.
  2. An output, which depends only on the value in register B.
  3. A conditional loop to return to the beginning of the program, where the condition depends only on the value in register A.

I then manually decompiled the first section, which sets the register values. If $A_0$ is the value stored in register A before any operations are applied, the final values in the registers are given by
```math
A_1 = A_0 // 8
B_1 = f_1(A_0)
C_1 = f_2(A_0)
```
This has several interesting properties. First, we see that the value in register A decreases by a factor of 8 every iteration. This means that if our program outputs 16 values, that the initial value for A must lie between $2^{15}$ and $2^{16}$. This is obviously too large a range to explore with brute force, but this is a good starting point.

Second, we see that the output value depends on the value in register B, which can be written as a function exclusively of the initial value in register A. So knowledge of the initial value of the A register before the iteration is enough to completely determine the output value.

Third, we see that the value assigned to register C is not used to update the value in register A (used to determine the conditional looping) or the value in register B (used to determine the output). So we can throw away this register entirely.

If we start at the final iteration of the loop, we know that the initial value in the A register must be less than 8 to ensure that the loop terminates. So to start, we can check the 8 possible integer values for A at the beginning of the loop to determine possible values consistent with the program outputs. Now moving backwards, we want to find the next smallest octal digit for A. We know that the next value of A must be at least a factor of 8 larger than the previous value due to our update rules. Furthermore, we know that we only need to check the next 8 digits since we only want the smallest solution and the output involves a modulo 8. In the case of multiple solutions, we can keep them all to ensure that we do not discard any valid solutions.
