# Day 1
The first problem seemed quite straightforward, so I wanted knowingly decided to over-engineer my solution a bit. A few examples:
  1. We are not actually provided the schema for the list of numbers. Are they always separated by 4 spaces? What if 2 spaces is used? Or a tab? Or what if a new column appears with a timestamp? Or a header is added? To more defensively handle some of these scenarios, I used a regex to extract the numbers rather than a simpler solution.
  2. Writing functions for maximum re-use. As one example, for this problem we can safely assume that we will exclusively be working with lists of numbers. But we should be able to compute the distance given any sequence or even a generator. 
  3. Thorough testing of all public functions, including utility functions. Since today was Sunday and the problems were straightforward, I spent more time on testing than necessary. I do not want to commit to always testing my solutions this well, but I think it is a worthwhile exercise.

There isn't too much to write about the solutions themselves, since I didn't do anything particularly interesting here.
