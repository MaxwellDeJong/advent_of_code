# Day 3
I had a lot of work today as well as some evening plans, so I added quite minimal testing today and did not try to solve any generalization of the problem. But I still enjoyed the problem, particularly devising an algorithm for part 2.

## Part 1
A simple regex does the heavy lifting for us, with a bit of functional programming to transform the regular expression output into the sum of products.

## Part 2
We first use `re.finditer` to extract the indices of the matches for both of the conditionals. By comparing the indices of these matches, we can figure out the sections of the original memory string that we can remove from consideration. For example, we can drop anything after each `don't()` until the next `do()`. The resulting minified memory string can then use the same regular expression as before.
