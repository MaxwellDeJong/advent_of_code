# Day 7

## Part 1
This was a fairly straightforward problem, at least in python. Because I have allowed myself to use the standard library, I could task `itertools` with the heavy lifting of finding all of the possible expressions to evaluate. The full expression string was decomposed into single operator instructions and evaluated using `eval` to ensure that the intended left-to-right behavior was followed.

## Part 2
This second part required only a minor modification to the solution. If the concatenation operator `||` was present, the digits were concatenated instead of using `eval`, which was still used for evaluating the previous operators.

