# Day 2
Today's solution was a bit less over-engineered than yesterday after a full day of work. So testing quality went down and I went for simpler solutions when reasonable, such as using `split()` rather than a regex to parse the file of numbers. But I was able to solve a bit more of an abstract problem than required that allowed for a more interesting approach.

## Part 1
This first problem was fairly straightforward again, so not much to write about it specifically.

## Part 2
This second problem was slightly more interesting. I wanted to create a fairly general solution, so I specified a constant to represent the number of bad levels that could be tolerated rather than assume that the tolerance was always a single level. This naturally led me to a recursive approach, where the original report was broken down into smaller reports with potentially offending elements removed. I did not test this recursive solution in-depth (mainly because I did not want to manually compute the solutions with larger values), but it correctly handled both of today's parts.
